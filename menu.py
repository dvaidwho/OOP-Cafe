# Menu data
drink_menu = {
    "Signature OOP Coffee": {"M": 3.75, "L": 5.00},
    "Vietnamese Coffee": {"M": 3.75, "L": 5.00},
    "Matcha Latte": {"M": 4.75, "L": 6.00},
    "Black Milk Tea": {"M": 3.50, "L": 4.75},
    "Honey Green Tea": {"M": 3.50, "L": 4.75},
}

toppings_menu = {
    "Tapioca Pearls": 0.75,
    "Milk Foam": 0.75,
    "Lavender Foam": 1.00,
    "Matcha Milk Foam": 1.00,
}

# Function to display the menu
def display_menu():
    print(r"""
        {   {   }
         }_{ __{
     .-{   }   }-.
    (   }     {   )
    |`-.._____..-'|
    |             ;--.
    |            (__  \
    |             | )  )
    |             |/  /
    |             /  /    --- Welcome to OOP Cafe! ---
    |            (  /
    \             y'
     `-.._____..-'

    ascii art credit - Felix Lee.
    """)
    
    print("-" * 100)
    print(f"{'DRINK MENU':<60}{'TOPPINGS':<40}")
    print("-" * 100)
    
    # Display drinks and toppings side by side
    for i in range(len(drink_menu)):
        drink_name = list(drink_menu.keys())[i]
        drink_prices = list(drink_menu.values())[i]
        drink_line = f"• {drink_name} M: ${drink_prices['M']:.2f}, L: ${drink_prices['L']:.2f}"
        
        # Add topping if available at this index
        topping_line = ""
        if i < len(toppings_menu):
            topping_name = list(toppings_menu.keys())[i]
            topping_price = list(toppings_menu.values())[i]
            topping_line = f"• {topping_name} - ${topping_price:.2f}"
        
        print(f"{drink_line:<60}{topping_line:<40}")
    
    # Display remaining toppings if any
    for i in range(len(drink_menu), len(toppings_menu)):
        topping_name = list(toppings_menu.keys())[i]
        topping_price = list(toppings_menu.values())[i]
        topping_line = f"• {topping_name} - ${topping_price:.2f}"
        print(f"{'':<60}{topping_line:<40}")
    
    print("-" * 100)
    print("1. Order")
    print("2. Exit.")

    

