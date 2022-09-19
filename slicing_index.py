"""Print by slicing the fourth to eighth member in the list of ten"""

import sys

def main():
    List = [1,4,3,5,6,7,8,7,2,9]

    print('List:', List)
    print('List', List[4:8])

    return 0

if __name__ == "__main__":
    sys.exit=main()