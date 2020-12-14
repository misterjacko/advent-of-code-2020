
from datetime import datetime
import math
from math import gcd

def readFile(filename):
  with open(filename, "r") as fh:
    lines = fh.readlines()
  return [x.strip().split(',') for x in lines]

def parseData(freshlist):
  newlist = []
  for line in freshlist:
    if line != 'x':
     newlist.append(int(line))
    else:
      newlist.append(line)
  return newlist

def part1(A):
  time = int(A[0][0])
  bus = parseData(A[1])
  closestTime = time
  closestBus = ''
  for ID in bus:
    if ID != 'x':
      nextID = math.ceil(time/int(ID))*int(ID)
      if nextID - time < closestTime:
        closestTime = nextID - time
        closestBus = ID
  return int(closestBus)*closestTime

def test():
  test_input = (readFile("test.txt"))
  assert part1(test_input) == 295
  #assert part2(test_input) == 1068781

if __name__ == "__main__":
  test()
  starttime = datetime.now()
  vals = readFile("data.txt")
  print(f"Part 1: {part1(vals)}")
  print (datetime.now()-starttime)
  #print(f"Part 2: {part2(vals)}")
  #print (datetime.now()-starttime)