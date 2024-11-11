from __future__ import annotations

class Ingredient:
    def __init__(self: Ingredient, name: str, percent: float):
        """ Initialize an ingredient. """
        self.name = name
        self.percent = percent

class CakeVariety:
    def __init__(self: CakeVariety, name: str, amount: int, ingredients: list[Ingredient]):
        """ Initialize a cake variety. """
        self.name = name
        self.amount = amount
        self.ingredients = tuple(ingredients)
    
    def main_ingredient(self: CakeVariety) -> Ingredient:
        """ Get the main ingredient of the recipe of a cake variety. """
        if len(self.ingredients) == 0: return None
        mi = Ingredient('', 0)
        for i in self.ingredients:
            if i.percent > mi.percent:
                mi.name, mi.percent = i.name, i.percent
        return mi
    
    def sell(self: CakeVariety, units: int) -> int:
        """ Sell some units. """
        a = self.amount
        self.amount = 0 if units > self.amount else self.amount - units
        return (a if units > a else units)

class CakeShop:
    def __init__(self: CakeShop, stock: list[CakeVariety]):
        """ Initialize a cake shop. """
        self.stock = stock
    
    def size(self: CakeShop) -> int:
        """ Number of cake varieties in the shop. """
        return len(self.stock)
    
    def find_variety(self: CakeShop, vname: str) -> CakeVariety:
        """ Find a cake variety by name. """
        return (next((c for c in self.stock if vname == c.name), None))
   
    def sell(self: CakeShop, vname: str, units: int) -> int:
        """ Sell some units of a named cake variety. """
        if self.find_variety(vname) == None:
            return None
        return self.find_variety(vname).sell(units)

class UI:   # User Interface.
    END_MARK = "fim"
    
    def __init__(self: UI):
        """ Read a shop and store it. The UI will need to deal with the shop. """
        self.shop = self.input_shop()
    
    def make_ingredient(self: UI, line: str) -> Ingredient:
        """ Create an ingredient from an input line. """
        name, percentage = line.split()
        return Ingredient(name, float(percentage))
    
    def make_cake_variety(self: UI, line: str) -> CakeVariety:
        """ Create a cake variety ingredient from an input line plus ingredient lines. """
        name, amount, n_ingredients = line.split()
        n_ingredients = int(n_ingredients)
        l = []
        for _ in range(n_ingredients):
            line = input()    # ingredient line
            ingr = self.make_ingredient(line)
            l.append(ingr)
        return CakeVariety(name, int(amount), l)
    
    def input_shop(self: UI) -> CakeShop:
        """ Fill the UI's own shop with data form the input. """
        l = []
        while True:
            line = input()
            if line == UI.END_MARK:
                break
            cake = self.make_cake_variety(line)
            l.append(cake)
        return CakeShop(l)
    
    def process(self: UI, name: str, units: int):
        """ User interface for selling of some units of a cake variety. """
        sold = self.shop.sell(name, units)
        print(f'Vendidas 0 unidades de {name}') if sold == None else print(f'Vendidas {sold} unidades de {name}')
        if sold != None: print(f'Ingrediente principal: {self.shop.find_variety(name).main_ingredient().name}')

    
    def run(self: UI):
        """ Run the user interface. """
        name = input("BOLO: ")            # pergunta o nome do bolo
        units = int(input("UNIDADES: "))  # pergunta a quantidade
        self.process(name, units)         # processa o pedido

def main():
    ui = UI()
    ui.run()

main()