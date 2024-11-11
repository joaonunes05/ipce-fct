from __future__ import annotations

class Rational:
    def __init__(self: Rational, num: int, den: int):
        """ Initialize a rational number.
            Precondition: den != 0
        """
        self.num = num
        self.den = den
        self.simplify()
    
    @staticmethod
    def gcd(m: int, n: int) -> int:
        """ Greatest common divisor. Used the Euclidean algorithm. """
        x = abs(m)  # ignoring the signs
        y = abs(n)
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x
    
    def simplify(self: Rational):
        """ Simplify the rational number. """
        div = self.gcd(self.num, self.den)
        self.num //= div
        self.den //= div
        if self.den <0: self.num, self.den = -self.num, -self.den
    
    def __str__(self: Rational) -> str:
        """ Convert to string. """
        return f"{self.num}/{self.den}"
    
    def __add__(self: Rational, other: Rational) -> Rational:
        """ Add two rational numbers. """
        result = Rational(self.num * other.den + other.num * self.den, self.den * other.den) 
        result.simplify()
        return result
    
    def __sub__(self: Rational, other: Rational) -> Rational:
        """ Subtract two rational numbers. """
        result = Rational(self.num * other.den - other.num * self.den, self.den * other.den) 
        result.simplify()
        return result
    
    def __mul__(self: Rational, other: Rational) -> Rational:
        """ Multiply two rational numbers. """
        result = Rational(self.num * other.num, self.den * other.den)
        result.simplify()
        return result
    
    def __truediv__(self: Rational, other: Rational) -> Rational:
        """ Divide two rational numbers. """
        result = Rational(self.num * other.den, self.den * other.num)
        result.simplify()
        return result

class UI:   # User Interface
    def make_rational(self: UI, s: str) -> Rational:
        """ Create a rational number from the format: 'n/d'. """
        n,d = s.split('/')
        return Rational(int(n), int(d))
    
    def process_input(self: UI, s: str) -> (Rational, str, Rational):
        """ Process the format: 'n/d op n/d'. """
        r1, op, r2 = s.split()
        x = self.make_rational(r1)
        y = self.make_rational(r2)
        return (x, op, y)
    
    def eval_input(self: UI, s: str) -> Rational:
        """ Decode the input and perform the operation. """
        x, op, y = self.process_input(s)
        if op == '+':
            return x+y
        elif op == '-':
            return x-y
        elif op == '*':
            return x*y
        elif op == '/':
            return x/y
        else:
            return None
    
    def run(self: UI):
        s = input("A/B OP C/D: ")
        print(self.eval_input(s))

def main():
    ui = UI()
    ui.run()

main()