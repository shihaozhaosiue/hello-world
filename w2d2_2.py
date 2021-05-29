# ~ shihao zhao--W2D2_assignment
from numpy import *
def computepay(a,b):
	if a<40:
		c=a*b
	else:
		c=40*b+1.5*b*(a-40)
	return c		
hour = int(input("please enter the number of hours:"))
rate = int(input("please enter the rate per hour:"))
pay=computepay(hour,rate)
print('gross pay:'+str(pay))
