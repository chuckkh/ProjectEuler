### Problem 37
### Truncatable primes
### 
### I believe tries would work well for this.
### Then a queue to populate and traverse each.

import queue

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


leftTrie = TruncatablePrimeTrie(TruncatablePrimeTrie.LeftDigits)
rightTrie = TruncatablePrimeTrie(TruncatablePrimeTrie.RightDigits)

qleft = queue.Queue()
qright = queue.Queue()
for childNodeValue in leftTrie.base.children.keys():
    qleft.put(childNodeValue)
for childNodeValue in rightTrie.base.children.keys():
    qright.put(childNodeValue)










