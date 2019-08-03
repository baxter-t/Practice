#ifndef __COMS_H
#define __COMS_H

// Basically just a wrapper for read, adds error checking
int get_message(int sockfd, char *message);

// Sends message to given file descriptor
void send_message(int sockFd, char *message);

// Connect to port specified (defaults to local host)
// Returns file descriptor of socket
// Will exit with stderr messages and exit codes on failure
int resolve_connection(int portno);

#endif
