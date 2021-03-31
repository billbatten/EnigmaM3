import unittest
import PractiseEnigma

class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        #encryption = PractiseEnigma.encrypt("abd", "123", "AAA", "AS BD CZ UI")
        self.assertEqual(PractiseEnigma.encrypt("ab d", "123", "AAA", "AS BD CZ UI"), "JSL")
        #self.assertEqual(encryption, "JSL")


if __name__ == '__main__':
    unittest.main()
