import unittest
import duze

class testy_kalkulator(unittest.TestCase):
        def test_duze_litery(self):
            wynik = duze.duze_litery('ala ma kota')
            self.assertEqual(wynik, 'Ala ma kota')



if __name__ == '__main__':
    unittest.main()
