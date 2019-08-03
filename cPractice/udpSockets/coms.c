#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include "util.h"
#include "coms.h"

// Basically just a wrapper for read, adds error checking
int get_message(int sockfd, char *message) {
    bzero(message, 256);
    FILE *file = fdopen(sockfd, "r");
    int n = read_line(file, &message, 0);
    fclose(file);

    return n;
}

// Sends message to given file descriptor
void send_message(int sockFd, char *message) {
    int n = write(sockFd, message, strlen(message));

    // Error checking
    if (n < 0) {
        fprintf(stderr, "Error writing to socket\n");
        exit(0);
    }
}

// Connect to port specified (defaults to local host)
// Returns file descriptor of socket
// Will exit with stderr messages and exit codes on failure
int resolve_connection(int portno) {
    char *hostname = "localhost";
    struct sockaddr_in servAddr;
    struct hostent *server;

    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        fprintf(stderr, "Failed to connect: socket() failed\n");
        exit(3);
    }

    server = gethostbyname(hostname);
    if (server == NULL) {
        fprintf(stderr, "Invalid server\n");
        exit(4);
    }
    bzero((char *) &servAddr, sizeof(servAddr));
    servAddr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&servAddr.sin_addr.s_addr,
            server->h_length);
    servAddr.sin_port = htons(portno);
    if (connect(sockfd, (struct sockaddr *) &servAddr, 
            sizeof(servAddr)) < 0) {
        fprintf(stderr, "Failed to connect: connect() failed\n");
        exit(3);
    }

    return sockfd;
}
