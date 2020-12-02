from datetime import datetime
import re

starttime = datetime.now()
passwords = []

datafile = open("./data/day2data.txt", "r")
for aline in datafile:
    passwords.append(re.split('[-|:\s]', aline))
datafile.close()

def parsepasswords(A):
    validcount = 0
    for i in A:
        index1 = int(i[0])-1
        index2 = int(i[1])-1
        passstring = i[4]
        if (passstring[index1] == i[2]) is not (passstring[index2] == i[2]):
            validcount = validcount +1      
    return validcount

print (parsepasswords(passwords))
print (datetime.now()-starttime)