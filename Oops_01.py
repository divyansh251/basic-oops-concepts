class student:
	student_count=0
	increae=2
	def __init__(self,name,percent,age):
		self.name=name
		self.per=percent
		self.age=age
		student.student_count+=1
	def increase(self):
		self.per=self.per*self.increae
		print(self.per)	
	@classmethod
	def strg(cls,word):
		name,per,age=word.split("-")
		return cls(name,per,age)
s1=student("divyansh",85,21)
s2=student("ritik",90,20)
s3=student("navneet",58,19)
s4=student.strg("kapil-85-23")
#print(s4.name)
#print(student.student_count)
s1.increase()
		