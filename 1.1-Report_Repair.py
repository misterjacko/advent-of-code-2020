from datetime import datetime

starttime = datetime.now()
transactions = []

datafile = open("./data/day1data.txt", "r")
for aline in datafile:
    transactions.append(int(aline))
datafile.close()

def searchfor2020 (A):
  for i in A:
    remainder = 2020 - i
    if remainder in A:
      return (i*remainder)
  return ("No Matches")

print (searchfor2020(transactions))
print (datetime.now()-starttime)
