"""
# pytest-tel ennyire egyszerű volt:

from utils import duplaz, is_palindrome


def test_duplaz():
    assert duplaz(2) == 4
    assert duplaz(3) == 6
    assert duplaz(0) == 0
    assert duplaz(-1) == -2
    assert duplaz(-5) == -10


def test_is_palindrome():
    assert is_palindrome("anna") == True
    assert is_palindrome("ana") == True
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
    #
    assert is_palindrome("abc") == False
    assert is_palindrome("ab") == False
    assert is_palindrome("Anna") == False
"""

import unittest

from utils import duplaz, is_palindrome

class TestUtils(unittest.TestCase):
    def test_duplaz(self):
        self.assertEqual(duplaz(2), 4)
        self.assertEqual(duplaz(3), 6)
        self.assertEqual(duplaz(0), 0)
        self.assertEqual(duplaz(-1), -2)
        self.assertEqual(duplaz(-5), -10)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("anna"))
        self.assertTrue(is_palindrome("ana"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))
        #
        self.assertFalse(is_palindrome("abc"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("Anna"))

##############################################################################

if __name__ == "__main__":
    unittest.main()
