from sys import argv
from os import system
count=0

f = open(argv[1], "r")
for line in f:

	if line!=0:
		count+=1
		time=line
		system('date +"%Y-%m-%d %H:%M:%S" -d @' + time)

print("Total count for epoch coversion is:", count)
