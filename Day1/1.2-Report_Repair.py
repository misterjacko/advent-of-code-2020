from datetime import datetime

starttime = datetime.now()
transactions = []

datafile = open("day1data.txt", "r")
for aline in datafile:
    transactions.append(int(aline))
datafile.close()

#this is brute force but the data set is small so :shrug:
def searchfor2020 (A):
  for i in A:
    # second2 = 2020 - i
    for j in A:
      remainder = 2020 - j - i
      if remainder in A:
        if j in A:
          return (i*j * remainder)
  return ("No Matches")

print (searchfor2020(transactions))
print (datetime.now()-starttime)
