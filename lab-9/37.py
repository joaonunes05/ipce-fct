def draw_segment(x: str, n: int):
    """ Draw a partial line with length n using the char x.
        Precondition: len(x) == 1 and n >= 0
    """
    for i in range(n):
        print(x, end='')

def draw_funny_line(a: str, b: str, c: str, n: int, i: int):
    """ Draw a funny line with length n using the chars a, b, c.
        The position of b in the line is given by i.
        Precondition: len(a) == 1 and len(b) == 1 and len(c) == 1 and n > 0
    """
    draw_segment(a, n-(i+1))
    draw_segment(b, 1)
    draw_segment(c, i)
    print()

def draw_funny_square(a: str, b: str, c: str, n: int):
    """ Draw a funny square with side n using the chars a, b, c.
        Precondition: len(a) == 1 and len(b) == 1 and len(c) == 1 and n > 0
    """
    for i in range(n):
        draw_funny_line(a, b, c, n, i)

def main():
    n = int(input("Introduza o tamanho do lado: "))
    if not n > 0:
        print("Argumento inválido")
    else:
        draw_funny_square('*', '0', '#', n)

main()
