#include <stdio.h>
#include <stdlib.h>

#include "coms.h"

int main(int argc, char **argv) {
	int socketFd = resolve_connection(4000);
	
	send_message(socketFd, "Hello from the client\n");

	printf("Message sent to server\n");
	
	return 0;

}
