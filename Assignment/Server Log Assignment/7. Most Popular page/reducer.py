#!/usr/bin/python

import sys

count = 0
oldpath = None
highest = 0
highestPath = ""

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped

    if oldpath and oldpath != thisKey:
        #print oldpath, "\t", count
        count = 0

    oldpath = thisKey
    count = count + 1
    if highest < count:
	highest = count
	highesPath = thisKey

#if oldpath != None:
 #   print oldpath, "\t", count
print highesPath, "\t", highest

