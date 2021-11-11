class PizzaDelivery:

    def __init__(self, name, price, ingredients = {}):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False


    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        for el, quant in self.ingredients.items():
            if ingredient == el:
                self.ingredients[el] += quantity
                self.price += price_per_quantity * quantity
                return self.price, self.ingredients

        self.ingredients[ingredient] = quantity
        self.price += price_per_quantity * quantity
        return self.price, self.ingredients


    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        for el, quant in self.ingredients.items():
            if el == ingredient:
                if quantity > quant:
                    return f'Please check again the desired quantity of {ingredient}!'
                elif quant >= quantity:
                    self.ingredients[el] -= quantity
                    self.price -= quantity * price_per_quantity
                    return self.price, self.ingredients
        return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'

    def make_order(self):
        self.ordered = True

        return f'You\'ve ordered pizza {self.name} prepared with {", ".join([x +": "+str(self.ingredients[x]) for x in self.ingredients.keys()])} and the price will be {self.price}lv.'




margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

