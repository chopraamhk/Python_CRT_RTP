import random
import sys


def double_number(n):
    return 2 * n


def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{list(map(double_number, random_numbers)) = }" ##map -> efficient way to not add all the data into memory


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{filter(lambda w: len(w) > 7, words) = }")


def main():
    using_map()  ##can comment this and check
    using_map_and_lambda()
    using_filter() ##can comment this and check
    return 0


if __name__ == '__main__':
    sys.exit(main())
