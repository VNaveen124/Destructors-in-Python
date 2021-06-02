#destex7.py
import time,sys 
class Sample:
	def __init__(self):
		print("Object Initliztion---Constructor:")

	def __del__(self):
		print("Memory Space pointed by object removed--Garbage Collector")


#main program
s1=Sample()
s2=s1
s3=s2
print("Refs of s1=", sys.getrefcount(s1)) #4
print("end of application")
