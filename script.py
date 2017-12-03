import serial
import json
from time import gmtime, strftime
import statistics

def line2json(line):
	try:
		data = json.loads(line)
		return data
	except:
		return None	
	
timestr = strftime("%H:%M:%S", gmtime())
datestr = strftime("%d.%m.%Y", gmtime())
print timestr
print datestr
with serial.Serial('/dev/ttyUSB0', 9800, timeout=5) as ser:
	lsthum = []
	lsttmp = []
	lstindextmp = []
	while True:
		line = ser.readline()   # read a '\n' terminated line
		jsonob = line2json(line)		
		if jsonob:
			lsthum.append(jsonob['humidity'])
			lsttmp.append(jsonob['temperature'])
			lsttmp.append(jsonon['heatindex'])
		
ser.close()
