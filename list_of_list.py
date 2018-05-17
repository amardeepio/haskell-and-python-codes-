import numpy as np 

array = np.array(np.arange(20)).reshape(4,5)

array_to_list = array.tolist()

print array_to_list

product =[[y*2 for y in x] for x in array_to_list]

print product

# lets make all the elements float 

float_ =[[float(y) for y in x] for x in array_to_list]

print float_

# let apply function to the list by mapping it 

def square(x):
	return x*x 

array_1 = [x for x in range(1,20)]

print array_1

print map(square,array_1)

# lets do it by another way 

pro = map(lambda x: x*x , array_1)

print pro 
