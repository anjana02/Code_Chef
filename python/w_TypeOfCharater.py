# To check whether a character is uppercase, lowercase ,digit or special character.

# Each keyboard character has been assigned a code by which they can be identified and that is called ASCII code, 128 values in total.

# Alphabets - Uppercase( between 65 to 90 ) Alphabets - Lowercase( between 97 to 122) Digits (between 48 to 57) Special Characters (all the remaining in between 0 to 127)


def type_of_character(character):
    if 65 <= ord(character) <= 90:
        return "Uppercase"
    elif 97 <= ord(character) <= 122:
        return "Lowercase"
    elif 48 <= ord(character) <= 57:
        return "Digit"
    else:
        return "Special Character"


print(type_of_character("A"))
