def draw_line(c: str, n: int):
    """ Draw a line with length n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        print(c, end='')
    print()

def f(x: float) -> float:
    """ Some real function. """
    return (x * x) / 6

def draw_histogram_f(c: str, lim: int):
    """ Draw an histogram for f over [-lim, lim] using the char c.
        Precondition: len(c) == 1 and lim >= 0
    """
    for i in range(-lim, lim +1):
        draw_line(c, int(f(i)))

def main():
    lim = int(input("Introduza o valor do limite: "))
    if not lim >= 0:
        print("Argumento inválido")
    else:
        draw_histogram_f('*', lim)

main()