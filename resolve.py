#!/user/bin/env python
from ast import literal_eval
from urllib import parse
import socket
import sys
import os
#Open text file with a list of urls read the lines and assign a variable
file = open('dns.txt', 'r')
lines = file.readlines()

#delete previous version of address file.
os.remove('address.html')

#iterate through lines variable, print value to screen and write value to text file
for index, line in enumerate(lines):
    # print(line.strip())
    data = socket.gethostbyname(line.strip())
    print((data), file=open("address.html", "a"))
    # print(data)
    file.close()

file.close()
