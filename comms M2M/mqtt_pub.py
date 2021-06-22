import time
import paho.mqtt.client as mqtt

broker_address = "__insert ip address of broker__"
client = mqtt.Client("__insert a name for publisher__")
client.connect(broker_address)

client.publish('__insert topic__', 28.445)