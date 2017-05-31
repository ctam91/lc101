from helpers import alphabet_position, rotate_character

import string 

def encrypt(text,rot):
    new_str = ""
    for letter in text:
        new_char = rotate_character(letter,rot)
        new_str += new_char
    return new_str 

def main():
    from sys import argv, exit
    #print("This is what the user typed on the command line:", argv,argv[1])
    if argv[1].isdigit():
        text = input("Give me a string that you'd like me to encrypt: ")
        rot = int(argv[1])
        print(encrypt(text,rot))
    else: 
        print("usage: python caesar.py n")
        exit()
        main()


if __name__ == '__main__':
    main()
