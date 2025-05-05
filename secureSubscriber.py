# File: secureSubscriber.py

# importing all required libraries
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet

# Assign MQTT broker connection 
mqttHost = "localhost"
mqttPort = 1883
mqttTopic = "emergency/assist"

# Loading same symmetric key as used by the publisher
with open("../keys/secureKey.key", "rb") as secKey:
    secretKey = secKey.read()
fernetCipher = Fernet(secretKey)

# Function definition for receive messages
def receiveMessages(client, userdata, message):
    encryptedPayload = message.payload
    try:
        decryptedMessage = fernetCipher.decrypt(encryptedPayload).decode()
        print(f"Decrypted Message Received: {decryptedMessage}")
    except Exception as error:
        print(f"Decryption Failed: {error}")

# Create the MQTT client and assign the callback
subscriberClient = mqtt.Client(client_id="emergencyReceiver", protocol=mqtt.MQTTv311)
subscriberClient.on_message = receiveMessages

# Connect to the broker and then subscribe to the topic
subscriberClient.connect(mqttHost, mqttPort)
subscriberClient.subscribe(mqttTopic)

print("Connected successfully. Waiting for incoming secure messages on 'emergency/assist'...")
subscriberClient.loop_forever()
