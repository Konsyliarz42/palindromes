import re

def is_palindromes(string):
    string = string.lower()
    string = ''.join(char for char in string if char not in '.,;:!?-     ')

    check_letters = int(len(string) / 2)
    
    if string[:check_letters] == string[:-check_letters-1:-1]:
        return True
    else:
        return False

#================================================================

strings = { 'kajak': True, 
            'potop': True,
            ' kość': False,
            'kartka': False,
            ' zaraz ': True,
            'mars': False,
            'Anna': True,
            'Może jutro ta dama sama da tortu jeżom.': True }

for str_ in strings:
    if strings[str_] != is_palindromes(str_):
        print("Bad:", str_)
        break
    else:
        print("Good:", str_)
