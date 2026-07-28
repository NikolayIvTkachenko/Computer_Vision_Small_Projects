



def min(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b

def max(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b

def min_v2(a: int, b: int) -> int:
    return -max(-a, -b)


def clamp(x: int, lower: int, upper: int) -> int:
    if x < lower:
        return lower
    elif x > upper:
        return upper
    else:
        return x

def clamp_v2(x: int, lower: int, upper: int) -> int:
    return max(lower, min(upper, x))






