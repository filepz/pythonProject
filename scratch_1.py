class Pizza:
    akcio = 1
    darab = 0

    def __init__(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price * self.akcio
        Pizza.darab = Pizza.darab + 1

    def __repr__(self):
        return f'Pizza({self.ingredients!r},{self.price})'

    def __str__(self):
        return self.ingredients + str(self.price)

    def learaz(self, percent):
        regiar = self.price
        ujar = regiar * percent
        self.price = ujar

    @classmethod
    def occso(cls):
        cls.akcio = 0.75


Margareta = Pizza("sajt, pari", 300)
Sonkas = Pizza("sonka,sajt", 500)
print(Margareta)
print(Sonkas.price)

akciosMargareta = Pizza("sajt, pari", 300)
print(akciosMargareta)
Margareta.learaz(0.5)
print(Margareta)
print(Pizza.darab)
