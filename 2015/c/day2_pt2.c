#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct box {
  long length;
  long width;
  long height;
};


long smallest_perimeter(struct box box) {
  int c;
  long peri[3];
  peri[0] = 2 * (box.length + box.width);
  peri[1] = 2 * (box.width + box.height);
  peri[2] = 2 * (box.height + box.length);

  long min = peri[0];
  for (c = 1; c < 3; c++) {
    if (peri[c] < min) {
      min = peri[c];
    }
  }

  return min;
};


long bow_length(struct box box) {
  return box.length * box.width * box.height;
}


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

    total_surface_area += (smallest_perimeter(present) + bow_length(present));
  }

  free(line);
  printf("%d\n", total_surface_area);
  exit(EXIT_SUCCESS);
};
