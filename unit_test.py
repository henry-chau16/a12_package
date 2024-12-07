import unittest
import pandas as pd
from stats_function import *
from validate_functions import *

class test_functions(unittest.TestCase):

    def test_valid_gender(self):
        df = pd.read_csv('crime.csv')
        self.assertEqual(validate_gender(23), False)
        self.assertEqual(validate_gender(df['Vict Sex'][3]), True)

    def test_valid_age(self):
        df = pd.read_csv('crime.csv')
        self.assertEqual(validate_age('16'), False)
        self.assertEqual(validate_age(df['Vict Age'][5]), True)

    def test_stats(self):
        df = pd.read_csv('crime.csv')
        self.assertEqual(column_mean(df['Vict Age']), 30.069437120368743)
        self.assertEqual(column_median(df['Vict Age']), 31.0)
        self.assertEqual(column_mean(pd.Series(['A', 'B', 'C'])), False)

if __name__ == '__main__':
    unittest.main()