class Employee:
	def __init__(self,ename,eid,esal):
		self.ename=ename
		self.eid=eid
		self.esal=esal
	def display(self):
		print(self.ename)
		print(self.eid)
		print(self.esal)
class test:
	def modify(emp):
		emp.esal=emp.esal+10000
		emp.display()
	
e=Employee("divyansh",201,45000)
test.modify(e)


		
		