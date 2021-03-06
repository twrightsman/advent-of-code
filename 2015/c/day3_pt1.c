#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>

#define GRID_SIZE 500
#define INTERCEPT GRID_SIZE/2


int count_visited(short unsigned grid[GRID_SIZE][GRID_SIZE]) {
  short x = 0, y = 0;
  int visited = 0;

  for (x = 0; x < GRID_SIZE; x++) {
    for (y = 0; y < GRID_SIZE; y++) {
      if (grid[x][y] >= 1) {
        visited += 1;
      }
    }
  }

  return visited;
};


int main() {
  short x = 0, y = 0;
  unsigned short grid[GRID_SIZE][GRID_SIZE] = {0};
  char input;

  grid[0 + INTERCEPT][0 + INTERCEPT] += 1;
  int i = 0;
  while( read(STDIN_FILENO, &input, 1) > 0 ) {
    switch(input) {
      case '^' :
        y += 1;
        break;
      case '>' :
        x += 1;
        break;
      case 'v' :
        y -= 1;
        break;
      case '<' :
        x -= 1;
    }

    grid[x + INTERCEPT][y + INTERCEPT] += 1;
  }

  printf("%d\n", count_visited(grid));
  exit(EXIT_SUCCESS);
};

