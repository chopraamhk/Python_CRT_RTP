"""appending 1 number of your choice at your own index"""

import sys

def main():
    print("Write three different numbers")

    A = int(input("A:  "))
    B = int(input("B:  "))
    C = int(input("C:  "))

    X = [A, B, C]
    # create a list of prime numbers
    #prime_numbers = [2, 3, 5, 7]
    X.insert(2,11)
    # insert 11 at index 4
    #prime_numbers.insert(4, 11)

    print('List:', X)
    return 0

if __name__ == "__main__":
    sys.exit=main()
