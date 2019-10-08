import unittest
import conversions

class TestConversions(unittest.TestCase):
    #1
    def test_C2K_good_values(self):
        print(TestConversions.test_C2K_good_values.__name__)
        print("Good Tests: 300.00 to 573.15")
        result = conversions.convertCelsiusToKelvin(300.00)
        self.assertEqual(result, 573.15)
        print("Good Tests: -78.0 to 195.14999999999998")
        result = conversions.convertCelsiusToKelvin(0.0)
        print("Good Tests: 0.0 to 273.15")
        self.assertEqual(result, 273.15)
    def test_C2K_exceptions(self):
        print(TestConversions.test_C2K_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions.convertCelsiusToKelvin(300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions.convertCelsiusToKelvin('a')
        print("\n")

    #2
    def test_C2F_good_values(self):
        print(TestConversions.test_C2F_good_values.__name__)
        print("Good Tests: 0.0 to 32.0")
        result = conversions.convertCelsiusToFahrenheit(0.0)
        self.assertEqual(result, 32.0)

        print("Good Tests: -10.0 to 14.0")
        result = conversions.convertCelsiusToFahrenheit(-10.0)
        self.assertEqual(result, 14.0)

        print("Good Tests: 300.0 to 572")
        result = conversions.convertCelsiusToFahrenheit(300.0)
        self.assertEqual(result, 572.0)
    def test_C2F_exceptions(self):
        print(TestConversions.test_C2F_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions.convertCelsiusToFahrenheit(300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions.convertCelsiusToFahrenheit('a')
        print("\n")

    #3
    def test_F2C_good_values(self):
        print(TestConversions.test_F2C_good_values.__name__)
        print("Good Tests: 0.0 to -17.77777777777778")
        result = conversions.convertFahrenheitToCelsius(0.0)
        self.assertEqual(result, -17.77777777777778)
        print("Good Tests: 300.0 to 572")
        result = conversions.convertFahrenheitToCelsius(300.0)
        self.assertEqual(result, 148.88888888888889)
        print("Good Tests: -10.0 to -23.333333333333332")
        result = conversions.convertFahrenheitToCelsius(-10.0)
        self.assertEqual(result, -23.333333333333332)
    def test_F2C_exceptions(self):
        print(TestConversions.test_F2C_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions.convertFahrenheitToCelsius(300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions.convertFahrenheitToCelsius('a')
        print("\n")

    #4
    def test_F2K_good_values(self):
        print(TestConversions.test_F2K_good_values.__name__)
        print('Good Tests: 0.0 to 255.3722222222222')
        result = conversions.convertFahrenheitToKelvin(0.0)
        self.assertEqual(result, 255.3722222222222)
        print('Good Tests: -10.0 to 249.81666666666666')
        result = conversions.convertFahrenheitToKelvin(-10.0)
        self.assertEqual(result, 249.81666666666666)
        print('Good Tests: 300.0 to 422.03888888888895')
        result = conversions.convertFahrenheitToKelvin(300.0)
        self.assertEqual(result, 422.03888888888895)
    def test_F2K_exceptions(self):
        print(TestConversions.test_F2C_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions.convertFahrenheitToKelvin(300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions.convertFahrenheitToKelvin('a')
        print("\n")
    #5
    def test_K2F_good_values(self):
        print(TestConversions.test_K2F_good_values.__name__)
        print('Good Tests: 0.0 to -459.67')
        result = conversions.convertKelvinToFahrenheit(0.0)
        self.assertEqual(result, -459.67)
        print('Good Tests: -10.0 to -477.67')
        result = conversions.convertKelvinToFahrenheit(-10.0)
        self.assertEqual(result, -477.67)
        print('Good Tests: 300.0 to 80.32999999999998')
        result = conversions.convertKelvinToFahrenheit(300.0)
        self.assertEqual(result, 80.32999999999998)
    def test_K2F_exceptions(self):
        print(TestConversions.test_K2F_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions.convertKelvinToFahrenheit(300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions.convertKelvinToFahrenheit('a')
        print("\n")
    #6
    def test_K2C_good_values(self):
        print(TestConversions.test_K2C_good_values.__name__)
        print('Good Tests: 0.0 to -273.15')
        result = conversions.convertKelvinToCelsius(0.0)
        self.assertEqual(result, -273.15)
        print('Good Tests: -10.0 to -283.15')
        result = conversions.convertKelvinToCelsius(-10.0)
        self.assertEqual(result, -283.15)
        print('Good Tests: 300.0 to 26.850000000000023')
        result = conversions.convertKelvinToCelsius(300.0)
        self.assertEqual(result, 26.850000000000023)
    def test_K2C_exceptions(self):
        print(TestConversions.test_K2C_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions.convertKelvinToCelsius(300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions.convertKelvinToCelsius('a')
        print("\n")

if __name__ == '__main__':
    unittest.main()
