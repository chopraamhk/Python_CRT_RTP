import sys


def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)


def main():
    try:
        a = int(input("a: "))
    except ValueError:
        print(f"Invalid value for a; defaulting to a=1...", file=sys.stderr) ##It will say that it will print out the error msg as output
        a = 1
   r = str(input("r: "))
   try:
       assert isinstance(r,float)
       #assert type (r) == float
   except AssertionError:
    raise ValueError("invalid input for r")
    r = float(input("r: "))
    n = int(input("n: "))
    try:
        assert n >= 1
    except AssertionError: ##can have multiple exceptions. -- There are different types of exceptions.
        raise ValueError(f"Invalid value for n; default to n=10...")
    else:
        print(f"s_{n} = {calculate_geometric_series(a, r, n=n)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
