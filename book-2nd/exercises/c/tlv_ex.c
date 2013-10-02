#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <setjmp.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>

#define TIMEOUT 5

/*
 * Do not hesitate to read the man page of the functions you do not understand.
 * RTFM & STFW
 */

jmp_buf timeout_jump;

/*
 * See the comments in the main function for an explanation of this function.
 */
void timeout()
{
    longjmp(timeout_jump, 1);
}

/*
 * Read a TLV from the socket.
 *
 * @return -1 if error, 0 if boolean, len (> 0) if ascii
 */
int read_tlv(int sock, char *buf)
{
    int type, len, bytes;

    bytes = recv(sock, buf, 1, 0);  // get first byte for header data
    if (bytes == -1 || bytes == 0)
        return -1;

    type = buf[0] >> 6;     // type is encoded in the first 2 bits
    len = buf[0] & 0x3f;    // last 6 bits for length (0x3f == 0b00111111)

    bytes = recv(sock, buf+1, len, 0); // get remaining data
    if (bytes == -1 || bytes == 0)
        return -1;

    if (bytes != len) // we should have received announced length
        return -1;

    return type == 1 ? len : 0; // return length for ASCII data and 0 for boolean value
}

int main(int ac, char **av)
{
    int n, sock, ret;
    struct addrinfo hints, *res = NULL;
    char buf[65];

    if (ac < 3) {
        fprintf(stderr, "Usage: %s <host> <port>\n", av[0]);
        return 1;
    }

    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET6;         // IPv6
    hints.ai_socktype = SOCK_STREAM;    // streaming type
    hints.ai_protocol = IPPROTO_TCP;    // TCP

    /* try to resolve provided server name */
    n = getaddrinfo(av[1], av[2], &hints, &res);
    if (n != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(n));
        if (n == EAI_SYSTEM)
            perror("getaddrinfo");
        return 1;
    }

    /* create a socket with data from getaddrinfo */
    if ((sock = socket(res->ai_family, res->ai_socktype,
        res->ai_protocol)) == -1) {
        perror("socket");
        freeaddrinfo(res);
        return 1;
    }

    printf("[+] Connecting to %s:%s...\n", av[1], av[2]);

    /* if the signal SIGALRM is received, then execute function timeout() */
    signal(SIGALRM, timeout);
    /* SIGALRM will be send after TIMEOUT seconds */
    alarm(TIMEOUT);

    /*
     * Save stack context/environment in timeout_jump buffer. The function
     * setjmp() will return 0 on its first call so the execution will
     * continue. The program will then execute the connect() function
     * that can take a long time if the remote host does not respond.
     * This is why we set an alarm triggered after a given number of
     * seconds so that we do not wait indefinitely.
     * Upon reception of the SIGALRM signal, the function timeout()
     * will be executed. This function (see above) calls longjmp()
     * with timeout_jump as the first argument and 1 as the second
     * argument. This function will restore the stack context/env-
     * ironment an the program execution will continue as if we just
     * returned from the setjmp() function call but with the second
     * argument of longjmp() as the return value. This means that the
     * branching will be taken and the program will display
     * "[-] Timeout" then exit.
     */
    if (setjmp(timeout_jump) == 1) {
        printf("[-] Timeout\n");
        return 1;
    }

    if (connect(sock, res->ai_addr, res->ai_addrlen) == -1) {
        alarm(0);
        perror("connect");
        printf("[-] Failed\n");
        freeaddrinfo(res);
        return 1;
    }

    alarm(0);
    freeaddrinfo(res);

    printf("[+] Connected\n");

    if ((ret = read_tlv(sock, buf)) == -1) {
        printf("[-] Connection unexpectedly closed or invalid data\n");
        close(sock);
        return 1;
    }

    if (ret == 0) {
        printf("[+] Received boolean value: %s\n", buf[1] ? "true" : "false");
    } else {
        buf[ret+1] = 0;
        printf("[+] Received ASCII data: %s\n", buf+1);
    }

    printf("[+] Sending response...\n");

    int i = htonl(buf[0]);  // convert integer to network byte order (i.e. big endian)
    send(sock, &i, sizeof(int), 0);

    if ((ret = read_tlv(sock, buf)) == -1) {
        printf("[-] Connection unexpectedly closed or invalid data\n");
        close(sock);
        return 1;
    }

    if (ret != 0) {
        printf("[-] Invalid response received from server\n");
        close(sock);
        return 1;
    }

    if (buf[1] != 0)
        printf("[+] Response accepted.\n");
    else
        printf("[-] Response rejected.\n");

    close(sock);
    return 0;
}
