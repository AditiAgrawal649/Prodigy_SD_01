def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == "celsius" or unit.lower() == "c":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"\n{value}° Celsius is equal to:")
        print(f"{f:.2f}° Fahrenheit")
        print(f"{k:.2f} Kelvin")
    elif unit.lower() == "fahrenheit" or unit.lower() == "f":
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"\n{value}° Fahrenheit is equal to:")
        print(f"{c:.2f}° Celsius")
        print(f"{k:.2f} Kelvin")
    elif unit.lower() == "kelvin" or unit.lower() == "k":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"\n{value} Kelvin is equal to:")
        print(f"{c:.2f}° Celsius")
        print(f"{f:.2f}° Fahrenheit")
    else:
        print("Invalid unit. Please choose from Celsius, Fahrenheit, or Kelvin.")

# Main Program
print("Temperature Converter: Celsius ↔ Fahrenheit ↔ Kelvin")
try:
    temp_value = float(input("Enter the temperature value: "))
    temp_unit = input("Enter the unit of temperature (Celsius/Fahrenheit/Kelvin): ")
    convert_temperature(temp_value, temp_unit)
except ValueError:
    print("Invalid input. Please enter a numeric temperature value.")
