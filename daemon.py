import psutil
import socket
import json
import sys
import time

daemonHostname = sys.argv[1];
daemonPort = sys.argv[2];

hostname = []
port = []

with open("listNode.txt") as f:
    for line in f:
    	address = line.split(":")
    	hostname.append(address[0])
    	port.append(address[1])

while 1:
	counter = 0;
	for host in hostname:
		cpuPercentage = psutil.cpu_percent(interval=1) / psutil.cpu_count()
		ticks = time.time()

		data = {
			"Sender" : "daemon",
			"IP_Address" : daemonHostname,
			"Port" : daemonPort,
			"CPU_Load" : cpuPercentage,
			"Time" : int(ticks)
		}

		json_data = json.dumps(data)

		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, 8081))
			s.send(json_data)
			print json_data
			s.close()
		except:
			print "connection failed"

		counter = counter + 1
	time.sleep(2)

