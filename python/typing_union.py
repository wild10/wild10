from typing import Union


def square(x: Union[int, float] ) -> float:
    return x*x


n = 2.3             # this is fine with integer and float, but hints error with string.
print(square(n))