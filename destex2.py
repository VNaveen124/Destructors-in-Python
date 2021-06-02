#destex2.py
import time 
class Sample:
	def __init__(self):
		print("Object Initliztion---Constructor:")

	def __del__(self):
		print("Memory Space pointed by object removed--Garbage Collector")


#main program
s1=Sample()
print("object created and initlized");
time.sleep(10)
print("End of application")
