// #include "VCNL4200.h"
// #include "VEML3328.h"
// #include "PCA9954.h"
#include <WiFi.h>
#include <Arduino.h>

// #define AUTH_TOKEN = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJEZXZpY2VDYWxsYmFja19CYW5hbmExIiwic3ZyIjoiZXUtY2VudHJhbC5hd3MudGhpbmdlci5pbyIsInVzciI6InFuZXJ0b3MifQ.8vTHgemzJKN_94FRH_F6-84_SX_FF3DaP_5FmsBZrp8'
// PCA9554 *
// pca; // Pointer to PCA9954 object (I2C expander)
// VEML3328 *veml3328; // Pointer to VEML3328 object (I2C light sensor); You can reference the object using the pointer (->) operator
// WiFiManager *wifi;

void setup()
{
  char *WIFI_SSID = "ja";
  char *WIFI_PW = "1337leet";
  // const char *AUTH_TOKEN = "0"; // Changed from 'const char' to 'const char*'

  Serial.begin(9600); // Start serial communication for debugging
  // Wire.begin(); // Initialize I2C

  // pca = new PCA9554();
  // veml3328 = new VEML3328();

  // active whitle led
  // pca->led_white_on(*pca);

  // sleep(5);
  // wifi = new WiFiManager(WIFI_SSID, WIFI_PW);
      //connect to wifi
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PW);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
      Serial.printf("WiFi Failed!\n");
      delay(2000);
  }
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.println("Setup beendet");
}

void loop()
{
// PCA9954: Lets read Configuration Register:
// uint8_t data = pca->getConfig(PCA9554_CONF_REGISTER, PCA9554_ADDRESS, 1); // read config register
// Serial.println(std::bitset<8>(data).to_string().c_str()); // to_string() returns a string representation of the bitset c_str() returns a pointer to an array that contains a null-terminated sequence of characters (i.e., a C-string) representing the current value of the string object.

// Serial.print((ALS_TURN_ON).to_ulong());
// uint16_t alsData = readALSData();
// uint16_t psData = readPSData();
// // Serial.print("ALS Data: ");
// Serial.println(alsData);
// Serial.print("PS Data: ");
// Serial.println(psData);
// uint16_t blueData = readBlue();
// Serial.println(blueData);
// PCA9954: Lets read Configuration Register:
// uint8_t data = pca->getConfig(PCA9554_CONF_REGISTER, PCA9554_ADDRESS, 1); // read config register
// Serial.println(std::bitset<8>(data).to_string().c_str()); // to_string() returns a string representation of the bitset c_str() returns a pointer to an array that contains a null-terminated sequence of characters (i.e., a C-string) representing the current value of the string object.

// Serial.print((ALS_TURN_ON).to_ulong());
// uint16_t alsData = readALSData();
// uint16_t psData = readPSData();
// // Serial.print("ALS Data: ");
// Serial.println(alsData);
// Serial.print("PS Data: ");
// Serial.println(psData);
// uint16_t blueData = readBlue();
// Serial.println(blueData);

// uint16_t greenData = veml3328->readGreen();
// uint16_t blueData = veml3328->readBlue();
// uint16_t redData = veml3328->readRed();
// Serial.print(redData);
// Serial.print(",");
// Serial.print(greenData);
// Serial.print(",");
// Serial.println(blueData);

// bool bannaYellow = veml3328->isBananaYellow();
// Serial.println(bannaYellow);

// Serial.println("test");

// trying to read command Register
// uint8_t data = getConfig(PCA9554_CONF_REGISTER, PCA9554_ADDRESS, 1);
// Serial.println(std::bitset<8>(data).to_string().c_str()); // to_string() returns a string representation of the bitset c_str() returns a pointer to an array that contains a null-terminated sequence of characters (i.e., a C-string) representing the current value of the string object.

delay(200); // Wait for 1 second before reading again
 // Start serial communication for debugging
// Wire.begin(); // Initialize I2C

// pca = new PCA9554();
// veml3328 = new VEML3328();

// active whitle led
// pca->led_white_on(*pca);

// sleep(5);
}

