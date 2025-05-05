# Emergency Communication Scenario with Privacy Safeguards

## Scenario Overview
In this project, I simulated a real world emergency situation where victims need to quickly send help messages with their location details. These messages are picked up by drones acting as brokers and delivered to a Command and Control (C2) unit for action.

I used MQTT as the core communication protocol to replicate this real time interaction. Victims behave as publishers,drones act as brokers (using Mosquitto) and the C2 system functions as a subscriber receiving those messages.

One of the main challenges in such a setup is privacy. If the messages are not protected properly, they could be intercepted, revealing sensitive details like who the victim is or where they are. So I designed the system to include privacy protections that address these concerns directly.

## Privacy Threats (Based on LINDDUN Framework)

I followed the LINDDUN privacy threat modeling method to identify potential issues in this system. Here is what I found:

| Threat                      | Concern Highlighted                                                          |
|:----------------------------|:-----------------------------------------------------------------------------|
|Linkability				  |	Same victim's multiple messages might be linked together       				 |
|Identifiability			  |	Unique names or details could reveal the victim’s identity					 |
|Non-repudiation			  |	Victims could be permanently tied to messages they sent						 |
|Detectability				  |	Attackers could observe when messages are sent, even if they can’t read them |
|Disclosure of Information	  |	Actual help requests or coordinates could be exposed						 |
|Unawareness				  | Victims might not realize how much information they're sharing				 |
|Non-compliance				  |	Privacy regulations could be violated without proper protections			 |

## MQTT-Specific Privacy Risks I Noticed
During testing, I realized MQTT's lightweight nature also makes it more vulnerable:

	- Wildcard subscriptions can allow an attacker to monitor everything.

	- Messages are unprotected by default, so eavesdropping is possible.

	- Timing and frequency of messages could help attackers guess patterns.

That's why I made sure to protect the payload and avoid exposing sensitive metadata.

## Privacy Enhancements I Used
To mitigate the risks I found, I applied two privacy enhancing techniques in the system:

	1. Tokenization
	Instead of using any real identifiers (like names), I used randomly generated UUIDs. This helps ensure that even if someone intercepts a message, they can not tie it back to a specific person.

	2. Payload Encryption
	I encrypted the entire message payload using symmetric encryption (Fernet). Even if a message is captured, it is unreadable without the right key.

Together, these two protections helped to maintain privacy while still allowing the system to function efficiently.

## Before vs. After Privacy Protections

| Aspect                | Without PETs                 | With PETs                                 |
|:----------------------|:-----------------------------|:------------------------------------------|	
| Victim Identifier	    | Plain names       	       | Randomized tokens                         |
| Message Visibility	| Fully readable text	       | Strongly encrypted with no readable data  |
| Risk of Data Exposure	| Extremely high	           | Significantly reduced                     |
| Legal Compliance	    | Potential privacy violations | Aligned with standard privacy principles  |

## How I Evaluated the Privacy Measures
I measured both message sizes and readability before and after applying privacy enhancements. Here is what I noticed:

	- Encrypted messages were slightly larger, but well within acceptable limits.

	- Tokenization removed any direct identifiers.

	- Overall system behavior remained smooth.

	- Privacy was significantly improved with almost no performance impact.

The encryption and tokenization worked seamlessly and didn't interfere with the real time nature of the setup.

## Conclusion: 
I learned how important it is to bake privacy into the design from the start, especially during emergencies when data is sensitive and timing is critical.

By carefully modeling the risks using LINDDUN and applying simple protections like tokenization and encryption, I was able to create a reliable and privacy conscious system. It is a great reminder that security and usability can absolutely go hand in hand with a thoughtful approach.
