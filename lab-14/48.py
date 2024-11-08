type GList = list[any]           # lista genérica
type GMatrix = list[GList]       # matriz genérica

type IList = GList[int]          # lista de inteiros
type IMatrix = GMatrix[int]      # matriz de inteiros

def create(nr: int, nc: int, value: any) -> GMatrix:
    """ Create and initialize a matrix with nr rows and nc columns.
        Precondition: nr >= 0 and nc >= 0
    """
    m = [None]*nr         # cria espaço para as linhas
    for i in range(nr):   # preenche as várias linhas
        m[i] = [value]*nc
    return m

def is_valid(m: GMatrix) -> bool:
    """ Check if all the lines have the same length. """
    nr = len(m)
    for i in range(nr-1):  # verifica se todas as linhas têm igual comprimento
        if len(m[i]) != len(m[i+1]):
            return False
    return True

def nrows(m: GMatrix) -> int:
    """ Number of rows of the matrix
        Precondition: is_valid(m)
    """
    return len(m)             # número de linhas

def is_empty(m: GMatrix) -> int:
    """ Is the matrix empty? """
    return nrows(m) == 0      # testa se matriz vazia 

def ncols(m: GMatrix) -> int:
    """ Number of columns of the matrix.
        Precondition: is_valid(m)
    """
    if is_empty(m):           # a matriz vazia tem 0 colunas
        return 0
    else:
        return len(m[0])      # número de colunas é o comprimento duma linha

def row(m: GMatrix, i: int) -> GList:
    """ Get the row i of the matrix.
        Precondition: is_valid(m) and i in range(nrows(m))
    """
    return m[i].copy()      # faz cópia porque col também faz cópia

def col(m: GMatrix, j: int) -> GList:
    """ Get the column j of the matrix.
        Precondition: is_valid(m) and j in range(ncols(m))
    """
    col = []
    for r in m:             # acumula os vários elementos da coluna j
        col.append(r[j])
    return col

def input_int_matrix() -> IMatrix:
    """ Interactive matrix reading. """
    l = input("ROWS COLS: ").split()
    nr, rc = int(l[0]), int(l[1])
    m = []
    for i in range(nr):
        l = []
        for j in range(rc):
            x = int(input(f"m[{i}][{j}] = "))
            l.append(x)
        m.append(l)
    return m

def maximum(m: IMatrix) -> any:
    """ Maximum of matrix.
        Precondition: is_valid(m) and not is_empty(m) 
    """
    maximum = m[0][0]
    for i in range(nrows(m)):
        for j in range(ncols(m)):
            maximum = max(m[i][j], maximum)
    return maximum
    

def multiply(m: IMatrix, scalar: int) -> IMatrix:
    """ Multiply matriz by scalar.
        Precondition: is_valid(m)
    """
    nr, nc = nrows(m), ncols(m)
    m2 = create(nr, nc, 0)
    for i in range(nr):
        for j in range(nc):
            m2[i][j] = scalar * m[i][j]
    return m2

def diagonals(m: GMatrix) -> (GList, GList):
    """ Get the two diagonals of the matrix.
        Precondition: is_valid(m) and nrows(m) == ncols(m)
    """
    nr = nrows(m)
    d1 = [0] * nr
    d2 = d1.copy()
    for i in range(nr):
        d1[i] = m[i][i]
        d2[i] = m[i][nr - (i + 1)]
    return (d1, d2)

def transpose(m: GMatrix) -> GMatrix:
    """ Transpose of matrix .
        Precondition: is_valid(m)
    """
    nr, nc = nrows(m), ncols(m)
    m2 = create(nc, nr, 0)
    for i in range(nr):
        for j in range(nc):
            m2[j][i] = m[i][j]
    return m2

def product(m1: IMatrix, m2: IMatrix) -> IMatrix:
    """ Multiply two matrices.
        Precondition: is_valid(m1) and is_valid(m2)
                      and ncols(m1) == nrows(m2)
    """
    nr, nc = nrows(m1), ncols(m2)
    n = ncols(m2)
    m3 = create(nr, n, 0)
    for i in range(nr):
        for j in range(n):
            m3[i][j] = sum(a*b for a, b in zip(row(m1, i), col(m2, j)))
    return m3

def main():
    m1 = [ [1, 2, 3, 4],
           [5, 6, 7, 8] ]

    m2 = [ [ 1,  2,  3],
           [ 4,  5,  6],
           [ 7,  8,  9],
           [10, 11, 12] ]

    m3 = [ [1,  2,  3],
           [4,  5,  6],
           [7,  8,  9] ]
    
    s = input("TESTE: ")
    if s == "1":
        max = maximum(m1)
        print(max)
    elif s == "2":
        m = multiply(m1, 5)
        print(m)
    elif s == "3":
        t = diagonals(m3)
        print(t)
    elif s == "4":
        m = transpose(m1)
        print(m)
    elif s == "5":
        m = product(m1, m2)
        print(m)
    else:
        print("No test")

main()