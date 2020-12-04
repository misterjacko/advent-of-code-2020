from datetime import datetime
import re

starttime = datetime.now()
passwords = []

datafile = open("day2data.txt", "r")
for aline in datafile:
    passwords.append(re.split('[-|:\s]', aline))
datafile.close()

def parsepasswords(A):
    validcount = 0
    for i in A:
        count = i[4].count(i[2])
        if count >= int(i[0]) and count <= int(i[1]):
            validcount = validcount +1
    return validcount

print (parsepasswords(passwords))
print (datetime.now()-starttime)