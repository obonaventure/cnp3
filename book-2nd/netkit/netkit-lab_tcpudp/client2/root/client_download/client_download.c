#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <errno.h>
#include "client_download.h"
#define TRUE 1
#define FALSE 0
extern int h_errno;


int download()
{
  int sock = socket(AF_INET6, SOCK_STREAM, 6);  
  if (sock < 0)
  {
    perror("socket()");
    exit(errno);
  }
  
  struct sockaddr_in6 sin;
  sin.sin6_family = AF_INET6;
  sin.sin6_port = htons((unsigned short) 80);
  const char *serverip = "2001:db8:be:600d::2";
  if(inet_pton(AF_INET6, serverip, &sin.sin6_addr) < 0)
  {
    perror("inet_pton()");
    exit(errno);
  }
  
  if(connect(sock, (const struct sockaddr *) &sin, sizeof(sin)) < 0)
  {
    perror("connect()");
    exit(errno);
  }
  char *request = "GET /1Mo.zero HTTP/1.1\r\nHost: webserver\r\nConnection:Keep-Alive\r\n\r\n";
  if(send(sock, request, strlen(request), 0) < 0)
  {
    perror("send()");
    exit(errno);
  }
  int loop = TRUE;
  char buffer[10000];
  int n = 0;
  int bytereceived = 0;
  while(bytereceived < 1024000)
  {
    if((n = recv(sock, buffer, sizeof(buffer), 0)) < 0)
    {
      perror("recv()");
      exit(errno);
    }
    bytereceived += n;
    sleep(1); // 1 second
  }
  close(sock);
}


int main(const char *argv[])
{
  download();
  return 0;
}
