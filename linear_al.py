import numpy as np 

a = np.array([1,1,1])
b=np.array([2,1,0])

emp =[]


fl = b.flat 



for x in fl:
	emp.append(x)


print emp


dot = np.dot(a,b)

print dot 






