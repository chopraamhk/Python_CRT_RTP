"""Intoductory example

Using input and output.
"""

import sys
#provides information about constants, functions and methods of the Python interpreter.

def main():
    #defining main function
    #ask user for input
    name = input("What is your name?")
    #print output for user;
    print(f"Hello {name}!")
    return 0
###main function requires integer values and we are telling it to execute by returning 0 ###


if __name__ == "__main__":
    sys.exit(main())