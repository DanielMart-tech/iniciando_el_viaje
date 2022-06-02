# This is a program that takes a number as an input and converts it from Fahrenheit to Celsius
'''The mathematical equation to calculate from Fahrenheit to Celsius grades: (Fahrenheit) - 32 * 5 / 9'''
fahrenheit = input("Please, introduce a number to convert it to Celsius: ")
celsius = (int(fahrenheit) - 32) * 5 / 9
print(f"{fahrenheit} ºFahrenheit to Celsius is: {celsius}ºC")