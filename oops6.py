class outer:
	def __init__(self):
		print("outer object is created")
	class inner:
		def __init__(self):
			print("inner object created")
		def m1(self):
			print("inner class method")
o=outer()
i=o.inner()
i.m1()		
		