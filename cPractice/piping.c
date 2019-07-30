#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define READEND 0
#define WRITEEND 1

int main() {
	
	// Two ends of the first pipe
	int toParent[2];
	int toChild[2];

	
	// Open the pipes with some error checking
	if (pipe(toParent) == -1) {
		printf("Pipe Failed\n");
		return -1;
	}
	
	if (pipe(toChild) == -1) {
		printf("Pipe Failed\n");
		return -1;
	}



	// Fork
	pid_t p = fork();

	if (!p) {
		// Zero, parent process
		printf("Hello from the Child\n");

		// Read from the parent pipe
		char stringFromParent[100];
		char reply[] = "Reply from child";

		read(toChild[READEND], stringFromParent, 100);

		// Print it
		printf("Got from parent: %s\n", stringFromParent);


		write(toParent[WRITEEND], reply, strlen(reply) + 1);

		

	} else {
		// Not zero, parent process
		printf("Hello from the Parent\n");

		char sent[] = "Message to the child";
		char stringFromChild[100];

		// Send it to the child
		write(toChild[WRITEEND], sent, strlen(sent) + 1);

		// Read from the child
		read(toParent[READEND], stringFromChild, 100);

		// Print the reply
		printf("Got from child: %s\n", stringFromChild);
	}

	return 0;
}


