"""replacing and deleting numbers in the list"""

import sys

def main():
    List = [1,4,3,5,6,7,8,7,2,9]

    print('List:', List)

    t = [2,5,6,8]

    List[4:8] = t
    print(List)

    del List[4:8]
    print(List)
    return 0

if __name__ == "__main__":
    sys.exit=main()