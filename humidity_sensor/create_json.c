#include "create_json.h"
#include <stdio.h>
#include <time.h>

#define RGB_VALUE_NUMBER 5

int create_json(int* rgb_values, int humidity_value, char* json_file, int buffer_size)
{
  time_t timer;
  time(&timer);
  if(
    snprintf(json_file, buffer_size, 
      "{\nid: %d,\ntemperature: %d,\nhumidity: %d,\ntimestamp: %d,\nred: %d,\ngreen: %d,\nblue: %d\n}",
      42,
      30,
      humidity_value,
      timer,
      rgb_values[0],
      rgb_values[1],
      rgb_values[2]
      )
    )
  {
    return 0;
  }
  else
  {
    return -1;
  }
}