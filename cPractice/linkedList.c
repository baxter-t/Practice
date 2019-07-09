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
};

int main(int argc, char **argv) {
  struct LinkedList list;
  struct Node first = {
    .value = 1;
  }
}
