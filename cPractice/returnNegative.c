/*
  Ensure always returns negative
*/

#include <stdlib.h>

int returnNegative(int num) {
  return num <= 0 ? num : -num;
}

// OR

int returnNegative2(int num) {
  return -1 * abs(num);
}

printf("%d", returnNegative(4));

printf("%d", returnNegative2(4));
