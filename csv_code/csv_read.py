import csv 

def parse(csvname):

	table =[]

	with open(csvname,"r") as csvfile:
		for line in csvfile:
			line = line.rstrip()

			columns = line.split(',')

			table.append(columns)

	return table


def print_table(table):
   
    for row in table:
   
        print("{:<19}".format(row[0]), end='')
      
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')


table = parse("hightemp.csv")

print(print_table(table))