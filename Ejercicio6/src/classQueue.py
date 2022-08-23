import numpy as np

class Queue:
	__q = None
	__capacity = 0
	__front = 0  	
	__rear = -1  		
	__count = 0  

	def __init__(self, size=1000):
		self.__q = np.empty(size, str)	
		self.__capacity = size
		self.__front = 0  	
		self.__rear = -1  		
		self.__count = 0  
	
	def __str__(self):
		out = ''
		if not self.isEmpty():
			i = self.__front
			for _ in range(self.__count):
				out += self.__q[i] + '->'
				i = (i + 1) % self.__capacity
		return out

	def dequeue(self):
		if self.isEmpty():
			print('Queue Underflow!! Terminating process.')
			exit(-1)
		x = self.__q[self.__front]
		print('Removing element…', x)
		self.__front = (self.__front + 1) % self.__capacity
		self.__count = self.__count - 1
		return x

	def enqueue(self, value):
		if self.isFull():
			print('Overflow!! Terminating process.')
			exit(-1)
		print('Inserting element…', value)
		self.__rear = (self.__rear + 1) % self.__capacity
		self.__q[self.__rear] = value
		self.__count = self.__count + 1

	def size(self):
		return self.__count

	def isEmpty(self):
		return self.size() == 0

	def isFull(self):
		return self.size() == self.__capacity

