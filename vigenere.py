from helpers import alphabet_position, rotate_character
import string 


def encrypt(text,rot):
    myString = ""
    alphabet = string.ascii_letters
    rot_p = -1
    for x in range(len(text)):
        if text[x] in alphabet:
            rot_p+=1
        else:
            rot_p +=0
        new_rot = alphabet_position(rot[rot_p%len(rot)])
        new_letter = rotate_character(text[x],new_rot)
        myString+=new_letter
    return myString 

def main():
    from sys import argv
    text = input("Give me a string that you'd like me to encrypt: ")
    rot = argv[1]
    print(encrypt(text,rot))


if __name__ == '__main__':
    main()

#print(encrypt('The crow flies at midnight!','boom'))
#test driven development. Use unit test. 
#is .alpha()

