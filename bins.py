import os
import sys
import subprocess

file = open('binaries.txt','r')
data=file.readlines()
for line in data:
    print(line)
