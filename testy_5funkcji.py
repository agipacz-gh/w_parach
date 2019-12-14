import unittest
import duze

class testy_5funkcji(unittest.TestCase):
        def test_duze_litery(self):
            wynik = duze.duze_litery('ala ma kota')
            self.assertEqual(wynik, 'Ala ma kota')

            print(wynik)

        def test_split(self):
            wynik = duze.split_litery('ala ma kota')
            self.assertEqual(wynik, ['Ala', 'ma', 'kota')

            print(wynik)

if __name__ == '__main__':
    unittest.main()
