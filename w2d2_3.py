# ~ shihao zhao--w2d2_assignment
from matplotlib.pyplot import *
from numpy import *

t=arange(0,1,0.01)
y=2*sin(2*pi*t)

# ~ solution1
N = len(y)
y1 = zeros(N)
for i in range(N):
	y_i=y[i]
	if -0.5<y_i<0.5:
		y1[i]=0
	elif y_i>0.5:
		y1[i]=y_i-0.5
	elif y_i<-0.5:
		y1[i]=y_i+0.5
        
figure (1)
clf()
plot(t,y,'r--')
plot(t, y1, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

# ~ solution2
y2 = zeros(N)
for i,y_i in enumerate(y):
	if -0.5<y_i<0.5:
		y2[i]=0
	elif y_i>0.5:
		y2[i]=y_i-0.5
	elif y_i<-0.5:
		y2[i]=y_i+0.5
figure (2)
clf()
plot(t,y,'r--')
plot(t, y2, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

# ~ solution3
# ~ T = arange(0,1,0.01)
a=[1 if s<0.5 else 0 for s in t]
b=[1 if s>0.5 else 0 for s in t]
ya=(y-0.5)*a
yb=(y+0.5)*b
import copy
y3_a=copy.copy(ya)
y3_b=copy.copy(yb)
figure(3)
clf()
plot(t,y,'r--')
y3_a[y3_a<0]=0
y3_b[y3_b>0]=0
y3=y3_a+y3_b
plot(t, y3, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

# ~ solution4
import copy
y4_a=copy.copy(ya)
y4_b=copy.copy(yb)
figure(4)
clf()
plot(t,y,'r--')
inds1=where(ya<0)[0]
y4_a[inds1]=0
inds2=where(yb>0)[0]
y4_b[inds2]=0
y4=y4_a+y4_b
plot(t, y4, label='$y(t)$',linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()
