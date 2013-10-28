#include <stdio.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netinet/sctp.h>
#include <string.h>
#include <errno.h>

#define	SERV_PORT		 9877			/* TCP and UDP client-servers */

/* Following shortens all the type casts of pointer arguments */
#define SA      struct sockaddr

#define	MAXLINE		4096	/* max text line length */
#define SERV_MAX_SCTP_STRM	10	/* normal maximum streams */

#ifndef HAVE_BZERO
#define bzero(ptr,n)            memset(ptr, 0, n)
/* $$.If bzero$$ */
/* $$.If memset$$ */
#endif

#define SCTP_MAXLINE    800
extern int h_errno;
void
sctpstr_cli_echoall(FILE *fp, int sock_fd, struct sockaddr *to, socklen_t tolen)
{
        struct sockaddr_in6 peeraddr;
        struct sctp_sndrcvinfo sri;
        char sendline[SCTP_MAXLINE], recvline[SCTP_MAXLINE];
        socklen_t len;
        int rd_sz,i,strsz;
        int msg_flags;

        bzero(sendline,sizeof(sendline));
        bzero(&sri,sizeof(sri));
        while (fgets(sendline, SCTP_MAXLINE - 9, fp) != NULL) {
                strsz = strlen(sendline);
                if(sendline[strsz-1] == '\n') {
                        sendline[strsz-1] = '\0';
                        strsz--;
                }
                for(i=0;i<SERV_MAX_SCTP_STRM;i++) {
                        snprintf(sendline + strsz, sizeof(sendline) - strsz,
                                ".msg.%d", i);
                        sctp_sendmsg(sock_fd, sendline, sizeof(sendline),
                                     to, tolen,
                                     0, 0,
                                     i,
                                     0, 0);
                }
                for(i=0;i<SERV_MAX_SCTP_STRM;i++) {
                        len = sizeof(peeraddr);
                        rd_sz = sctp_recvmsg(sock_fd, recvline, sizeof(recvline),
                                     (SA *)&peeraddr, &len,
                                     &sri,&msg_flags);
                        printf("From str:%d seq:%d (assoc:0x%x):",
                                sri.sinfo_stream,sri.sinfo_ssn,
                                (u_int)sri.sinfo_assoc_id);
                        printf("%.*s\n",rd_sz,recvline);
                }
        }
}


void
sctpstr_cli(FILE *fp, int sock_fd, struct sockaddr *to, socklen_t tolen)
{
        struct sockaddr_in6 peeraddr;
        struct sctp_sndrcvinfo sri;
        char sendline[MAXLINE], recvline[MAXLINE];
        socklen_t len;
        int out_sz,rd_sz;
        int msg_flags;

        bzero(&sri,sizeof(sri));
        while (fgets(sendline, MAXLINE, fp) != NULL) {
                if(sendline[0] != '[') {
                        printf("Error, line must be of the form '[streamnum]text'\n");
                        continue;
                }
                sri.sinfo_stream = strtol(&sendline[1],NULL,0);
                out_sz = strlen(sendline);
                sctp_sendmsg(sock_fd, sendline, out_sz,
                             to, tolen,
                             0, 0,
                             sri.sinfo_stream,
                             0, 0);

                len = sizeof(peeraddr);
                rd_sz = sctp_recvmsg(sock_fd, recvline, sizeof(recvline),
                             (SA *)&peeraddr, &len,
                             &sri,&msg_flags);
                printf("From str:%d seq:%d (assoc:0x%x):",
                       sri.sinfo_stream,sri.sinfo_ssn,
                       (u_int)sri.sinfo_assoc_id);
                printf("%.*s",rd_sz,recvline);
        }
}


int
main(int argc, char **argv)
{
	int sock_fd;
	struct sockaddr_in6 servaddr;
	struct sctp_event_subscribe evnts;
	int echo_to_all=0;

	if(argc < 2)
		{printf("Missing host argument - use '%s host [echo]'\n",
		       argv[0]);
		exit(1);}
	if(argc > 2) {
		printf("Echoing messages to all streams\n");
		echo_to_all = 1;
	}
        sock_fd = socket(AF_INET6, SOCK_SEQPACKET, IPPROTO_SCTP);
	if (sock_fd < 0)
  	{
    		perror("socket()");
    		exit(errno);
  	}

	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin6_family = AF_INET6;
//	servaddr.sin6_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin6_port = htons(SERV_PORT);
	if (inet_pton(AF_INET6, argv[1], &servaddr.sin6_addr) <0 )
	{
		perror("inet_pton()");
		exit(errno);
	}

	bzero(&evnts, sizeof(evnts));
	evnts.sctp_data_io_event = 1;
	setsockopt(sock_fd,IPPROTO_SCTP, SCTP_EVENTS,
		   &evnts, sizeof(evnts));
	if(echo_to_all == 0)
		sctpstr_cli(stdin,sock_fd,(SA *)&servaddr,sizeof(servaddr));
	else
		sctpstr_cli_echoall(stdin,sock_fd,(SA *)&servaddr,sizeof(servaddr));
	close(sock_fd);
	return(0);
}
