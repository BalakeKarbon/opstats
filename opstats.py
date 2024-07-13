import os
import sys
import subprocess

#print(sys.argv)

if len(sys.argv) <= 1:
    print("Not enough dawg")
else:
    if os.path.isfile(sys.argv[1]):
        #data=os.system("objdump -d "+sys.argv[1])
        data=subprocess.run(["objdump","-d",sys.argv[1]],stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
        for line in data:
            #print(line)
            print(line[36:43])
    else:
        print("Malo puto")

#os.system("objdump -d")
