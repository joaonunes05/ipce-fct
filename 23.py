def is_leap_year(year: int) -> bool:
    """ Check if the year is a leap year. """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def month_length(month: int, year: int) -> int:
    """ Number of days of a given month (in a given year).
        Preconditions: 1 <= month <= 12
    """
    if month in {1, 3, 5, 7, 8, 10, 12}:    # teste de pertença a um set (teórica 6)
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2 and is_leap_year(year):
        return 29
    else:
        return 28

def main():
    month = int(input("Mês: "))
    year = int(input("Ano: "))
    print(month_length(month, year))

main()