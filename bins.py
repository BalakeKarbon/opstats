import os
import sys
import subprocess
import json

file = open('binaries.txt','r')
data=file.readlines()
opcount=0
ops=[]
counts=[]
#percents=[]
allstats=[]
curops=[]
curcounts=[]
for line in data:
    #Using split() wont work for some programs and paths that have spaces.
    elf=line.split()[0][:-1]
    stats=json.loads(subprocess.check_output(['./opstats.sh', elf]).decode('utf-8').replace("'","\""))
    opcount=opcount+stats[0]
    for op in stats[1]:
        curops.append(op[0])
        curcounts.append(op[1])
    for op in curops:
        if op in ops:
            counts[ops.index(op)]=counts[ops.index(op)]+1
        else:
            ops.append(op)
            counts.append(1)
for op in ops:
    percent=(counts[ops.index(op)]/opcount)*100
    #percents.append(percent)
    allstats.append([op,counts[ops.index(op)],percent])
allstats=sorted(allstats,key=lambda x: x[2])

print(allstats)
print(opcount)
