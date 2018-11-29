#include "Arduino.h"
#include "mqtt-ds.h"
#include "WiFiClientSecure.h"
#include "PubSubClient.h"
#include "esp_system.h"

WiFiClientSecure espClient;
PubSubClient client_mqtt(espClient);

String _deviceId;
String _devicePass;
String _topic;
String _clientId;

String getMacAddress() {
  uint8_t baseMac[6];
  esp_read_mac(baseMac, ESP_MAC_WIFI_STA);
  char baseMacChr[18] = {0};
  sprintf(baseMacChr, "%02X:%02X:%02X:%02X:%02X:%02X", baseMac[0], baseMac[1], baseMac[2], baseMac[3], baseMac[4], baseMac[5]);
  return String(baseMacChr);
}

void MqttDS::SetDeviceID(String deviceId)
{
  _deviceId = deviceId;
}

void MqttDS::SetPassword(String devicePass)
{
  _devicePass = devicePass;
}

void MqttDS::SetTopic(String topic)
{
  _topic = topic;
}

void MqttDS::SetClientID(String clientId)
{
  _clientId = clientId;
}

void MqttDS::SetWifi(const char* ssid, const char* password) {
  delay(100);
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.print(".");
  }
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Mac address: ");
  Serial.println(getMacAddress());
}

void reconnect() {
  while (!client_mqtt.connected()) {
    Serial.print("Attempting MQTT connection...");
    _clientId += String(random(0xffff), HEX);
    if (client_mqtt.connect(_clientId.c_str())) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client_mqtt.state());
      Serial.println(" try again in 5 seconds");
      delay(6000);
    }
  }
}

void MqttDS::Publish(String message){
	
}



