def is_palindromes(string):
    string = string.strip()
    string = string.lower()

    check_letters = int(len(string) / 2)
    
    if len(string) % 2 == 0:
        if string[:check_letters] == string[:check_letters -1:-1]:
            return True
        else:
            return False
    else:
        if string[:check_letters] == string[:check_letters:-1]:
            return True
        else:
            return False

#================================================================

strings = ['kajak', 'potop', ' kość', 'kartka', ' zaraz ', 'mars', 'Anna']

for str_ in strings:
    print('-' *16)
    print(f"{str_:<8}|", is_palindromes(str_))
