import machine
import network
import time
import urequests
import umqtt.simple as mqtt
import config

# Handle interrupts
# http://docs.micropython.org/en/latest/esp8266/reference/isr_rules.html

class counter(object):
	count = 0
	def __init__(self,inp):
		self.first = inp
		if self.first == pin:
			self.second = pout
		else:
			self.second = pin
		self.first.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback)
	def callback(self,inp):
		print('First: ',self.first)
		print('Second: ',self.second)
		print(self.__class__.count)
		init_state = self.second.value()
		start = time.ticks_ms()
		while time.ticks_diff(time.ticks_ms(),start) < 5000:
			if self.second.value() != init_state:
				if self.second == pin:	# Leave
					self.__class__.count = self.__class__.count - 1
				else:	# Enter
					self.__class__.count = self.__class__.count + 1
				print(self.__class__.count)
				mqclient.publish('libary',str(self.__class__.count))
				print('Uploaded')
				while self.second.value()!=init_state:
					pass
				break

# Handle SZZX WIFI
def szzx_connection():
	res = urequests.request(config.SZZX_TEACHER_METHOD,\
		config.SZZX_TEACHER_URL,\
		data=config.SZZX_TEACHER_DATA,\
		headers=config.SZZX_TEACHER_HEADER)
	print('Connected')
	res.close()

# Led pin
led = machine.Pin(config.LED_PIN, machine.Pin.OUT)

# Initializing Network
# Need to consider SZZX
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
led.off()
sta_if.connect(config.SSID, config.passwd)
while not sta_if.isconnected():
	pass
if config.SSID
led.on()

# Connect to SMS WIFI
szzx_connection()

# Connect to server
global mqclient
mqclient = mqtt.MQTTClient(config.MQTT_ID,config.MQTT_SERVER,\
	port=config.MQTT_PORT,user=config.MQTT_USER,password=config.MQTT_PASSWD,\
	ssl=config.MQTT_SSL)
led.off()
res = mqclient.connect()
start = time.ticks_ms()
while res is not 0:
	res = mqclient.connect()
	if (time.ticks_ms() - start) < 10000:
		exit()
led.on()

# Initializing pins
global pin
pin = machine.Pin(config.IN_PIN, machine.Pin.IN)
global pout
pout = machine.Pin(config.OUT_PIN, machine.Pin.IN)

enter = counter(pin)
leave = counter(pout)
