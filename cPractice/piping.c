#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define READEND 0
#define WRITEEND 1


// For IPC, the child's stdin and out needs to be piped to the parent
// then exec is called, cant pass the pipe to the other process

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

		// reroute the stdout of the child
		dup2(toParent[WRITEEND], STDOUT_FILENO);
		close(toParent[WRITEEND]);

		// Call something to generate output
		char *args[] = {"ls", "-al", NULL};
		execvp(args[0], args);


		return 0;

	} else {
		// Not zero, parent process
		printf("Hello from the Parent\n");
		char stringFromChild[1000];

		// Read from the child
		read(toParent[READEND], stringFromChild, 1000);

		// Print the reply
		printf("Got from child: %s\n", stringFromChild);
	}

	return 0;
}


