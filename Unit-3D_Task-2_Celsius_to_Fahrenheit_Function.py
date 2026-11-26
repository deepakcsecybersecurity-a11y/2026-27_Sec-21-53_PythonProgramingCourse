def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature in Celsius: "))

f = convert(c)

print("Temperature in Fahrenheit:", f)