import csv as cs2 


def parse(csvfilename):

	table =[]

	with open(csvfilename,"r") as csvfile:
		csvreader = cs2.reader(csvfile, skipinitialspace=True)


		for row in csvreader:
			table.append(row)

		return table 



def print_table(table):

	for row in table :


		print ("{:<19}".format(row[0]), end='')


		for col in row [1:]:

			print ("{:>4}".format(col), end='')

		print  ("",end='\n')

table =parse("hightemp2.csv")
print_table(table)