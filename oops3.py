import sys
class customer:
	bankname="Axis Bank"
	def __init__(self,name,balance=0):
		self.name=name
		self.cbalance=balance
		
	def deposit(self,amt):
		self.cbalance=(self.cbalance)+(amt)
		print("current amount-->",self.cbalance)
	def withdraw(self,amt):
		if(amt<self.cbalance):
			self.cbalance=self.cbalance-(amt)
			print("current amount-->",self.cbalance)
		else:
			print("incifficent balance")
			sys.exit()
print("Welcome to ",customer.bankname)
name=input("enter your name-->")
c=customer(name)
while True:
	print('d-->deposit\nw-->withdraw\ne-->exit')
	option=input('make your choice-->')
	if option=='d' or option=='D':
		amt=int(input('enter amount-->'))
		c.deposit(amt)
	elif(option=='w' or option=='W'):
		amt=int(input("enter amount-->"))
		c.withdraw(amt)
	elif(option=='E' or option=='e'):
		print("thank for banking")
		sys.exit()
	else:
		print("please enter valid option")
		

		