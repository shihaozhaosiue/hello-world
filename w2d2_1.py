# ~ shiao zhao--W2D2_assignment
from numpy import *
hour = int(input("please enter the number of hours:"))
rate = int(input("please enter the rate per hour:"))

if hour<40.0:
	pay = hour*rate
	print('gross pay:'+str(pay))
else:
	ex = hour-40.0
	pay = 40.0*rate+1.5*rate*	ex
	print('gross pay:'+str(pay))
	
