import machine
import network
import time
import umqtt.simple as mqtt
import config

# Handling interrupts
# http://docs.micropython.org/en/latest/esp8266/reference/isr_rules.html
class counter():
	count = 0
	def __init__(self,inp):
		self.first = inp
		if self.first == pin:
			self.second = pout
		else:
			self.second = pin
		self.first.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback)
	def callback(self,inp):
		init_state = self.second.value()
		start = time.ticks_ms()
		while time.ticks_diff(time.ticks_ms(),start) < 5000:
			if self.second.value() != init_state:
				if self.second == pin:	# Leave
					count = count - 1
				else:	# Enter
					count = count + 1
				mqclient.publish('libary',count)

# Led pin
led = machine.Pin(config.LED_PIN, machine.Pin.OUT)
# led = machine.Pin(2, machine.Pin.OUT)

# Initializing Network
# Need to consider SZZX
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
led.off()
sta_if.connect(config.SSID, config.passwd)
while not sta_if.isconnected():
	pass
led.on()

# Connect to server
global mqclient
mqclient = mqtt.MQTTClient(config.MQTT_ID,config.MQTT_SERVER,\
	port=config.MQTT_PORT,user=config.MQTT_USER,password=config.MQTT_PASSWD,\
	ssl=config.MQTT_SSL)
led.off()
res = mqclient.connect()
while res is not 0:
	res = mqclient.connect()
led.on()

# Initializing pins
global pin
pin = machine.Pin(config.IN_PIN, machine.Pin.IN)
global pout
pout = machine.Pin(config.OUT_PIN, machine.Pin.OUT)

# pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=enter)
# pout.irq(trigger=machine.Pin.IRQ_FALLING, handler=leave)
enter = counter(pin)
leave = counter(pout)

"""
def enter(p):
	# IRQ for people entering
	init_state = pout.value()
	start = time.tick_ms()
	while time.tick_diff(time.tick_ms(),start) < 5000:
		if pout.value() != init_state:
			mqclient.publish('libary',1)

def leave(p):
	# IRQ for people leaving
	init_state = pin.value()
	start = time.tick_ms()
	while time.tick_diff(time.tick_ms(),start) < 5000:
		if pin.value() != init_state:
			mqclient.publish('libary',-1)
"""
