class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def setNext(self, next):
		self.next = next
	def getNext(self):
		return self.next



def hasCycle(node):
	if node:
		hashMap = {}
		while node.getNext():
			if id(node) in hashMap:
				return True
			hashMap[id(node)] = True
			node = node.getNext()
	return False

#Create a bunch of nodes for my linkedlist
firstNode = Node(0)
prevNode = firstNode
for i in range(1, 10):
	newNode = Node(i)
	prevNode.setNext(newNode)
	prevNode = newNode
print hasCycle(None)
print hasCycle(firstNode)
prevNode.setNext(firstNode)
print hasCycle(firstNode)