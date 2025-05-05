# Secure MQTT Communication for Disaster Response

# Project Overview

As per the project requirements, I created a secure messaging flow to simulate real time communication during emergencies. This system allows victims to send encrypted help messages to a central Command and Control unit. 
I used MQTT to build the message pipeline and I applied privacy safeguards to protect sensitive details like victim identity and location.

# Tools I Used
- Python 3.11.7 (Windows version)
- Mosquitto MQTT Broker (version 2.0.21a)
- paho-mqtt (for MQTT client communication)
- cryptography (Fernet symmetric encryption)
- OS: Windows 10 (64-bit)

# Installation Steps

# Step 1: Install Required Libraries

I ran the following commands in my terminal:

pip install paho-mqtt
pip install cryptography

# Step 2: Install and Start Mosquitto

I downloaded the broker from mosquitto.org and then installed version 2.0.21a, after that I started it was using the default settings (port 1883, no TLS, no authentication). And for confirmation I checked services.msc as it was running.

I used Mosquitto's default configuration without TLS or username/password authentication. 
Instead, I applied privacy protections at the application level using Fernet encryption and UUID tokenization.

# Step 3: Generate the Encryption Key
I manually generated the encryption key and placed it inside the keys/ folder.
I used python code to generate encryption key as follows: 

Python Code: 

from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("keys/secureKey.key", "wb") as file:
    file.write(key)
	
I saved this key in the keys/ directory and both publisher and subscriber use it for encryption and decryption.

# How I Ran the System
First, I opened one terminal and ran the subscriber:
python secureSubscriber.py

Then I opened a second terminal and ran the publisher:
python securePublisher.py

The subscriber successfully decrypted and displayed the messages. Each uniquely tokenized and securely encrypted.

# Conclusion
I made sure the messages couldn't be linked to individuals by replacing real identities with UUIDs. I also encrypted the entire payload to keep the content hidden, even if someone intercepted it. These privacy enhancements work well together and don't slow down the system at all.

