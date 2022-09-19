"""defining containers and matrices : Python does not have a matrices function and hence, we use list inside the list to turn in into matrices"""

import sys

def main():
    a11 = int(input("a11: "))
    a12 = int(input("a12: "))
    a21 = int(input("a21: "))
    a22 = int(input("a22: "))

A = [
    [a11, a12],
    [a21, a22]
]
print(f"A = {A}!")
  ##print the matrix
      print(f"a11 = {A[0][0]}")
      print(f"a22 = {A[1][1]}")
      return 0

if __name__ == "__main__":
      sys.exit=main()