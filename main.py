import unittest
import re

def is_palindrome(string):
    string = string.lower()
    #string = ''.join(char for char in string if char not in '.,;:!?-     ')

    regular = r"[   .,:;!?/-]"
    string = re.sub(regular, '', string)

    check_letters = int(len(string) / 2)
    
    return string[:check_letters] == string[:-check_letters-1:-1]

#================================================================
class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('kajak'), True)

    def test_is_not_palindrome(self):
        self.assertEqual(is_palindrome('kartka'), False)

    def test_is_palindrome_with_capital_letter(self):
        self.assertEqual(is_palindrome('Anna'), True)

    def test_is_not_palindrome_with_capital_letter(self):
        self.assertEqual(is_palindrome('Mars'), False)

    def test_is_palindrome_with_spaces(self):
        self.assertEqual(is_palindrome(" zaraz "), True)

    def test_is_not_palindrome_with_spaces(self):
        self.assertEqual(is_palindrome("gra "), False)

    def test_is_palindrome_with_special_chars(self):
        self.assertEqual(is_palindrome(":potop"), True)

    def test_is_not_palindrome_with_special_chars(self):
        self.assertEqual(is_palindrome(".,gd-f/!"), False)

    def test_is_palindrome_with_multiple_strings(self):
        self.assertEqual(is_palindrome("Może jutro ta dama sama da tortu jeżom"), True)

    def test_is_not_palindrome_with_multiple_strings(self):
        self.assertEqual(is_palindrome("abc def coc ghi jkl"), False)

if __name__ == "__main__":
    unittest.main()
