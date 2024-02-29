#include "humidity_meas.h"
#define MIN_MEAS 1900
#define MAX_MEAS 2600

int measure_humidity(int sensor_pin)
{
  int sensorValue = ((analogRead(sensor_pin) - MIN_MEAS) / ((MAX_MEAS - MIN_MEAS)*0.01));
  sensorValue = 100 - sensorValue;
  if (sensorValue < 0)
  {
    return 0;
  }
  else if (sensorValue >= 100)
  {
    return 100;
  }  
  return sensorValue;
}