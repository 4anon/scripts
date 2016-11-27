import sys
import re

try:
	if sys.argv[1:]:
		print "File: %s" % (sys.argv[1])
		logfile = sys.argv[1]
	else:
		logfile = raw_input("Please enter a log file to parse, e.g /var/log/secure: ")
	if sys.argv[2:]:
		print "File %s" % (sys.argv[2])
		baby = sys.argv[2]
	else:
		baby = raw_input("Please enter the output name: ")
	try:
		file = open(logfile, "r")
		ips = []
		for text in file.readlines():
		   text = text.rstrip()
		   found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
		   if found:
			ips.extend(found)


		for ip in ips:
		   outfile = open(baby, "a")
		   addy = "".join(ip)
		   if addy is not '':
			  print "IP: %s" % (addy)
			  outfile.write(addy)
			  outfile.write("\n")
	finally:
		file.close()
except TypeError:
	print "hello"