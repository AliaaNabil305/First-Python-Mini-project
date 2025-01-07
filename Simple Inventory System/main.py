class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_product_info(self):
        """Displays the product's name, price, and available quantity."""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity Available: {self.quantity}")
    
    def update_quantity(self, quantity_change):
        """Updates the quantity of the product when sold or restocked.
        A positive value increases the quantity (restock), while a negative value decreases it (sale).
        """
        if self.quantity + quantity_change >= 0:
            self.quantity += quantity_change
            action = "restocked" if quantity_change > 0 else "sold"
            print(f"Product '{self.name}' has been {action} by {abs(quantity_change)} units.")
        else:
            print(f"Insufficient quantity for '{self.name}' to complete the operation.")
    
    def calculate_product_value(self):
        """Calculates the total value of the product in the inventory (price * quantity)."""
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        """Adds a new product to the inventory."""
        self.products.append(product)
    
    def display_all_products(self):
        """Displays information about all products in the inventory."""
        for product in self.products:
            product.display_product_info()
            print()
    
    def calculate_inventory_value(self):
        """Calculates the total value of the inventory (sum of all product values)."""
        total_value = sum(product.calculate_product_value() for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}")


inventory = Inventory()

product1 = Product("Laptop", 1200.00, 10)
inventory.add_product(product1)

product2 = Product("Smartphone", 800.00, 20)
inventory.add_product(product2)

print("Inventory Details:")
inventory.display_all_products()

product1.update_quantity(-3)
product2.update_quantity(5)  

print("Updated Inventory Details:")
inventory.display_all_products()

inventory.calculate_inventory_value()
