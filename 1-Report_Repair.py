transactions = []

datafile = open("./data/day1data.txt", "r")
for aline in datafile:
    transactions.append(int(aline))
datafile.close()

def searchfor2020_2 (A):
  for i in A:
    remainder = 2020 - i
    if remainder in A:
      return (i*remainder)
  return ("No Matches")

#this is brute force but the data set is small so :shrug:
def searchfor2020_3 (A):
  for i in A:
    second2 = 2020 - i
    for j in A:
      remainder = 2020 - j - i
      if remainder in A:
        if j in A:
          return (i*j * remainder)
  return ("No Matches")

print (searchfor2020_3(transactions))