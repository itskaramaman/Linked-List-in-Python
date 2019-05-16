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

	def delete(self,x):
		if self.head.value==x:
			self.head=self.head.next
			return
		previousNode=self.head
		current_node=self.head.next
		while current_node.value!=x:
			current_node=current_node.next
			previousNode=previousNode.next
		previousNode.next=current_node.next
		return		

	def update(self,a,b):
		x=self.head
		while x.value!=a:
			x=x.next
		x.value=b
		return	


# apple--banana--orange--kiwi--potato--tomato			

l=LinkedList()
l.insert('apple')
l.insert('banana')
l.insert('orange')
l.insert('kiwi')
l.insert('potato')
l.insert('tomato')
l.traverse()
l.delete('kiwi')
print('After deletion')
l.traverse()

l.update('potato','carrot')
print('After updation')
l.traverse()