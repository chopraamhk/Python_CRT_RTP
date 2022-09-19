"""count characters"""

import sys

def main():
    word = input("word: ")
    character_count = dict() ##creating the dictionary using dict function
    for letter in word: #at each iteration, letter is a new letter from word
        character_count[letter] = word.count(letter)

    print(f"{character_count = }")
    return 0

if __name__ == "__main__":
    sys.exit=main()

