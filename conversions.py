import sys

def convertCelsiusToKelvin(celsius):
    if isinstance(celsius, float):
        return(celsius + 273.15)
    else:
        raise(TypeError('Celsius must be a float.'))

def convertCelsiusToFahrenheit(celsius):
    if isinstance(celsius, float):
        return((1.8 * celsius) + 32)
    else:
        raise(TypeError('Celsius must be a float.'))
# TODO
def convertFahrenheitToCelsius(fahrenheit):
    if isinstance(fahrenheit, float):
        return((fahrenheit - 32) * 5/9)
    else:
        raise(TypeError('fahrenheit must be a float.'))

def convertFahrenheitToKelvin(fahrenheit):
    if isinstance(fahrenheit, float):
        return((fahrenheit + 459.67) * 5/9)
    else:
        raise(TypeError('fahrenheit must be a float.'))

def convertKelvinToCelsius(kelvin):
    if isinstance(kelvin, float):
        return(kelvin - 273.15)
    else:
        raise(TypeError('Kelvin must be a float.'))

def convertKelvinToFahrenheit(kelvin):
    if isinstance(kelvin, float):
        return((kelvin * 1.8) - 459.67)
    else:
        raise(TypeError('Kelvin must be a float.'))

def main():
    pass

if __name__ == '__main__':
     main()
