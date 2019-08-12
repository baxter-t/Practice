/**
 *  Linked list implementation in c
 */

#include <stdio.h>

// Node struct
struct Node {
	int value;
	struct Node *next;
};

struct LinkedList {
	struct Node *root;
	struct Node *tail;
};

void
add_LL(struct LinkedList *list, int value)
{
	struct Node new = {
		.value = value,
		.next = 0,
	};

	if (!list->root) {
		list->root = &new;
		list->tail = &new;
	} else {
		list->tail->next = &new;
		list->tail = &new;
	}

	printf("hello, current value: %d\n", value);
}

int
main(int argc, char **argv)
{
	struct LinkedList list;
	add_LL(&list, 1);
	add_LL(&list, 2);
	add_LL(&list, 3);
	add_LL(&list, 4);
	add_LL(&list, 5);

	struct Node *current = list.root;

	while (current) {
		printf("Value: %d\n", current->value);
		current = current->next;
	}
}
