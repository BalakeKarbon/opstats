import os
import sys
import subprocess

file = open('opcodes.txt','r')
data=file.readlines()
opcount=0
ops=[]
counts=[]
for line in data:
    opcode=line[:-1]
    opcount=opcount+1
    if opcode in ops:
        counts[ops.index(opcode)]=counts[ops.index(opcode)]+1
    else:
        ops.append(opcode)
        counts.append(1)
percents=[]
for op in ops:
    percent=(counts[ops.index(op)]/opcount)*100
    percents.append(percent)
opstats=[]
for op in ops:
    index=ops.index(op)
    opstats.append([op,counts[index],percents[index]])

sortedopstats=sorted(opstats,key=lambda x: x[2])
for line in sortedopstats:
    print(line)
