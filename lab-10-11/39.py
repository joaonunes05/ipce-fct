IList = list[int]    # definição de tipo

def input_list(l: IList, nome: str):
    """ Input a sequence of integers to l without changing the size of l. 
        Extra values are discarded. If there are few values, complete with zeros.
   """
    line = input(f"Introduza os valores de {nome}: ")
    s = line.split()      		# cria lista de strings
    m = len(s)
    n = len(l)
    i = -1
    for i in range(min(m,n)):    # converte cada string para um inteiro
        l[i] = int(s[i])
    for j in range(i+1, n):
        l[j] = 0

def draw_line(c: str, n: int):
    """ Draw a line with length n using the char c.
        Precondition: len(c) == 1 and n >= 0
    """
    for i in range(n):
        print(c, end='')
    print()

def print_list(l: IList, name: str):
    """ Show a list with a name. """
    print(f"    {name} = {str(l)}")

def copy(l1: IList, l2: IList):
    """ Copy the contents of ​ l1 to l2.
        Precondition: len(l1) == len(l2)
    """
    n = len(l1)
    for i in range(n):
        l2[i] = l1[i]    

def print_histogram(l: IList):
    """ Histogram for l with maximum width 40. """
    MAX_HISTOGRAM = 40
    for item in l:
        if item > MAX_HISTOGRAM:
            draw_line('*', MAX_HISTOGRAM)
        else:
            draw_line('*', item)

def reverse(l1: IList, l2: IList):
    """ Copy the inverted contents of list l1 to l2.
        Precondition: len(l1) == len(l2)
    """
    for i in range(len(l1)):
        l2[-(i+1)] = l1[i]

def equal(l1: IList, l2: IList) -> bool:
    """ Are two lists equal?
        Precondition: len(l1) == len(l2)
    """
    # Challenge: do not use l1 == l2; instead, compare the various elements.
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            pass
        else:
            return False
        return True

def longest_ascending(l: IList) -> int:
    """ Length of the longest ascending subsequence in l. """
    maxCount = 0
    count = 1

    lSort = sorted(l)

    for i in range(len(lSort) - 1):
        if lSort[i] == lSort[i + 1] - 1:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 1
    
    maxCount = max(maxCount, count)

    return maxCount

def maximum(l: IList) -> int:
    """ Maximum of list l.
        Precondition: len(l) > 0
    """
    for i in range(len(l)):
        pass


def copy_even_numbers(l1: IList, l2: IList):
    """ Copy only the even numbers from l1 to l2.
        Fills with 0s the remaining free space at the end of l2.
        Precondition: len(l1) == len(l2)
    """
    pass # TO DO

def proportion_of_even_numbers(l: IList) -> float:
    """ Proportion of even numbers in l.
        Precondition: len(l) > 0
    """
    pass # TO DO
    return 0.0

def is_ascending(l: IList) -> bool:
    """ Is l ascending in strict sense? """
    pass # TO DO
    return False

def summation(l: IList) -> int:
    """ Add all the elements of the list """
    # Challenge: do not use sum(l).
    pass # TO DO
    return 0

def dot_product(l1: IList, l2: IList) -> int:
    """ Inner product.
        Precondition: len(l1) == len(l2)
    """
    pass # TO DO
    return 0

def interpreter():
    la = [1, -2, 3, -4, 40, 50]  # list A
    sa = "A"                     # name of A
    
    lb = [0, 0, 0, 0, 0, 0]      # list B
    sb = "B"                     # name of list B
        
    if len(la) != len(lb) or len(la) == 0:
        print("ERRO INTERNO")
        return
    
    while True:
        print_list(la, sa)
        print_list(lb, sb)
        command_line = input("> ")     
        if command_line == '':
            command = ''
        else:
            command = command_line[0]

        if command == 'a':
            input_list(la, sa)

        elif command == 'b':
            input_list(lb, sb)

        elif command == 'c':
            print("COPIAR")
            copy(la, lb)

        elif command == 'h':
            print("HISTOGRAMA")
            print_histogram(la)

        elif command == 'i':
            print("INVERTER")
            reverse(la, lb)

        elif command == 'g':
            if equal(la, lb):
                print("IGUAIS")
            else:
                print("DIFERENTES")

        elif command == 'l':
            print(f"MAIOR ASCENDENTE = {longest_ascending(la)}")

        elif command == 'm':
            if len(la) == 0:
                print("IMPOSSÍVEL")
            else:
                print(f"MÁXIMO = {maximum(la)}")

        elif command == 'p':
            print("PARES")
            copy_even_numbers(la, lb)

        elif command == 'q':
            if len(la) == 0:
                print("IMPOSSÍVEL")
            else:
                print(f"PROPORÇÃO DE PARES = {proportion_of_even_numbers(la):.6f}")

        elif command == 'r':
            if is_ascending(la):
                print("CRESCENTE")
            else:
                print("NÃO CRESCENTE")

        elif command == 's':
            print(f"SOMA = {summation(la)}")

        elif command == 'x':
            print(f"PRODUTO = {dot_product(la, lb)}")

        elif command == 'z':
            print("Fim de execução! Volte sempre.")
            return

        elif command == '':
            pass

        else:
            print(f"Comando desconhecido: \"{command}\"")

interpreter()