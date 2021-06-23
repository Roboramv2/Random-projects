# Random Projects

A collection of small/random projects that cannot be put in a repository of their own.
***

### Home-made flex sensor:
* Making a flex sensor with a pencil, a piece of paper, two wires, plastic sheet.
* Following the instructions in [this video](https://www.youtube.com/watch?v=SJNYbSpvlP8&t=2s).

### Line detection using Picam:
* Processing the output of a picamera to obtain the position of a curve or line.
* To be used with line-follower projects.

### Home-made flex sensor version-2:
* Making a flex sensor with a pencil, a piece of paper, two card paper pieces, two pieces of aluminium foil: following the instructions in [this article](https://www.instructables.com/How-to-Make-FLEX-Sensor-at-Home-DIY-Flex-Sensor/).
* Structured a frame for using it on my finger: using two ribbon pieces. Code for actuating a servo based on my finger movement(fingering?). Checkout the [video](https://github.com/Roboramv2/Random-projects/blob/main/3_flexv2/v2demo.mp4).

### Home-made pull sensor:
* Making a digital pull sensor out of a hexnut, some cardboard, two wires, a spring, and some glue. 
* Pulling on the sensor closes the connection between the two wires. Thus the two possible resistive states are HIGH and LOW (digital).
* Connect red wire to +5v and white wire to voltage reading instrument (such as i/p pin on arduino). Pulling the red wire will cause a signal at white wire.

### Calibrate:
* servos have to be in 0 angle to place them properly while constructing casings for a project.
* due to physical adjustments, they are usually not in their 0 angle and need code to get them there.
* this script will recalibrate the servos. 
* attach the servos one by one to pin 12 of arduino.

### Comms (M2M):
* python scripts to use mqtt.
* publish and subscribe information from/to several devices simultaneously.
* requires python libraries 'mosquitto' and 'paho-mqtt'.
* lightweight and can be integrated with windows (mqttbox) or android.

### Comms (user):
* python scripts for various comms.
* script that send sms using fast2sms service.
* script that sends a phone call using twilio services.
* script that sends email using smpt and email libraries.

### Indexer:
* choose a directory to get index for.
* the script will create an index file for the whole directory.
* includes proper file types and marks folders as folders.
* includes proper indentation to show parent child relations.

### Localization:
* opencv trained haarcascade filters are contained in the haarcascade folder.
* we can use the filters to localize specific items in images.
* for example: get bounding boxes for human faces, cat faces, etc.
* localize.py script contains the code for loading and using the filters.

### Speech:
* getfv script can be used to get feature vector from recorded wav file.
* record script has two useful functions.
* 'record' function allows us to record time samples of audio directly using python.
* 'say' function allows python to play any array as a time sampled audio.

### Resistance:
* automatic resistance value calculation.
* implemented as gui, can handle 4 band as well as 5 band resistors.
* select colors from radio buttons and click calculate to see resistance.