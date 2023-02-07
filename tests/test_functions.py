from convert import result, code_validity, num_validity, RatesNotAvailableError
from unittest import TestCase

class ConverterTestCase(TestCase):
    def test_valid_number(self):
        """ Function determines correctly if input value is valid number """
        self.assertTrue(num_validity('2'))
        self.assertTrue(num_validity('2.0'))
        self.assertTrue(num_validity(2))
        self.assertTrue(num_validity(2.0))
        self.assertFalse(num_validity('two'))
        self.assertFalse(num_validity('0'))
        self.assertFalse(num_validity(0))
        self.assertFalse(num_validity('-2'))
        self.assertFalse(num_validity(-2))

    def test_valid_curr_code(self):
        """ Function determines correctly if currency code is a valid code """
        self.assertTrue(code_validity('USD'))
        self.assertTrue(code_validity('eur'))
        self.assertTrue(code_validity('Mnn'))
        self.assertTrue(code_validity('GBP'))
        self.assertFalse(code_validity('avv'))
        self.assertFalse(code_validity('MEX'))
        self.assertFalse(code_validity('a'))
        self.assertFalse(code_validity('aaaaaaa'))
        self.assertFalse(code_validity('1333'))
        self.assertFalse(code_validity(3333))

    def test_converter(self):
        """ Function returns correct string and handles input values appropriately"""        
        self.assertEqual(result('USD', 'USD', '20'), 'US$20.00')
        self.assertRaises(RatesNotAvailableError, result, 'AAA', 'USD', '20')        
        self.assertEqual(result('USD', 'USD', 20), 'US$20.00')        
        self.assertIn('1.00', result('GBP', 'GBP', '1'))
        self.assertIn('5.10', result('GBP', 'gbp', '5.10'))
        self.assertIsInstance(result('USD', 'USD', '20'), str)