import random

def make_cipher_dict(alphabet):
    """
    Given a string of unique characters, compute a random 
    cipher dictionary for these characters
    """
    dic={}
    sh=[x for x in alphabet]
    random.shuffle(sh)
    for i in range(len(alphabet)):
        dic[alphabet[i]]=sh[i]
    return dic

print(make_cipher_dict("helloworld"))
print(make_cipher_dict("opensource"))
