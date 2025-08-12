class Drink:
    def __init__(self, name: str, size: str): 
        self.name = name
        self.size = size  # M or L
        self.temperature = "Iced"  # Default temperature
        self.toppings = []
        self.topping_prices = {}

    # Set the size of the drink
    def set_size(self, size):
        if size in ["M", "L"]:
            self.size = size
        else:
            raise ValueError("Size must be 'M' or 'L'")

    # Set the temperature of the drink
    def set_temperature(self, temp):
        if temp in ["Hot", "Iced"]:
            self.temperature = temp
        else:
            raise ValueError("Temperature must be 'Hot' or 'Iced'")

    # Add a topping to the drink
    def add_topping(self, topping_name, topping_price):
        """Add a topping to the drink"""
        if topping_name not in self.toppings:  # Prevent duplicates
            self.toppings.append(topping_name)
            self.topping_prices[topping_name] = topping_price
            return True
        else:
            print(f"{topping_name} is already added to this drink.")
            return False

    # Remove a topping from the drink
    def remove_topping(self, topping_name):
        """Remove a topping from the drink"""
        if topping_name in self.toppings:
            self.toppings.remove(topping_name)
            del self.topping_prices[topping_name]
            return True
        else:
            print(f"{topping_name} is not in this drink.")
            return False
        
    # Get base price from menu based on drink name and size
    def get_total_price(self):
        from menu import drink_menu
        base_price = drink_menu[self.name][self.size]
        
        return base_price + sum(self.topping_prices.values())

    def __str__(self): # What the user sees when they print the object
            toppings_str = f" + {', '.join(self.toppings)}" if self.toppings else ""
            return f"{self.name}{toppings_str} - ${self.get_total_price():.2f}"
        
    def __repr__(self): # What the developer sees when they print the object
            return f"Drink(name={self.name}, size={self.size}, temperature={self.temperature}, toppings={self.toppings})"
        