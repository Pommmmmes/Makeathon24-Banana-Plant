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
#include <WiFi.h>
#include <WiFiClient.h>
extern "C" {
  #include "humidity_meas.h"
}
extern "C" {
  #include "create_json.h"
}

#define BUFFER 1000
#define DELAY 1000000

// Sensor goes to ADC 0 (0)
int sensor_pin = 0;
int sensor_value = 0;

// internet stuff
const char* ssid = "Bananuts";
const char* password = "Cheesburger!";

IPAddress gateway(192, 168, 0, 1);
IPAddress subnet(255, 255, 255, 0);
const int port = 80;
String hostname = "Bananuts-Station";


void setup() {
  init();
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    ets_delay_us(DELAY);
    Serial.println("connecting to wifi...");
  }
  Serial.println("connection established!");
}

void loop() {
  // Humidity Sensor with 12 Bit ADC conversion, transformed in 3.3 V representation
  // Max: 2600 (DRY)
  // Min; 1900 (WET)
  int dummy_rgb[5] = {111, 222, 333, 27, 0};
  sensor_value = measure_humidity(sensor_pin);
  Serial.println(sensor_value);
  char json[BUFFER]; 
  int control = create_json(dummy_rgb, sensor_value, json, BUFFER);
  

  // Need to figure out the measurement rates.
  Serial.println(json);
  ets_delay_us(DELAY);
}
