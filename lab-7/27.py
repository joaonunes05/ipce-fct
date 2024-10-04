import math

def disc(a: float, b:float, c:float) -> float:
    val = (b**2) - (4*a*c)
    return val

def how_many_roots(a: float, b:float, c:float) -> int:
    if disc(a, b, c) > 0:
        return 2
    elif disc(a, b, c) == 0:
        return 1
    else:
        return 0

def root_left(a: float, b: float, c: float) -> float:
    if a < 0:
        x = (-b + math.sqrt(disc(a, b, c)))/(2*a)
        return x
    else:
        x = (-b - math.sqrt(disc(a, b, c)))/(2*a)
        return x

def root_right(a: float, b: float, c: float) -> float:
    if a > 0:
        x = (-b + math.sqrt(disc(a, b, c)))/(2*a)
        return x
    else:
        x = (-b - math.sqrt(disc(a, b, c)))/(2*a)
        return x

def main():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    n = how_many_roots(a, b, c)
    if n == 0:
        print("0")
    elif n == 1:
        print(f"1 {root_left(a,b,c)}")
    else:
        print(f"2 {root_left(a,b,c)} {root_right(a,b,c)}")

main()