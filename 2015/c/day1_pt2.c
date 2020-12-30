#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main() {
  int position = 0;
  int floor = 0;
  char input;

  while( read(STDIN_FILENO, &input, 1) > 0 ) {
    position += 1;
    switch(input) {
      case '(' :
        floor += 1;
        break;
      case ')' :
        floor -= 1;
    }

    if (floor < 0) {
      break;
    }
  }

  printf("%d\n", position);

  exit(EXIT_SUCCESS);
};

