"""
Program: 03_fahrenheit_to_celsius
--------------------
Another python program to get some practice with
variables.  This program asks the user for one
integers and prints their Temperature in Fahrenheit.
"""


def main():
    print("This program Temperature in Fahrenheit:.")
    num1 : str = input("Enter temperature in Fahrenheit:  ")
    num1 : int = int(num1)
    degrees_celsius = num1 * 5.0/9.0
    print("Temperature: " + (num1) + "=" + str(degrees_celsius) )


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()