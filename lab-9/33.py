def draw_line(c: str, n: int):
    """ Draw a line with length n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        print(c, end='')
    print()

def draw_triangle(c: str, n: int):
    """ Draw a upright right triangle with side n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        draw_line(c, i+1)

def main():
    n = int(input("Introduza o tamanho do lado: "))
    if not n >= 0:
        print("Argumento inválido")
    else:
        draw_triangle('*', n)

main()