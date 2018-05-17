grade_table = {
	
				
	'Joe':[100,98,100,13],

	'Scott':[75,59,89,77],

	'John': [86,84,91,78]
}
print grade_table['Joe']


def make_dic(name_list,grade_list):
	emp = {}

	for key in name_list:
		for values in grade_list:

			emp[key] = values



	return emp


name_list = ["Joe", "Scott", "John"]
grades_list = [100, 98, 100, 13], [75, 59, 89, 77],[86, 84, 91, 78] 
print(make_dic(name_list, grades_list))