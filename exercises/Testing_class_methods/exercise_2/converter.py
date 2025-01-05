class UnitConverter:
    """A class to convert between different measurement units."""
    def convert_celcius_to_fahrenheit(self, value):
        f = (value * 9/5) + 32
        return f
    def convert_celsius_to_kelvin(self, value):
        k = value + 273.15
        return k
    def convert_kelvin_to_celsius(self, value):
        c = value - 273.15
        return c

    def convert_fahrenheit_to_kelvin(self, value):
        k = (value - 32) * (9/5) + 32
        return k

    def convert_kelvin_to_fahrenheit(self, value):
        f = (value - 273.15) * (9/5) + 32
        return f

result = UnitConverter()
print(result.convert_kelvin_to_celsius(10))

