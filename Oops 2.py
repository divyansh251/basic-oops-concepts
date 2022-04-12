class test:
	cname="bansal"
	def __init__(self,name,age):
		self.sname=name
		self.age=age
	@classmethod
	def m1(cls):
		cls.per=50
		test.fname='d'
	@staticmethod
	def m2():
		test.lname=100
	def m3(self):
		test.sec='b'
		
s1=test("divyansh",21)
print(test.m1())
print(test.m2())
print(s1.m3())
print(test.__dict__)

		