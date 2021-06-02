#destex6.py
import time 
class Sample:
	def __init__(self):
		print("Object Initliztion---Constructor:")

	def __del__(self):
		print("Memory Space pointed by object removed--Garbage Collector")


#main program
s1=Sample()
s2=Sample()
s3=Sample() 
print("we created 3 sample objects and placed in lst")
time.sleep(10)
print("object s1--memory space")
del s1    # gc is calling __del__(self)
time.sleep(10)
print("object s2--memory space")
del s2   # gc is calling __del__(self)
time.sleep(10)
print("object s3--memory space")
del s3   # gc is calling __del__(self)
time.sleep(10)
print("end of application")
