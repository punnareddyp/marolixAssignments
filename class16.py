class Product:
    def __init__(self, name, price, quantity, inventory):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} costs {self.price} and has {self.quantity} units in stock."

    def sell(self, quantity):
        try:
            if quantity > self.inventory:
                raise ValueError(f"Only {self.inventory} units of {self.name} are available in stock.")
            else:
                self.quantity -= quantity
                self.inventory -= quantity
                print(f"{quantity} units of {self.name} sold successfully!")
        except ValueError as e:
            print(e)

    def add_inventory(self, quantity):
        self.inventory += quantity
        print(f"{quantity} units of {self.name} added to inventory.")

product = Product("Laptop", 50000, 10, 20)
print(product)

# Sell 5 units of Laptop
product.sell(4)

# Add 10 units of Laptop to inventory
product.add_inventory(10)

# Sell 15 units of Laptop
product.sell(15)