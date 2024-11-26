#MATRIZ - nrows create e ncols do EX 48 dos labs
def create(nr: int, nc: int, value: any) -> list[list[int]]:
    """ Create and initialize a matrix with nr rows and nc columns.
        Precondition: nr >= 0 and nc >= 0
    """
    m = [None]*nr         # cria espaço para as linhas
    for i in range(nr):   # preenche as várias linhas
        m[i] = [value]*nc
    return m

def nrows(m: list[list[int]]) -> int:
    """ Number of rows of the matrix
        Precondition: is_valid(m)
    """
    return len(m)

def ncols(m: list[list[int]]) -> int:
    """ Number of columns of the matrix.
        Precondition: is_valid(m)
    """
    if len(m) == 0:           # a matriz vazia tem 0 colunas
        return 0
    else:
        return len(m[0])  

def compress(m: list[list[int]]) -> dict[(int,int), int]:
    nr, nc = nrows(m), ncols(m)
    d = dict()

    for i in range(nr):
        for j in range(nc):
            if m[i][j] != 0:
                d[(i, j)] = m[i][j]
    
    return d

def expand(d: dict[(int,int), int], nr: int, nc: int) -> list[list[int]]:
    m = create(nr, nc, 0)

    for e in d:
        m[e[0]][e[1]] = d[e]

    return m

""" print(compress([[5,0,0], 
                [0,0,0],
                [0,0,9]])) """

""" print(expand(compress([[5,0,0], [0,0,0], [0,0,9]]), 3, 3)) """

#IS BALANCED
def is_balanced(s: str) -> bool:
    delta = 0

    for i, c in enumerate(s):
        if delta < 0:
            return False
        elif c == '(':
            delta += 1
        elif c == ')':
            delta -= 1
    
    return delta == 0

#mais bem explicado
def is_balanced_d(s: str) -> bool:
    count_open, count_closed = 0, 0

    for i in range(len(s)):
        if count_closed > count_open: #opcional mas melhora a performance e o professor diz no enunciado
            return False
        if s[i] == '(':
            count_open += 1
        elif s[i] == ')':
            count_closed += 1

    return count_open == count_closed

