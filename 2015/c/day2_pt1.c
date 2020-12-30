#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct box {
  long length;
  long width;
  long height;
};


long surface_area(struct box box) {
  return (2 * box.length * box.width) + (2 * box.width * box.height) + (2 * box.height * box.length);
};


long smallest_side(struct box box) {
  int c;
  long side_areas[3];
  side_areas[0] = box.length * box.width;
  side_areas[1] = box.width * box.height;
  side_areas[2] = box.height * box.length;

  long min = side_areas[0];
  for (c = 1; c < 3; c++) {
    if (side_areas[c] < min) {
      min = side_areas[c];
    }
  }

  return min;
};


int main() {
  char *line = NULL;
  size_t len = 0;
  struct box present;
  char *token, *end;
  long total_surface_area = 0;

  while (getline(&line, &len, stdin) != -1) {

    present.length = strtol(strtok(line, "x"), &end, 10);
    present.width = strtol(strtok(NULL, "x"), &end, 10);
    present.height = strtol(strtok(NULL, "x"), &end, 10);

    total_surface_area += (surface_area(present) + smallest_side(present));
  }

  free(line);
  printf("%d\n", total_surface_area);
  exit(EXIT_SUCCESS);
};
