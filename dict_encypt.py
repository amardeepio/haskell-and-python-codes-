alpha = 'abcdefghijklmnopqrstuvwxyz'

to_list = [x for x in alpha]

rev = to_list[::-1]

dict_1 = {}


for i in range (len(to_list)):

	dict_1[to_list[i]] = rev[i]


print dict_1


def encrypt(dict_1,text):
	encrypt=""
	for texts in text:

		encrypt += dict_1[texts]

	return encrypt

name ="amardeep"


enc = encrypt(dict_1,name)

print enc










