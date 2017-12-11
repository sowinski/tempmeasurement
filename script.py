import serial
import json
from time import gmtime, strftime
import statistics
import csv

if []:
	print "haha"
else:
	print "hoho"

def line2json(line):
	try:
		data = json.loads(line)
		data['time'] = strftime("%H:%M:%S", gmtime()) 
		return data
	except:
		return None	
	
timestr = strftime("%H:%M:%S", gmtime())
datestr = strftime("%d.%m.%Y", gmtime())
with serial.Serial('/dev/ttyUSB0', 9800, timeout=5) as ser:
	with open("test.csv", "a") as file:
		lsthum = []
		lsttmp = []
		lstindextmp = []
		curmin = strftime("%M", gmtime())
		while True:
			line = ser.readline()   # read a '\n' terminated line
			jsonob = line2json(line)		
			if jsonob:
				lsthum.append(float(jsonob['humidity']))
				lsttmp.append(float(jsonob['temperature']))
				lstindextmp.append(float(jsonob['heatindex']))
				print curmin
				if curmin != strftime("%M", gmtime()):
					curmin = strftime("%M", gmtime())				
					row = ""
					row = row + unicode(strftime("%d.%m.%Y", gmtime())) + ";"
					row = row + unicode(strftime("%H:%M:%S", gmtime()))	+ ";"
					row = row + unicode(statistics.median(lsthum)) + ";"
					row = row + unicode(statistics.median(lsttmp)) + ";"
					row = row + unicode(statistics.median(lstindextmp)) + "\n\r" 			
					print row
					file.write(row)
					file.flush()
					lsthum = []
					lsttmp = []
					lstindextmp = []
		
ser.close()
file.close()
