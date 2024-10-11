def draw_full_line(c: str, n: int):
    """ Draw a full line with length n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        print(c, end='')
    print()

def draw_hollow_line(c: str, n: int):
    """ Draw a hollow line with length n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        if (i == 0 or i == n-1):
            print(c,end='')
        else:
            print(' ', end='')
    print()

def draw_frame(c: str, n: int):
    """ Draw a frame with side n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        if (i == 0 or i == n-1):
            draw_full_line(c, n)
        else:
            draw_hollow_line(c, n)


def main():
    n = int(input("Introduza o tamanho do lado: "))
    if not n >= 0:
        print("Argumento inválido")
    else:
        draw_frame('*', n)

main()