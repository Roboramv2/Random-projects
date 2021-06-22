import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
   print (message.payload) 

broker_address = '__insert ip address of mqtt broker__'
client = mqtt.Client("PYTHONSUB1")
client.on_message = on_message
client.connect(broker_address) 
client.loop_start()

client.subscribe('test/temperature')

try:
   while True:
      time.sleep(5)
except KeyboardInterrupt:
   client.loop_stop()
   pass 