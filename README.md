# Makeathon24-Banana-Plant
Makeathon24 github repo for Banana growth anlytics


# Humidity Sensor

## The Sensor

The sensor is producing an anlog output signal between 0V and 3V. This analog signal is digitalized via an analog digital converter (ADC) of the ESP32. For the ADC, the ADC1 of the ESP32 is used, since it does not intefere with the WIFI Signal of the chip.


## Connection the ESP32

The ESP32 is connected with PIN 0.