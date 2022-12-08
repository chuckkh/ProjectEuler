### Problem 37
### Truncatable primes
### 
### I believe tries would work well for this.
### Then a queue to populate and traverse each.

import queue
from math import log10
from PEtools import PEisPrime

class TruncatablePrimeTrie:
    LeftDigits = (2,3,5,7)
    RightDigits = (3,7)
    MiddleDigits = (1,3,7,9)
    class TruncatablePrimeNode:
        def __init__(self, value, parent):
            self.parent = parent
            self.children = {}
            self.value = value
        def getValue(self):
            return self.value
        def addChild(self, childVal):
#            print("adding", childVal)
            if childVal not in self.children.keys():
                self.children[childVal] = TruncatablePrimeTrie.TruncatablePrimeNode(childVal, self)
        def getChild(self, value):
            if value in self.children.keys():
                return self.children[value]
            else:
                return None
    def __init__(self, baseNodeValues):
        self.base = self.TruncatablePrimeNode(None, None)
        for nodeValue in baseNodeValues:
            self.base.addChild(nodeValue)
    def checkNumber(self, soughtValue, reverse=False):
        node = self.base
        numLen = int(log10(soughtValue))
        found = True
        if reverse:
            start = 0
            end = numLen + 1
            incr = 1
        else:
            start = numLen
            end = -1
            incr = -1
        while start != end:
            digit = soughtValue//(10**start)%10
#            print("digit", digit)
            if digit in node.children.keys():
#                print("found", digit)
                node = node.children[digit]
                numLen -= 1
            else:
                found = False
                return None
            start += incr
        if found:
            return node
        else:
            return None

### We need to total 11 prime numbers which satisfy the conditions.
total = 0
allFound = set()

leftTrie = TruncatablePrimeTrie(TruncatablePrimeTrie.LeftDigits)
rightTrie = TruncatablePrimeTrie(TruncatablePrimeTrie.RightDigits)

qleft = queue.Queue()
qright = queue.Queue()
for childNodeValue in leftTrie.base.children.keys():
    qleft.put(childNodeValue)
for childNodeValue in rightTrie.base.children.keys():
    qright.put(childNodeValue)

#for i in range(100000):
while len(allFound) < 11:
    if qleft.empty() and qright.empty():
        break
    if not qleft.empty():
        prleft = qleft.get()
        toAdd = 0
        for digit in TruncatablePrimeTrie.MiddleDigits:
            candidate = prleft * 10 + digit
            if PEisPrime(candidate):
                toAdd += 1
#                print("left", candidate)
                leftTrie.checkNumber(prleft).addChild(digit)
                qleft.put(candidate)
                if digit in TruncatablePrimeTrie.RightDigits and candidate > 0:
                    if rightTrie.checkNumber(candidate, reverse=True):
                        total += candidate
                        allFound.add(candidate)
                        #print(candidate)
    
    if not qright.empty():
        prright = qright.get()
        toAdd = 0
        for digit in TruncatablePrimeTrie.MiddleDigits:
            candidate = int(str(digit) + str(prright))
            if PEisPrime(candidate):
                toAdd += 1
#                print("right", candidate)
                rightTrie.checkNumber(prright, reverse=True).addChild(digit)
                qright.put(candidate)
                if digit in TruncatablePrimeTrie.LeftDigits and candidate > 0:
                    if leftTrie.checkNumber(candidate):
                        total += candidate
                        allFound.add(candidate)
                        #print(candidate)
        for digit in (2,5):
            candidate = int(str(digit) + str(prright))
            if PEisPrime(candidate):
                toAdd += 1
#                print("right", candidate)
                rightTrie.checkNumber(prright, reverse=True).addChild(digit)
#                qright.put(candidate)
                if candidate > 0:
                    if leftTrie.checkNumber(candidate):
                        total += candidate
                        allFound.add(candidate)
                        #print(candidate)
    

print(sum(allFound))









