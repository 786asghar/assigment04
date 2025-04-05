"""
Program: 02_agreement
--------------------"""


def main():
    print("This program Favorite Animal .")
    ani1 : str = input("What's your favorite animal? : ")
    print("My favorite animal is also " + str(ani1) + "!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()