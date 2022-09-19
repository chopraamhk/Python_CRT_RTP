"""Create a list of ten unique numbers and print out the following
- the smallest number
- the largest number
- the index of the smallest number
- the index of the largest number"""

import sys

def main():
    List = [1,2,3,4,5,6,7,8,9,2]
    s= min(List)
    s_index = List.index(s)
    print("smallest number is, "{s}!")
    print(index of smallest number is, "{s_index}!")
    l= max(List)
    print(largest number is, {l})
    l_index = List.index(l)
    print(index of largest number is, "{l_index}!")
    return 0

if __name__ == "__main__":
    sys.exit=main()
