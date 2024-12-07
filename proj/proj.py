#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
max width = 100 columns
tab = 4 spaces
01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
------------------------------------------------------

------------------------------------------------------
Introdução à Programação para a Ciência e Engenharia - Projeto de 2024/2025

*** Datas & Cronologias ***

Calendário gregoriano proléptico

 AUTHORS IDENTIFICATION
	Estudante 1: 69855, Afonso Castro
	Estudante 2: 71710, Joao Nunes

Comments:
......................................
......................................

Place here the numbers and names of the authors, plus possibly some comments.
Do not deliver an anonymous file with unknown authors.
------------------------------------------------------

======================================================
CHANGELOG:
18/nov - Adicionado "@staticmethod" na função Util.error.
18/nov - Adicionados comentários em alguns métodos que não tinham comentário.
18/nov - Removida a função Date.move_year, que ficou esquecida duma experiência que foi feita. Mas se alguém descobrir alguma utilidade para essa função, pode deixar ficar, claro.
======================================================

"""
from __future__ import annotations

class Util:
    @staticmethod
    def file_exists(file_name: str) -> bool:
        """ Check if a file can be opened in read mode. """
        try:
           f = open(file_name, 'r')
           f.close()
           return True
        except FileNotFoundError:
           return False

    @staticmethod
    def error(mesg: str):
        """ Issue an error message. """
        print("ERRO:", mesg)
        print('')

    @staticmethod
    def printf(mesg: str):
        """Prints in correct format - blanck line after"""
        print(mesg)
        print('')

    @staticmethod
    def help():
        print('Legenda: d-Data(dd/mm/aaaa) i-inteiro s-string')
        print('-----------------------------------------------------------------')
        print('|Comando   | Funcionalidade                                     |')
        print('|---------------------------------------------------------------|')
        print('|A         | Lista de Comamdos Disponiveis                      |')
        print('|=         | Lista de Autores                                   |')
        print('|+ d i     | Avancar/Recuar(-) i dias de d                      |')
        print('|- d1 d2   | Nr de dias entre d1 e d2                           |')
        print('|C i1 i2   | Calendario para mes i2 do ano i1/ano total se i2=0)|')
        print('|D i1 i2   | Nr de dias do mes i2 do ano i1                     |')
        print('|F i1 i2   | Feriados no mes i2 do ano i1/ ano i1 se i2=0       |')
        print('|H         | Dia de Hoje                                        |')
        print('|I d       | Idade de alguem que nasceu a d                     |')
        print('|M d1 d2 i | Maximizar i dias de ferias entre d1 e d2           |')
        print('|S d       | Dia da semana de d                                 |')
        print('|T i       | Sextas-feiras 13 no ano i                          |')
        print('|U s f     | Carrega cronologia em f com nome s                 |')
        print('|V s       | Mostra a cronologia com nome s                     |')
        print('|W s1 s2   | Cria cronologia s1 com as datas repetidas em s2    |')
        print('|X s1 s2   | Cria cronologia s1 com elementos de s2 em feriados |')
        print('|Y s1 s2 s3| Cria cronologia s1 com a uniao de s2 e s3          |')
        print('|Z s1 s2 s3| Cria cronologia s1 com a uniao de s2 e s3          |')
        print('|Q         | Fecha o programa                                   |')
        print('-----------------------------------------------------------------')
        print('')


class DateFormats:
    WEEK_NAMES = [
            "Domingo", "Segunda-feira", "Terça-feira",
            "Quarta-feira", "Quinta-feira",
            "Sexta-feira", "Sábado"]

    WEEK_NAMES_ABR = ['Do', 'Sg', 'Te', 'Qa', 'Qi', 'Sx', 'Sa']
    MONTH_NAMES = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
    MONTH_CALENDAR_LENGTH = 22

    @staticmethod
    def from_str(s: str) -> Date:
        """ Build a date from a string.
            If the format is invalid or the date is invalid then return None.
        """
        l = s.split("/")
        valid_format = (
                len(l) == 3
            and l[0].isdigit()
            and l[1].isdigit()
            and len(l[2]) > 0
            and (l[2][1:].isdigit() if l[2][0] == '-' else l[2].isdigit())
         )
        if not valid_format:
            return None
        day, month, year = [int(x) for x in l]
        d = Date(day, month, year)
        if not d.is_valid():
            return None
        return d

    @staticmethod
    def to_day_of_week(d: Date) -> str:
        """ Converts a 0-6 int to week day name"""
        return DateFormats.WEEK_NAMES[d.day_of_the_week()]

    @staticmethod
    def to_str(d: Date) -> str:
        """ Convert a date to a formated string. """
        return f"{d.day}/{d.month}/{d.year}"

    @staticmethod
    def cal_month(month, year) -> str:
        """ Generate the calendar for a given month and year.
            Prerequisites: Date(1, month, year) is valid"""
        month_length = Date.month_length(month, year)
        first_day_weekday = Date(1, month, year).day_of_the_week()
        calendar_lines = []

        calendar_lines.append(f"{DateFormats.MONTH_NAMES[month-1]} {year}")
        calendar_lines.append(' '.join(DateFormats.WEEK_NAMES_ABR))
        current_line = ' ' * (3 * first_day_weekday)

        current_day = 1
        current_weekday = first_day_weekday

        while current_day <= month_length:
            current_line += f"{current_day:2d}"
            current_weekday = (current_weekday + 1) % 7

            if current_weekday == 0 or current_day == month_length:
                calendar_lines.append(current_line.rstrip())
                current_line = ''
            else:
                current_line += ' '
            current_day += 1

        if current_line:
            calendar_lines.append(current_line.rstrip())

        return '\n'.join(calendar_lines) + '\n'

    @staticmethod
    def get_line_in_year(month: int, year: int, l: int) -> str:
        """Draw one numbered line for yearly calendar"""
        line = []
        for i in range(month, month+3):
            if l < len(DateFormats.cal_month(i, year).split('\n')):
                line.append(DateFormats.cal_month(i, year).split('\n')[l] + \
                    ' ' * (DateFormats.MONTH_CALENDAR_LENGTH - len(DateFormats.cal_month(i, year).split('\n')[l])))
            else:
                line.append(' '*DateFormats.MONTH_CALENDAR_LENGTH)
        return ''.join(line)


    @staticmethod
    def cal_year(year: int) -> str:
        """ Generate the full calendar for a given year. """
        full_calendar = [str(year)]
        for quarter in range(1, 13, 3):
            line = [DateFormats.MONTH_NAMES[x-1] + (" "*(DateFormats.MONTH_CALENDAR_LENGTH-len(DateFormats.MONTH_NAMES[x-1]))) \
                for x in range(quarter, quarter+3)]
            full_calendar.append(''.join(line))
            line2 = [DateFormats.cal_month(x, year).split('\n')[1] + '  ' for x in range(quarter, quarter + 3)]
            full_calendar.append(''.join(line2))
            for l in range(2,max([len(DateFormats.cal_month(x, year).split('\n')) - 1 for x in range(quarter, quarter + 3)])):
                full_calendar.append(DateFormats.get_line_in_year(quarter, year, l))
            full_calendar.append('')

        return '\n'.join(full_calendar)


class Date:
    # Constants shared by all the methods
    VARIABLE_HOLIDAYS_NAMES = [
            "Páscoa", "Carnaval", "Sexta-feira Santa", "Corpo de Cristo"]

    # Variables shared by all the methods
    fixed_holidays = None
    non_fixed_holidays = None
    holidays = None

    # Static methods - functions without "self"
    @staticmethod
    def set_fixed_holidays(h: Chronology):
        """ Setup the variable 'fixed_holidays'.
            Must call this function before start using any
            methods related to holidays. """
        Date.fixed_holidays = h

    def set_non_fixed_holidays(self: Date):
        """ Setup the variable 'non_fixed_holidays'.
            Must call this function before start using any
            methods related to holidays. """
        if self.year < 0:
            return
        d = {}
        d['Páscoa'] = Date.easter(self.year)
        d['Sexta-feira Santa'] = d['Páscoa'].copy().move(-2)
        d['Carnaval'] = d['Páscoa'].copy().move(-47)
        d['Corpo de Deus'] = d['Páscoa'].copy().move(60)

        self.non_fixed_holidays = Chronology(d)

    def set_holidays(self: Date):
        if self.non_fixed_holidays:
            self.holidays = self.fixed_holidays.union(self.non_fixed_holidays)
        else:
            self.holidays = self.fixed_holidays

    @staticmethod
    def is_zero(year: int) -> bool:  # PRIVATE
        """ Check for the invalid year zero? """
        return year == 0

    @staticmethod
    def is_bc(year: int) -> bool:  # PRIVATE
        """ Check for a negative date - before Christ? """
        return year < 0

    @staticmethod
    def is_leap(year: int) -> bool:
        """ Check if the year is a leap year.
            Precondition: not is_zero(year)
        """
        if year > 0:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        else:
            return (year + 1) % 4 == 0 and ((year + 1) % 100 != 0 or (year + 1) % 400 == 0)

    @staticmethod
    def month_length(month: int, year: int) -> int:
        """ Number of days of a given month (in a given year).
            Precondition: 1 <= month <= 12 and not is_zero(year)
        """
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif Date.is_leap(year):
            return 29
        else:
            return 28

    @staticmethod
    def year_lenght(year: int) -> int:
        """ Number of days of a given year.
            Precondition: not is_zero(year)
        """
        if(Date.is_leap(year)):
            return 366
        return 365


    @staticmethod
    def from_str(s: str) -> Date:
        """ Build a date from a string.
            If the date is invalid then return None.
        """
        return DateFormats.from_str(s)

    @staticmethod
    def today() -> Date:
        """ Today's date. """
        from time import strftime
        return DateFormats.from_str(strftime("%d/%m/%Y"))

    @staticmethod
    def easter(year: int) -> Date:
        """ Date of easter for a given year.
            Precondition: year > 0
            Sources:
                https://aa.usno.navy.mil/faq/easter
                https://adsabs.harvard.edu/full/1940BuAst..12..391O
        """
        y = year
        c = y // 100
        n = y - 19 * (y // 19)
        k = (c - 17) // 25
        i = c - c // 4 - (c - k) // 3 + 19 * n + 15
        i = i - 30 * (i // 30)
        i = i - (i // 28) * (1 - (i // 28)
                             * (29 // (i + 1)) * ((21 - n) // 11))
        j = y + y // 4 + i + 2 - c + c // 4
        j = j - 7 * (j // 7)
        l = i - j
        m = 3 + (l + 40) // 44
        d = l + 28 - 31 * (m // 4)
        return Date(d, m, y)

    @staticmethod
    def fridays13(year: int) -> list[Date]:
        """ The list of all the fridays 13 dates for a given year.  """
        return [Date(13, m, year) for m in range(1,13) if Date(13, m, year).day_of_the_week() == 5]

    # Instance methods - functions with "self"

    def __init__(self: Date, day: int, month: int, year: int):
        """ Initialize a date. """
        self.day = day
        self.month = month
        self.year = year

    def copy(self: Date) -> Date:
        """ Duplicate a date. """
        return Date(self.day, self.month, self.year)

    def is_valid(self: Date) -> bool:  # PRIVATE
        """ Is the date valid? """
        return (
            not Date.is_zero(self.year)
            and self.day in range(1, Date.month_length(self.month, self.year) + 1)
            and self.month in range(1, 13)
        )

    def __repr__(self: Date) -> str:
        """ Convert date to string. """
        return DateFormats.to_str(self)

    def __lt__(self: Date, other: Date) -> bool:
        """ Check if self < other.
            Precondition: self.is_valid() and other.is_valid()
        """
        return (
            self.year < other.year
            or (self.year == other.year and self.month < other.month)
            or (self.year == other.year and self.month == other.month and self.day < other.day)
        )

    def __eq__(self: Date, other: Date) -> bool:
        """ Check if self == other.
            Precondition: self.is_valid() and other.is_valid()
        """
        return (
            self.year == other.year and self.month == other.month and self.day == other.day
        )

    def __le__(self: Date, other: Date) -> bool:
        """ Check if self <= other.
            Precondition: self.is_valid() and other.is_valid()
        """
        return (
            self.year <= other.year
            or (self.year == other.year and self.month <= other.month)
            or (self.year == other.year and self.month == other.month and self.day <= other.day)
        )

    def order(self: Date) -> int:
        """ The position of a date within the respective year, starting with 1.
            Precondition: self.is_valid()
        """
        return sum(Date.month_length(m, self.year) for m in range(1, self.month)) + self.day

    def next(self: Date) -> Date:
        """ Create the date of the next day.
            Precondition: self.is_valid()
        """
        next_day, next_day_month, next_day_year = self.day + 1, self.month, self.year

        if next_day > self.month_length(next_day_month, next_day_year):
            next_day = 1
            next_day_month = self.month + 1 if self.month < 12 else 1
            next_day_year += 0 if next_day_month > 1 else 1

        return Date(next_day, next_day_month, next_day_year)

    def prev(self: Date) -> Date:
        """ Create the date of the previous day.
            Precondition: self.is_valid()
        """
        if self.day == 1:
            prev_day_month = self.month - 1 if self.month > 1 else 12
            prev_day_year = self.year if prev_day_month != 12 else \
            (self.year - 1 if self.year != 1 else self.year - 2)
            prev_day = self.month_length(prev_day_month, prev_day_year)
        else:
            prev_day = self.day - 1
            prev_day_month, prev_day_year = self.month, self.year

        return Date(prev_day, prev_day_month, prev_day_year)

    def move(self: Date, n: int) -> Date:
        """ Create a date shifted n days .
            Precondition: self.is_valid()
        """
        final_date = self.copy()
        if n > 0:
            for _ in range(n):
                final_date = final_date.next()
        else:
            for _ in range(abs(n)):
                final_date = final_date.prev()
        return final_date



    def distance(self: Date, other: Date) -> int:
        """ Number of days from self to other. Can be negative. .
            Precondition: self.is_valid() and other.is_valid()
        """
        temp_date = self.copy()
        dist = 0
        if self < other:
            while temp_date != other:
                dist -= 1
                temp_date = temp_date.next()
        else:
            while temp_date != other:
                dist += 1
                temp_date = temp_date.prev()
        return dist

    def age(self: Date) -> int:
        """ The current age in years for somebody that has born in the date self.
            Precondition: self.is_valid() and self <= Date.today()
        """
        if self > Date.today():
            return -1
        day = self.next().day if (self.day == 29 and self.month == 2 and not Date.is_leap(Date.today().year))\
            else self.day
        age = Date.today().year - self.year if \
            Date.today().month > self.month \
            or (Date.today().month == self.month and Date.today().day >= day) \
            else Date.today().year - self.year - 1
        return age

    def day_of_the_week(self: Date) -> int:
        """ Calculate the day of week of a date.
            Precondition: self.is_valid()
            Source: Zellers congruence algorithm explained @ geeksforgeeks.org (adapted)
        """
        day, month, year = self.day, self.month, self.year

        if year < 0:
            year += 1
        if (month < 3):
            month += 12
            year -= 1
        c = year // 100
        year = year % 100
        h = (c // 4 - 2 * c + year + year // 4 + 13 * (month + 1) // 5 + day - 1) % 7

        return (h + 7) % 7

    def get_month_hollidays(self: Date) -> Chronology:
        """ Gets the Fixed Holidays for the acutal month
            Preconditions: set_fixed_holidays must have been called
        """
        d = {}
        for name, date in self.holidays.events.items():
            if date.month == self.month:
                d[name] = date
        if d:
            return Chronology(d)
        return None

    def get_max_holidays(self: Date, other: Date, n: int) -> Date:
        """ Gets the Fixed Holidays for the acutal month
            Preconditions: set_fixed_holidays must have been called
        """
        holidays_and_weekends = []
        final_date = self.copy()

        t1_date, t2_date = self.copy(), other.copy()
        t2_date = t2_date.next()
        while t1_date < t2_date:
            c = Chronology.from_file('feriados_fixos.txt')
            c.change_year(t1_date.year)
            t1_date.set_fixed_holidays(c)
            t1_date.set_non_fixed_holidays()
            t1_date.set_holidays()

            if t1_date.day_of_the_week()in [0, 6] or t1_date in t1_date.holidays.events.values():
                holidays_and_weekends.append(1)
            else: holidays_and_weekends.append(0)
            t1_date = t1_date.next()

        max_consecutive = 0
        best_start_index = 0

        for start in range(len(holidays_and_weekends)):
            remaining_days = n
            current_consecutive = 0

            for end in range(start, len(holidays_and_weekends)):
                if holidays_and_weekends[end] == 0:
                    if remaining_days > 0:
                        remaining_days -= 1
                    else:
                        break

                current_consecutive += 1

            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
                best_start_index = start

        for _ in range(best_start_index):
            final_date = final_date.next()

        return final_date

class Chronology:
    def __init__(self: Chronology, events: dict[str, Date]):
        """ Initialize a chronology from a dict. Sort the chronology. """
        self.events = events
        self.sort()      # ensures it is created sorted by key

    @staticmethod
    def from_file(file_name: str) -> Chronology:
        """ Load a chronology from a file. """
        dict = {}
        with open(file_name, 'r') as file:
            for line in file:
                l = line.strip()
                if l == '':
                    continue
                elif l[0] == '#':
                    continue
                else:
                    d, m, y = [int(x) for x in line.split(' ')[0].split('/')]
                    dict[" ".join(line.split(' ')[1:]).strip()] = Date(d, m, y)

        return Chronology(dict)

    def sort(self: Chronology):  # PRIVATE
        """ Sort by key. """
        self.events = dict(sorted(self.events.items(), key = lambda item: (item[1], item[0])))

    def __repr__(self: Chronology) -> str:
        """ Convert chronology to string, to display. """
        s = ''
        for e in self.events:
            s += f"\n{e} ---> {self.events[e]}"
        return s[1:]

    def size(self: Chronology) -> int:
        """ Size of chronology. """
        return len(self.events)

    def union(self: Chronology, other: Chronology) -> Chronology:
        """ Union of chronologies. """
        return Chronology({**self.events, **other.events})

    def repeated(self: Chronology) -> Chronology:
        d = {}
        keys = list(self.events.keys())

        for i in range(len(keys)-1):
            if self.events[keys[i]] == self.events[keys[i+1]]:
                if not keys[i] in d: d[keys[i]] = self.events[keys[i]]
                d[keys[i+1]] = self.events[keys[i+1]]

        return Chronology(d)

    def intersection(self: Chronology, other: Chronology) -> Chronology:
        d = {}
        for n1, d1 in self.events.items():
            for n2, d2 in other.events.items():
                if d1 == d2:
                    d[n1] = d1
                    d[n2] = d2
        return Chronology(d)

    def get_holidays(self: Chronology) -> Chronology:
        """ Gets the days of a chronology which are Holidays"""
        d = {}
        for name, date in self.events.items():
            c = Chronology.from_file('feriados_fixos.txt')
            c.change_year(date.year)
            date.set_fixed_holidays(c)
            date.set_non_fixed_holidays()
            date.set_holidays()

            for date_h in date.holidays.events.values():
                if date_h == date:
                    d[name] = date

        return Chronology(d)

    def change_year(self: Chronology, year: int):
        """ Changes the year of all Chronology events
            To use with fixed holidays and probably nothing more """
        for name, date in self.events.items():
            self.events[name] = Date(self.events[name].day, self.events[name].month, year)

class Chronologies:
    def __init__(self: Chronologies):
        """ Initialize a repository of chronologies as empty. """
        self.cronos = dict()

    def get(self: Chronologies, id: str) -> Chronology:
        """ Get a named chronology. If it does not exist return None. """
        if id in self.cronos:
            return self.cronos[id]
        else:
            return None

    def add(self: Chronologies, id: str, c: Chronology):
        """ Add a chronology. """
        self.cronos[id] = c

    def load(self: Chronologies, id: str, file_name: str):
        """ Load a chronology from file and assign a id to it. """
        self.cronos[id] = Chronology.from_file(file_name)

    def show(self: Chronologies):
        """ Show the contents of the repository, for debuging. """
        for id in self.cronos:
            print(id, "--", self.cronos[id].events)


class UI:   # User Interface
    PROG_NAME = "Datas & Cronologias"

    def __init__(self: UI):
        """ Initialize a UI with an empty repository of cronologies. """
        self.repository = Chronologies()

    def dir(self: UI):
        """ Show the current directory, only for debugging. """
        from os import getcwd
        print(getcwd())

    def welcome(self: UI):  # PRIVATE
        """ Print an welcome message. """
        Util.printf(UI.PROG_NAME)

    def input_command(self: UI) -> (str, list[str]):  # PRIVATE
        """ Process the command line. """
        command_line = input("> ")
        l = command_line.split()
        if l == []:
            command = ' '
        else:
            command = l[0].upper()
        arguments = l[1:]
        return (command, arguments)

    def get_args(self: UI, args: list[str], types: str) -> list[any]:  # PRIVATE
        """ Convert and validate the arguments of any command. """
        error = False
        res = []
        if len(args) != len(types):
            error = True
        else:
            for i in range(len(args)):
                if types[i] == 'd':  # 'd' means Date
                    d = Date.from_str(args[i])
                    if d is None:
                        error = True; break
                    else:
                        res.append(d)
                elif types[i] == 'i':  # 'i' means integer
                    is_int = (args[i][1:].isdigit()
                              if args[i][0] == '-'
                              else args[i].isdigit())
                    if not is_int:
                        error = True; break
                    i = int(args[i])
                    res.append(i)
                elif types[i] == 's':  # 's' means string
                    res.append(args[i])
                else:
                    error = True; break
        if error:
            Util.error("Argumentos inválidos.")
            res = ['x']*len(types)     # dummy result with the correct length
        if len(types) == 0:
            return error
        else:
            res.insert(0, error)
            return res

    def command_authors(self: UI, args: list[str]):  # PRIVATE
        error = self.get_args(args, "")
        if error: return
        print(UI.PROG_NAME)
        Util.printf("Autores: Afonso Castro (69855), Joao Nunes (71710)")

    def command_plus(self: UI, args: list[str]):  # PRIVATE
        error, d, n = self.get_args(args, "di")
        if error: return
        res = d.move(n)
        Util.printf(res)

    def command_less(self: UI, args: list[str]):  # PRIVATE
        error, d1, d2 = self.get_args(args, "dd")
        if error: return
        res = d1.distance(d2)
        Util.printf(res)

    @staticmethod
    def command_today():  # PRIVATE
        Util.printf(Date.today())

    def command_days(self: UI, args: list[str]):
        error, y , m = self.get_args(args, "ii")

        if error: return
        elif y == 0 or m < 0 or m > 12:
            Util.error("Argumentos inválidos.")
            return
        if m == 0:
            res = Date.year_lenght(y)
            Util.printf(res)
            return
        res = Date.month_length(m, y)
        Util.printf(res)

    def command_holidays(self: UI, args: list[str]):
        error, y, m = self.get_args(args, "ii")

        if error: return
        if m == 0 and Date.is_valid(Date(1, 1, y)):
            d = Date(1, 1, y)
            c = Chronology.from_file('feriados_fixos.txt')
            c.change_year(y)
            d.set_fixed_holidays(c)
            d.set_non_fixed_holidays()
            d.set_holidays()
            Util.printf(d.holidays)
        elif Date.is_valid(Date(1, m, y)):
            d = Date(1, m, y)
            c = Chronology.from_file('feriados_fixos.txt')
            c.change_year(y)
            d.set_fixed_holidays(c)
            d.set_non_fixed_holidays()
            d.set_holidays()
            if not d.get_month_hollidays():
                Util.printf("Nada.")
                return
            Util.printf(d.get_month_hollidays())
        else:
            Util.error("Argumentos inválidos.")
            return

    def command_age(self: UI, args: list[str]):
        error, d = self.get_args(args, "d")

        if error: return
        a = d.age()
        if a == -1:
            Util.error("Você ainda não nasceu.")
            return
        Util.printf(a)

    def command_weekday(self: UI, args: list[str]):
        error, d = self.get_args(args, "d")

        if error: return
        Util.printf(DateFormats.to_day_of_week(d))

    def command_FT13(self: UI, args: list[str]):
        error, y = self.get_args(args, "i")
        if error: return
        if y == 0:
            Util.error("Argumentos inválidos.")
            return
        for x in Date.fridays13(y):
            print(x)
        print('')

    def command_add_crono(self: UI, args: list[str]):
        error, n, p = self.get_args(args, "ss")
        if error: return
        try:
            with open(p, 'r'):
                try:
                    self.repository.load(n, p)
                    for value in self.repository.cronos[n].events.values():
                        if not value.is_valid():
                            del(self.repository.cronos[n])
                            Util.error(f"O ficheiro '{p}' contém uma cronologia inválida.")
                            return
                    Util.printf(f"Foram carregados {len(self.repository.cronos[n].events)} elementos.")
                except:
                    Util.error(f"O ficheiro '{p}' contém uma cronologia inválida.")

        except FileNotFoundError:
            Util.error(f"Não foi possível abrir o ficheiro '{p}'.")

    def command_view_crono(self: UI, args: list[str]):
        error, n = self.get_args(args, "s")
        if error: return
        elif not self.repository.get(n):
            Util.error(f"Não existe uma cronologia com o nome '{n}'.")
            return
        elif not self.repository.get(n).events:
            Util.printf('Nada.')
        else:
            Util.printf(self.repository.get(n))

    def command_repeated_crono(self: UI, args: list[str]):
        error, n1, n2  = self.get_args(args, "ss")
        if error: return
        if not self.repository.get(n2):
            Util.error(f"Não existe uma cronologia com o nome '{n2}'.")
            return
        self.repository.add(n1, self.repository.get(n2).repeated())

    def command_holidays_in_crono(self: UI, args: list[str]):
        error, n1, n2 = self.get_args(args, "ss")
        if error: return
        if not self.repository.get(n2):
            Util.error(f"Não existe uma cronologia com o nome '{n2}'.")
            return
        self.repository.add(n1, self.repository.get(n2).get_holidays())

    def command_union(self: UI, args: list[str]):
        error, n1, n2, n3 = self.get_args(args, "sss")
        if error: return
        if not self.repository.get(n2):
            Util.error(f"Não existe uma cronologia com o nome '{n2}'.")
            return
        elif not self.repository.get(n3):
            Util.error(f"Não existe uma cronologia com o nome '{n3}'.")
            return
        self.repository.add(n1, self.repository.get(n2).union(self.repository.get(n3)))

    def command_intersec(self: UI, args: list[str]):
        error, n1, n2, n3 = self.get_args(args, "sss")
        if error: return
        elif not self.repository.get(n2):
            Util.error(f"Não existe uma cronologia com o nome '{n2}'.")
            return
        elif not self.repository.get(n3):
            Util.error(f"Não existe uma cronologia com o nome '{n3}'.")
            return
        self.repository.add(n1, self.repository.get(n2).intersection(self.repository.get(n3)))

    def command_max_holidays(self: UI, args: list[str]):
        error, d1, d2, n = self.get_args(args, "ddi")
        if error: return
        elif d1 > d2:
            Util.error("Argumentos inválidos.")
            return
        Util.printf(d1.get_max_holidays(d2, n))

    def command_calendar(self: UI, args: list[str]):
        error, y, m = self.get_args(args, "ii")
        if error: return
        elif m == 0 and Date.is_valid(Date(1, 1, y)):
            print(DateFormats.cal_year(y))
            return
        elif Date.is_valid(Date(1, m, y)):
            print(DateFormats.cal_month(m, y))
            return
        else:
            Util.error("Argumentos inválidos.")
            return


    def command_help(self: UI):
        Util.help()

    def interpreter(self: UI):
        self.welcome()
        while True:
            command, args = self.input_command()
            if command == '=': self.command_authors(args)
            elif command == '+': self.command_plus(args)
            elif command == '-': self.command_less(args)
            elif command == 'H': self.command_today()
            elif command == 'D': self.command_days(args)
            elif command == 'F': self.command_holidays(args)
            elif command == 'I': self.command_age(args)
            elif command == 'S': self.command_weekday(args)
            elif command == 'T': self.command_FT13(args)
            elif command == 'U': self.command_add_crono(args)
            elif command == 'V': self.command_view_crono(args)
            elif command == 'W': self.command_repeated_crono(args)
            elif command == 'X': self.command_holidays_in_crono(args)
            elif command == 'Y': self.command_union(args)
            elif command == 'Z': self.command_intersec(args)
            elif command == 'M': self.command_max_holidays(args)
            elif command == 'C': self.command_calendar(args)
            elif command == 'A': self.command_help()
            elif command == 'Q': break
            elif command == ' ': pass
            else: Util.error("Comando desconhecido.")
        Util.printf("Execução terminada.")

    def run(self: UI):
        self.interpreter()

def main():
    ui = UI()
    ui.run()

main()
