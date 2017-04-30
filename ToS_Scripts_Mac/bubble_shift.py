#Shifts all ChartBubble numbers by an inputted value

import sys
import os
import re


#number = float(input("Enter a number to shift by: "))
number= -5.25

fp = open(sys.argv[1],"rw")
data = fp.readlines()
fp.close()

f_out = open(os.path.expanduser("bubbly.txt"), "w")
f_out.write("#Found and replaced all numbers with specified number\n")
f_out.write("#\n")

for line in data:

	if line.startswith("AddChartBubble"):

	    matches = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	    for match in matches:
	        num = float(match)
	        num += number
	        line =  re.sub(match, str(num), line)

	f_out.write(line)

f_out.close()

