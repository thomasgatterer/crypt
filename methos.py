"""
search reference https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

https://www.w3schools.com/python/ref_string_maketrans.asp
https://www.w3schools.com/python/ref_string_translate.asp
https://www.askpython.com/python/examples/when-to-use-colon-python
https://www.w3schools.com/python/ref_list_index.asp

https://pythontutor.com/render.html#mode=display
 """
import string

letter = "D"
key = "D"
alphabet = string.ascii_uppercase

##shiftNumber = 3
##print(alphabet[shiftNumber:])
##print(alphabet[:shiftNumber])

##print(alphabet.index("D"))

##print(alphabet[alphabet.index(shift):])


def caesarCryptLetter(letter, key):
    shifted_alphabet = alphabet[alphabet.index(key):] + alphabet[:alphabet.index(key)]
    table = str.maketrans(alphabet, shifted_alphabet)
    return letter.translate(table)


def caesarDecryptLetter(letter, key):
    shifted_alphabet = alphabet[alphabet.index(key):] + alphabet[:alphabet.index(key)]
    table = str.maketrans(shifted_alphabet, alphabet)
    return letter.translate(table)


"""     HowTo: python3 methos.py  """

######### Test Code ############


print(caesarCryptLetter('A', 'D'))
print(caesarCryptLetter('U','X'))
print(caesarDecryptLetter('D','A'))
print(caesarDecryptLetter('X','U'))

def test_starting_out_tg():
    assert 1==1
 #   assert deleteSpaces('Trafen sich Caesar und Cicero') == 'TrafensichCaesarundCicero'
 #   assert inCapitals('CaesarrauchteeineCigaretteundCiceroeineCigarre') == 'CAESARRAUCHTEEINECIGARETTEUNDCICEROEINECIGARRE'
    assert caesarCryptLetter('A', 'D') == 'D'
    assert caesarCryptLetter('U','X') == 'R'
    assert caesarDecryptLetter('D','A') == 'D'
    assert caesarDecryptLetter('X','U') == 'D'

    """ HowTo: Ausführen mit pytest Dateiname.py """

    """ Quellen:
    https://stackoverflow.com/questions/3371255/writing-unit-tests-in-python-how-do-i-start
    https://docs.pytest.org/en/7.1.x/getting-started.html
    """
    """ Lizenz CC BY 4.0 TG https://creativecommons.org/licenses/by/4.0/legalcode.de """