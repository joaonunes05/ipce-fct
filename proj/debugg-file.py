def Zellercongruence(day, month, year):
    if year < 0:
        year += 1
    if (month < 3):
        month += 12
        year -= 1
    c = year // 100
    year = year % 100
    h = (c // 4 - 2 * c + year + year // 4 + 13 * (month + 1) // 5 + day - 1) % 7
    return (h + 7) % 7



def from_file(file_name: str) -> dict[str, list[int]]:
    """ Load a chronology from a file. """
    d = {}
    with open(file_name, 'r') as file:
        for line in file:
            l = line.strip()
            if l == '':
                continue
            elif l[0] == '#':
                continue
            else:
                t_date = line.split(' ')[0]
                t_name = " ".join(line.split(' ')[1:]).strip()
                print(t_date)
                print(t_name)

def cd(x: dict, y: dict) -> dict:
    return {**x, **y}

x = {'a': 3, 'b': 2, 'c': 1}
y = {'x':2, 'y': 1, 'c': 2}
print(cd(y, x))
