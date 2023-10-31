## search reference https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

## https://www.w3schools.com/python/ref_string_maketrans.asp
## https://www.w3schools.com/python/ref_string_translate.asp
## https://www.askpython.com/python/examples/when-to-use-colon-python
## https://www.w3schools.com/python/ref_list_index.asp


## https://pythontutor.com/render.html#mode=display


import string

plaintext = "ABCD"
shift = "D"
alphabet = string.ascii_lowercase+string.ascii_uppercase

##shiftNumber = 3
##print(alphabet[shiftNumber:])
##print(alphabet[:shiftNumber])

##print(alphabet.index("D"))


shifted_alphabet = alphabet[alphabet.index(shift):] + alphabet[:alphabet.index(shift)]
table = str.maketrans(alphabet, shifted_alphabet)
print(plaintext.translate(table))
