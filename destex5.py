#destex5.py
import time 
class Sample:
	def __init__(self):
		print("Object Initliztion---Constructor:")

	def __del__(self):
		print("Memory Space pointed by object removed--Garbage Collector")


#main program
lst=[ Sample(),Sample(),Sample() ]
print("we created 3 sample objects and placed in lst")
time.sleep(10)
del lst  
time.sleep(10)
print("end of application")
