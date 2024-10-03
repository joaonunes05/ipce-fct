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

def is_date_valid(day: int, month: int, year: int) -> bool:
    """ Validate a calendar date. """
    return (month > 0 and month < 13 and day > 0 and day < (month_length(month, year) + 1))

def day_order(day: int, month: int, year: int) -> int:
    """ Position of a date within the respective year, starting with 1.
        Preconditions: is_date_valid(day, month, year)
    """
    order = day
    for i in range(1,month,1):
        order += month_length(i, year)
    return(order)

def main():
    day = int(input("Dia: "))
    month = int(input("Mês: "))
    year = int(input("Ano: "))
    if is_date_valid(day, month, year):
        print(day_order(day, month, year))
    else:
        print("DATA INVÁLIDA")

main()