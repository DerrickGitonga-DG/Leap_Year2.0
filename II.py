for i in range(2, 30, 5):  # rang(start,stop,step)
    print(i, end=" ")


def check(num: float) -> None:
    if num <= 50.0:
        print("Has passed")
    else:
        print("Has not passed")
        return


def check_two(num: float) -> bool:
    if num <= 50:
        return True
    else:
        return False


def calcAreaOfCircle(radius: float) -> float:
    return 3.14 * (radius ** 2)


def sum_I(b: float, y: float) -> float:
    return b + y


def sum_II(b: float, y: float) -> float:
    return b + y


def sum_III(b: float, y: float) -> float:
    return b + y


print(calcAreaOfCircle(7.2))

check(89.9)
check_two(45.7)

has_passed: bool = check_two(30.2)
print(has_passed)