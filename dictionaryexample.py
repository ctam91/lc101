import string

def textDictionary(text):
    myDictionary = {}
    alphabet = string.ascii_letters
    for x in range(len(text)):
        if text[x] in alphabet:
            myDictionary[x] = alphabet.find(text[x])
    return myDictionary

print(textDictionary("apple"))