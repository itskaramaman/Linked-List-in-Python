class Node:
	def __init__(self,value):
		self.value=value
		self.next=None	

class LinkedList(object):
	def __init__(self):
		self.head=None

	def insert(self,data):
		if self.head==None:
			self.head=Node(data)
			return
		lastnode=self.head	
		while(lastnode.next!=None):
			lastnode=lastnode.next
		lastnode.next=Node(data)

	def traverse(self):
		current_node=self.head
		while(current_node):
			print(current_node.value)
			current_node=current_node.next

l=LinkedList()
l.insert('apple')
l.insert('banana')
l.insert('orange')
l.insert('kiwi')
l.traverse()
