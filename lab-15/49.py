############# type Date #############

type Date = (int, int, int)   # (day, month, year)

def is_leap_year(year: int) -> bool:
    """ Check if the year is a leap year. """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def month_length(month: int, year: int) -> int:
    """ Number of days of a given month (in a given year).
        Precondition: 1 <= month <= 12
    """
    MONTHS = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2 and is_leap_year(year):
        return MONTHS[2] + 1
    else:
        return MONTHS[month]

def date_is_valid(dt: Date) -> bool:
    """ Is the date valid? """
    day, month, year = dt
    return (year > 0          # estamos só interessados na "Era Comum"
        and 1 <= month <= 12
        and 1 <= day <= month_length(month, year))

def date(day: int, month: int, year: int) -> Date:
    """ Create a date. """
    return (day, month, year)

def date_input(prompt: str) -> Date:
    """ Interactive date reading. """
    s = input(prompt)
    if s == '':
        return None
    
    day, month, year = map(int, s.split('/'))
    return (date(day, month, year))

def date_as_str(dt: Date) -> str:
    """ Convert date to string.
        Precondition: date_is_valid(dt)
    """
    day, month, year = dt
    return f"{day}/{month}/{year}"

def date_print(dt: Date):
    """ Print a date.
        Precondition: date_is_valid(dt)
    """
    print(date_as_str(dt))

def date_is_less(dt1: Date, dt2: Date) -> bool:
    """ Check if dt1 < dt2.
        Precondition: date_is_valid(dt1) and date_is_valid(dt2)
     """
    return (next((x  for x in [a - b for a, b in zip(dt1, dt2)] if x != 0), 0) < 0)


def date_is_equal(dt1: Date, dt2: Date) -> bool:
    """ Check if dt1 == dt2.
        Precondition: date_is_valid(dt1) and date_is_valid(dt2)
     """
    return (dt1 == dt2)

def date_order(dt: Date) -> int:
    """ The position of a date within the respective year, starting with 1.
        Precondition: date_is_valid(dt)
    """
    day, month, year = dt
    days = 0
    for i in range(month - 1):
        days = days + month_length(month, year)
    days = days + day
    return days

def date_next(dt: Date) -> Date:
    """ Create the date of the next day.
        Precondition: date_is_valid(dt)
    """
    day, month, year = dt
    if (day == month_length(month, year)):
        day = 1
        if (month == 12):
            year = year + 1
            month = 1
        else:
            month = month + 1
    else:
        day = day + 1

    return (day, month, year)

def date_prev(dt: Date) -> Date:
    """ Create the date of the previous day.
        Precondition: date_is_valid(dt)
                   and not date_is_equal(date(1,1,1), dt)
    """
    day, month, year = dt
    if (day == 1):
        if (month == 1):
            year = year - 1
            month = 12
        else:
            month = month - 1
        day = month_length(month, year)
    else:
        day = day - 1

    return (day, month, year)

############# type Dates #############

END_MARK = ''

type Dates = list[Date]

def dates_input(prompt1: str, prompt2: str) -> Dates:
    """ Interactive date sequence reading. """
    print(prompt1)
    l = []
    while True:
        dt = date_input(prompt2)
        if dt == None:
            break
        l.append(dt)
    return l

def dates_print(dts: Dates):
    """ Print a sequence of dates.
        Precondition: all(valid_date(dt) for dt in dts)
    """
    for dt in dts:
        date_print(dt)

def dates_maximum(dts: Dates) -> Date:
    """ Maximum date.
        Precondition:
    """
    maxdate = dts[0]
    for date in dts:
        if (date_is_less(maxdate, date)):
            maxdate = date
    return (maxdate)

def dates_minimum(dts: Dates) -> Date:
    """ Minimum date.
        Precondition:
           len(dts) > 0 and all(valid_date(dt) for dt in dts)
    """
    mindate = dts[0]
    for date in dts:
        if (date_is_less(date, mindate)):
            mindate = date
    return mindate
    
############# main #############

def main():
    dts = dates_input(
    	("Introduza uma data por linha, "
    	+ "tudo terminado por uma linha vazia:"),
    	"D/M/Y: ")
    if dts == []:
        print("Não há datas!")
    else:
        max = dates_maximum(dts)
        min = dates_minimum(dts)
        print(f"Data máxima: {date_as_str(max)}")
        print(f"Data mínima: {date_as_str(min)}")
        print(f"Ord max: {date_order(max)}")
        print(f"Next max: {date_as_str(date_next(max))}")
        print(f"Prev max: {date_as_str(date_prev(max))}")

main()