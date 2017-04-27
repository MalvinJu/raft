import socket
import json
import os
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler
import BaseHTTPServer
BUFFER_SIZE = 2048

hostname= "localhost"
port= 8080

filename = hostname+":"+str(port)+".log"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8083))
s.listen(1)
while 1:
	conn,addr = s.accept()
	data = conn.recv(BUFFER_SIZE)
	jsonReceive=json.loads(data)
	print data

	if os.path.exists("/"+filename) == True :
		print "MASUK"
		file = open(filename,"w")
		file.write(data)
		file.close()
	else :
		logData = []
		with open(filename) as f:
		    for line in f:
				try:
					jsonData = json.loads(line)
					if jsonData["IP_Adrress"] == jsonReceive["IP_Adrress"] :
						logData.append(data)
					else :
						logData.append(line)
				except :
					print "Not a JSON String"

		file = open(filename,"w")

		for data in logData:
			file.write(str(data))
			file.write("\n")

		file.close()

		try:
			args = self.path.split('/')
			if len(args) != 2:
				raise Exception()
			n = int(args[1])
			self.send_response(200)
			self.end_headers()

			min = 0
			minIPAddress = ""
			minPort = 0

			with open(filename) as f:
			    for line in f:
					try:
						jsonData = json.loads(line)
						if min == 0 :
							min = jsonData["CPU_Load"] 
							minIPAddress = jsonData["IP_Address"] 
							minPort = jsonData["Port"]
						elif jsonData["CPU_Load"] < min :
							min = jsonData["CPU_Load"]
							inIPAddress = jsonData["IP_Address"] 
							minPort = jsonData["Port"]
					except :
						print "Not a JSON String"

			print urllib2.urlopen("http://",IP_Address,"/",Port).read()

			self.wfile.write(str(self.calc(n)).encode('utf-8'))
		except Exception as ex:
			self.send_response(500)
			self.end_headers()
			print(ex)

		server = BaseHTTPServer.HTTPServer((hostname, port), BaseHTTPRequestHandler)
		server.serve_forever()


conn.close()
s.close()

