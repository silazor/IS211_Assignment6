import sys

class ConversionNotPossible(Exception):
    def __init__(self):
        Exception.__init__(self, "Incompatible conversion requested")

def convert(fromUnit, toUnit, value):
    #[K] = [°C] + 273.15
    valid_temp = ['celsius', 'fahrenheit', 'kelvin']
    valid_distance = ['miles', 'yards', 'meters']

    # Raise if not a valid fromUnit
    if fromUnit not in valid_temp and fromUnit not in valid_distance:
        raise(AssertionError(f"From unit {fromUnit} not a valid Unit."))

    # Raise if not a valid toUnit
    if toUnit not in valid_temp and toUnit not in valid_distance:
        raise(AssertionError(f"To unit {toUnit} not a valid Unit."))

    # Raise is not a float
    if not isinstance(value, float):
        raise(TypeError('Celsius must be a float.'))

    #Return value if converting to same Unit
    if fromUnit == toUnit:
        return(value)

    # Conversion work
    if fromUnit in valid_temp and toUnit in valid_temp:
        if fromUnit == 'celsius':
            if toUnit == 'kelvin':
                return(value + 273.15)
            if toUnit == 'fahrenheit':
                return((1.8 * value) + 32)
        elif  fromUnit == 'kelvin':
            if toUnit == 'celsius':
                return(value - 273.15)
            if toUnit == 'fahrenheit':
                return((value * 1.8) - 459.67)
        elif fromUnit == 'fahrenheit':
            if toUnit == 'celsius':
                return((value - 32) * 5/9)
            if toUnit == 'kelvin':
                return((value + 459.67) * 5/9)
        else:
            raise(Exception('idk how we got here'))

    if fromUnit in valid_distance and toUnit in valid_distance:
        if fromUnit == 'meters':
            if toUnit == 'miles':
                return(value / 1609.344)
            if toUnit == 'yards':
                return(value * 1.094)
        if fromUnit == 'miles':
            if toUnit == 'meters':
                return(value * 1609.344)
            if  toUnit == 'yards':
                return(value * 1760)
        if fromUnit == 'yards':
            if toUnit == 'miles':
                return(value /1760)
            if toUnit == 'meters':
                return(value / 1.094)

    if (fromUnit in valid_temp and toUnit in valid_distance or
        fromUnit in valid_distance and toUnit in valid_temp):
        raise(ConversionNotPossible)

def main():
    print('main')
if __name__ == '__main__':
     main()
