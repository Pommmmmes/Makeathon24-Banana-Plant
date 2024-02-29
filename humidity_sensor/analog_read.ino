/*
  Analog Input

  Demonstrates analog input by reading an analog sensor on analog pin 0 and
  turning on and off a light emitting diode(LED) connected to digital pin 13.
  The amount of time the LED will be on and off depends on the value obtained
  by analogRead().

  The circuit:
  - potentiometer
    center pin of the potentiometer to the analog input 0
    one side pin (either one) to ground
    the other side pin to +5V
  - LED
    anode (long leg) attached to digital output 13 through 220 ohm resistor
    cathode (short leg) attached to ground

  - Note: because most Arduinos have a built-in LED attached to pin 13 on the
    board, the LED is optional.

  created by David Cuartielles
  modified 30 Aug 2011
  By Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInput
*/
#include <FreeRTOSConfig.h>
#include <rom/ets_sys.h>
#include <stdio.h>
extern "C" {
  #include "humidity_meas.h"
}

#define DIVISOR 4096
#define MEAS_VOLTAGE 3.3
#define DELAY 100000
#define MEAN 100
#define MIN_MEAS 1900
#define MAX_MEAS 2600

// Sensor goes to ADC 0 (0)
int sensor_pin = 0;
int sensor_value = 0;

void setup() {
  init();
  Serial.begin(115200);

}

void loop() {
  // Humidity Sensor with 12 Bit ADC conversion, transformed in 3.3 V representation
  // Max: 2600 (DRY)
  // Min; 1900 (WET)
  
  sensor_value = measure_humidity(sensor_pin);
  Serial.println(sensor_value);
  // Need to figure out the measurement rates.
  ets_delay_us(DELAY);
}
