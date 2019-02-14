'''Epoch time converter using defined file path'''
from sys import argv
import os
count=0

f = open("/home/ash/Desktop/epoch-time", "r")
for line in f:

	if line!=0:
		count+=1
		time=line
		os.system('date +"%Y-%m-%d %H:%M:%S" -d @' + time)

print("Total count for epoch coversion is:", count)
