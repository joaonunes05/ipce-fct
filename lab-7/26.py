def quadratic_polynomial_value(a: float, b: float, c: float, x: float) -> float:
    """ Eval a quadratic polynomial for the given value x """
    y = float((a * (x**2)) + (b*x) + c)
    return y

def print_table(a: float, b: float, c: float,
                lower_bound: float, upper_bound: float,
                n: int):                # no result
    """ Print table of values for a quadratic polynomial in a interval.
        Preconditions: lower_bound < upper_bound and n > 1
    """
    step = float((upper_bound - lower_bound)/(n-1))
    for i in range(0, n, 1):
        x = lower_bound + i*step
        y = quadratic_polynomial_value(a, b, c, x)
        print(f"{x:.6f} {y:.6f}")



def main():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    lower_bound = float(input("LOWER: "))
    upper_bound = float(input("UPPER: "))
    n_points = int(input("N: "))
    print_table(a, b, c, lower_bound, upper_bound, n_points)

main()