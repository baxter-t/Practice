#include <stdio.h>
#include <stdlib.h>

int
readLine(char buffer[], int bufLength) 
{
    int counter = 0;
    char c;
    
    while ((c = fgetc(stdin)) != EOF && counter < bufLength) {
	
	if (c == '\n') {
	    buffer[counter++] = '\0';
	    return counter - 1;
	}

	buffer[counter++] = c;
	
    }    
    return counter - 1;
}

int main(int argc, char **argv) {
    char buf[1024];
    
    int read = readLine(buf, 1024);

    printf("Read %d char from stdin, recieved: %s\n", read, buf);

    int one, two, three;

    if (sscanf(buf, "%d %d %d", &one, &two, &three) != 3) {
	printf("Invalid input boi, ask again\n");
    } else {
	printf("%d %d %d", one, two, three);
    }
}
