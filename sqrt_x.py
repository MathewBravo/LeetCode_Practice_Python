import math


def mySqrt(x: int) -> int:
    sqrt = math.sqrt(x)
    return math.floor(sqrt)


if __name__ == "__main__":
    print(mySqrt(4))
    print(mySqrt(8))
