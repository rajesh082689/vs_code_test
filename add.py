def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    x = int(input("Enter first integer: "))
    y = int(input("Enter second integer: "))
    print(f"{x} + {y} = {add(x, y)}")
