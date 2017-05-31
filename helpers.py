import string 

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    letter = letter.lower()
    position = 0
    for character in range(len(alphabet)):
        if alphabet[character] == letter:
            position = character 
    return position


def rotate_character(char,rot):
    position = (alphabet_position(char)+rot)%26
    alphabet_lowercase = string.ascii_lowercase
    alphabet_uppercase = string.ascii_uppercase
    if char in alphabet_lowercase:
        for index in range(len(alphabet_lowercase)):
            if position == index:
                new_letter = alphabet_lowercase[index]
        return new_letter
    elif char in alphabet_uppercase:
        for index in range(len(alphabet_uppercase)):
            if position == index:
                new_letter = alphabet_uppercase[index]
        return new_letter
    else: 
        return char 
