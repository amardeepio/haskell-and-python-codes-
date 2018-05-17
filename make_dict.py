def make_dict(key_list):
	dic ={}

	for keys,value in key_list:

		dic[keys]= value

	return dic
tu =(1,2,3,4)

print(make_dict([("Joe", 1), ("Scott", 2), ("John", 4)]))