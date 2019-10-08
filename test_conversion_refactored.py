import unittest
import conversions_refactored

class TestConversionsRefactored(unittest.TestCase):

    def test_all_good_temp_values(self):
        print(TestConversionsRefactored.test_all_good_temp_values.__name__)
        print("C to F")
        result = conversions_refactored.convert('celsius', 'fahrenheit', 0.0)
        self.assertEqual(result, 32)
        print("C to K")
        result = conversions_refactored.convert('celsius', 'kelvin', 0.0)
        self.assertEqual(result, 273.15)
        print("F to K")
        result = conversions_refactored.convert('fahrenheit', 'kelvin', 0.0)
        self.assertEqual(result, 255.3722222222222)
        print("F to C")
        result = conversions_refactored.convert('fahrenheit', 'celsius', 0.0)
        self.assertEqual(result, -17.77777777777778 )
        print("K to F")
        result = conversions_refactored.convert('kelvin', 'fahrenheit', 0.0)
        self.assertEqual(result, -459.67 )
        print("K to C")
        result = conversions_refactored.convert('kelvin', 'celsius', 0.0)
        self.assertEqual(result, -273.15 )
        print("\n")

    def test_all_good_distance_values(self):
        print(TestConversionsRefactored.test_all_good_distance_values.__name__)
        print("Meter to Mile")
        result = conversions_refactored.convert('meters', 'miles', 1.0)
        self.assertEqual(result, 0.0006213711922373339)
        print("Meter to Yards")
        result = conversions_refactored.convert('meters', 'yards', 1.0)
        self.assertEqual(result, 1.094)
        print("Mile to Meter")
        result = conversions_refactored.convert('miles', 'meters', 1.0)
        self.assertEqual(result, 1609.344)
        print("Mile to Yards")
        result = conversions_refactored.convert('miles', 'yards', 1.0)
        self.assertEqual(result, 1760)
        print("Yards to Miles")
        result = conversions_refactored.convert('yards', 'miles', 1.0)
        self.assertEqual(result, 0.0005681818181818182)
        print("Yards to Meters")
        result = conversions_refactored.convert('yards', 'meters', 1.0)
        self.assertEqual(result, 0.9140767824497257)

    def test_am_i_me(self):
        print(TestConversionsRefactored.test_am_i_me.__name__)
        for i in ['yards', 'meters', 'miles', 'fahrenheit', 'kelvin', 'celsius']:
            print(f"Testing is {i} converted to itself is the same value")
            result = conversions_refactored.convert(i, i, 1.0)
            self.assertEqual(result, 1)

    def test_exceptions(self):
        print(TestConversionsRefactored.test_exceptions.__name__)
        print("Exception Tests: Raise typeError if int")
        with self.assertRaises(TypeError) as context:
            conversions_refactored.convert('celsius', 'fahrenheit', 300)
        print("Exception Tests: Raise typeError if str")
        with self.assertRaises(TypeError) as context:
            conversions_refactored.convert('celsius', 'fahrenheit', 'a')
        print("Exception Tests: wrong conversion")
        with self.assertRaises(conversions_refactored.ConversionNotPossible) as context:
            conversions_refactored.convert('celsius', 'miles', 1.0)
        print("\n")


if __name__ == '__main__':
    unittest.main()
