# File: securePublisher.py

# importing libraries
import time
import random
import string
import uuid
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet

# Assign MQTT broker connection
mqttHost = "localhost"
mqttPort = 1883
mqttTopic = "emergency/assist"

# Then load the symmetric key used for encryption
with open("../keys/secureKey.key", "rb") as keyFile:
    secretKey = keyFile.read()
fernetCipher = Fernet(secretKey)

# Now create a new MQTT client instance with a unique ID
publisherClient = mqtt.Client(client_id="emergencySender", protocol=mqtt.MQTTv311)

# Connect to the MQTT broker
publisherClient.connect(mqttHost, mqttPort)

# Function to simulate victim messages
def createMessage(index):
    randomCoords = f"{random.randint(1, 100)},{random.randint(1, 100)}"
    victimId = str(uuid.uuid4())  # To generate unique token
    message = f"ID:{victimId} Coordinates:{randomCoords}"
    return message

# Publish 10 unique encrypted messages
for messageCount in range(10):
    originalMessage = createMessage(messageCount)

    # Show size of plain message
    print(f"[{messageCount+1}] Original Msg Length: {len(originalMessage.encode())} bytes")

    # Encrypt the message
    encryptedPayload = fernetCipher.encrypt(originalMessage.encode())
    print(f"[{messageCount+1}] Encrypted Msg Length: {len(encryptedPayload)} bytes")

    # Publish to topic
    publisherClient.publish(mqttTopic, encryptedPayload)
    print(f"[{messageCount+1}] Published securely: {originalMessage}")
    print("-" * 50)
    time.sleep(2)

# Now disconnect from the broker
publisherClient.disconnect()
