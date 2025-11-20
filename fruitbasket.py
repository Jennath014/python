
class FruitBasket:
    def __init__(self, fruit, price):
        self.fruit = fruit
        self.price = price

    def __add__(self, other):
        # Same fruit → pick the lowest-price basket
        if self.fruit == other.fruit:
            lowest_price = min(self.price, other.price)
            return FruitBasket(self.fruit, lowest_price)

        # Different fruits → return a new basket containing both fruits
        # Each fruit keeps its lowest available price from both baskets
        return [
            FruitBasket(self.fruit,
                        min(self.price, other.price)),
            FruitBasket(other.fruit,
                        min(self.price, other.price))
        ]

    def display(self):
        print(f"Fruit: {self.fruit}, Price per kg: {self.price}")


# --------------------- Testing ----------------------

b1 = FruitBasket("Apple", 150)
b2 = FruitBasket("Apple", 120)
b3 = FruitBasket("Mango", 180)

print("Same fruit:")
res1 = b1 + b2
res1.display()

print("\nDifferent fruits:")
res2 = b1 + b3
for fruit in res2:
    fruit.display()
