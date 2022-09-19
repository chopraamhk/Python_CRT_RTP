"""Strings and functions"""

import sys

def main():

      print("Hello" + " " + "world")  #concatenate
      print("*" * 20)   #this will print * for 20 times
      print(f"Hello {'Paul'}")  #another way to concatenate
      print("hello world".capitalize()) ##first character to capitalize
      print("Hello World".find('ello')) ##to find the characters in the string
      print("183".isdigit())
      print("you are what you eat".split('  ')) ### turns a string into cantainer (list) splitting the words at the space (‘ ‘) character
      return 0

if __name__ =="__main__":
    sys.exit=main()



