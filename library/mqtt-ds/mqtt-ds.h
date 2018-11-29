#ifndef MqttDS
#define MqttDS

#include "Arduino.h"
#include "WiFiClientSecure.h"
#include "PubSubClient.h"
#include "esp_system.h"

class MqttDS{
	public:
	void SetDeviceID(String deviceId);
    void SetPassword(String devicePass);
    void SetTopic(String topic);
    void SetClientID(String clientId);
    void SetWifi(const char* ssid, const char* password);
	void SecPublish(String message);
};