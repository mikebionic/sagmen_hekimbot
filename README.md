# Ardiono ESP + Python API for Doctor request accept/refuse

Sagmen Hekimbot – IoT Doctor Request System
Sagmen Hekimbot is a prototype IoT-based medical assistant that connects patients and doctors through Wi-Fi using an ESP8266 module and a Python API. Patients send consultation requests, which are displayed on the doctor’s device in real time. The doctor can accept or refuse the request directly from the interface, and the decision is instantly sent back to the patient. The system combines Arduino hardware, wireless communication, and API integration to demonstrate how robotics can streamline medical communication.

![Sagmen Hekimbot](https://mikebionic.github.io/portfolio/static/projects/web_proj/sagmen_hekimbot.webp)


This is a concept project made for competition, where we tried to implement IoT as a robotics in medicine.
You should:
1. build the arduino circuit according to PIN management
2. attach ESP8266 as a Wi-fi api communicator
3. Share Wi-fi connection
4. Run the API
5. Get the ip and port, put it in Arduino code

App principle:
1. Client sends request to a doctor
2. Doctor receives a request details in display
3. accepts or refuses the request
4. response gets back to client
