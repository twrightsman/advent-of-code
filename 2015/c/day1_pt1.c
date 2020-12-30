#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main() {
  int floor = 0;
  char input;

  while( read(STDIN_FILENO, &input, 1) > 0 ) {
    switch(input) {
      case '(' :
        floor += 1;
        break;
      case ')' :
        floor -= 1;
    }
  }

  printf("%d\n", floor);

  exit(EXIT_SUCCESS);
};

