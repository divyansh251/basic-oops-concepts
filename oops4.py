class animal:
	leg=4
	@staticmethod
	def sum(x,y):
		sum=x+y
		print(sum)
	@staticmethod
	def mul(x,y):
		mul=x*y
		print(mul)
	@classmethod
	def walk(cls,name):
		print(f"{name} has {animal.leg} leg")
	@classmethod
	def evenodd(cls,num):
		if num%2==0:
			print(f"{num} is even number")
		else:
			print("f{num} is odd number")
		
t1=animal()
t1.sum(10,30)
animal.mul(10,50)
t1.walk("dog")
animal.evenodd(10)