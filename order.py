from drink import Drink

class Order:
    def __init__(self): # Initialize order with an empty list
        self.items = []
    
    # Add drink to the order
    def add_item(self, drink): 
        self.items.append(drink)
        print(f"Added {drink.name} to your order.")

    # Remove drink from the order
    def remove_item(self, drink): 
        if drink in self.items:
            self.items.remove(drink)
            print(f"Removed {drink.name} from your order.")
        else:
            print(f"{drink.name} is not in your order.")
    
    # Calculate total price of the order
    def total(self):
        return sum(item.get_total_price() for item in self.items)

    # Order a single drink
    def order_single_drink(self):
        """Guide the user through building a single drink and add it to the order."""
        print("\n--- STARTING ORDER ---")

        # Step 1: Choose drink
        print("Available drinks:")
        from menu import drink_menu
        for i, drink_name in enumerate(drink_menu.keys(), 1):
            prices = drink_menu[drink_name]
            print(f"{i}. {drink_name} - M: ${prices['M']:.2f}, L: ${prices['L']:.2f}")

        # Drink selection with validation
        while True:
            try:
                drink_choice = int(input(f"Please select a drink (1-{len(drink_menu)}): "))
                drink_names = list(drink_menu.keys())
                if 1 <= drink_choice <= len(drink_menu):
                    selected_drink_name = drink_names[drink_choice - 1]
                    print(f"Selected drink: {selected_drink_name}")
                    break
                else:
                    print(f"Invalid drink choice. Please enter 1-{len(drink_menu)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Step 2: Choose size
        while True:
            size_choice = input("Would you like that in a (Medium) or a (Large)? (M/L): ").strip().upper()
            if size_choice in ["M", "L"]:
                print(f"Selected size: {size_choice}")
                break
            else:
                print("Invalid size choice. Please enter M or L.")

        # Step 3: Choose temperature
        while True:
            temp_choice = input("Would you like that (Hot) or (Iced)?: ").strip().title()
            if temp_choice in ["Hot", "Iced"]:
                print(f"Selected temperature: {temp_choice}")
                break
            else:
                print("Invalid temperature choice. Please enter Hot or Iced.")

        # Create the drink
        drink = Drink(selected_drink_name, size_choice)
        drink.set_temperature(temp_choice)

        # Step 4: Add toppings
        from menu import toppings_menu
        print("\nAvailable toppings:")
        for topping_name, price in toppings_menu.items():
            print(f"• {topping_name} - ${price:.2f}")

        # Ask if they want to add toppings
        while True:
            add_toppings = input("Would you like to add any toppings? (y/n): ").strip().lower()
            if add_toppings in ['y', 'yes']:
                while True:
                    topping_choice = input("Enter topping name (or 'done' to finish): ").strip()
                    if topping_choice.lower() == 'done':
                        break
                    # Case-insensitive search
                    found_topping = None
                    for menu_topping in toppings_menu.keys():
                        if menu_topping.lower() == topping_choice.lower():
                            found_topping = menu_topping
                            break

                    if found_topping:
                        if drink.add_topping(found_topping, toppings_menu[found_topping]):
                            print(f"Added {found_topping}")
                        # If add_topping returns False, it's already added
                    else:
                        print("Topping not found. Please try again.")
                break
            elif add_toppings in ['n', 'no']:
                break
            else:
                print("Invalid input. Please enter y/n.")

        # Add to order
        self.add_item(drink)

        # Show drink summary
        size_display = "Large" if drink.size == "L" else "Medium"
        temp_display = drink.temperature
        toppings_display = f" w/ {', '.join(drink.toppings)}" if drink.toppings else ""
        print(f"\n[{size_display} {temp_display} {drink.name}{toppings_display}]")
        print(f"\nOrder updated! Current Total: ${self.total():.2f}")

    def start_ordering(self):
        """Handle the complete ordering process; supports adding multiple drinks."""
        while True:
            # Build one drink and add to order
            self.order_single_drink()

            # Ask if user wants to order more
            while True:
                order_more = input("\nWould you like to order anything else? (y/n): ").strip().lower()

                if order_more in ('y', 'yes'):
                    print("\n" + "-"*50)
                    print("ORDERING NEXT DRINK")
                    print("-"*50)
                    break  # break inner loop to add another drink in the outer loop

                elif order_more in ('n', 'no'):
                    print("\n" + "-"*50)
                    print("CURRENT ORDER")
                    print("-"*50)
                    self.show_order()

                    # Show order management options
                    while True:
                        print("\n" + "-"*50)
                        print("ORDER MANAGEMENT")
                        print("-"*50)
                        print("1. View order")
                        print("2. Add to order")
                        print("3. Adjust drink/topping")
                        print("4. Remove drink")
                        print("5. Checkout")

                        choice = input("Select an option (1-5): ").strip()

                        if choice == "1":
                            print("\n" + "-"*50)
                            print("CURRENT ORDER")
                            print("-"*50)
                            self.show_order()
                            input("\nPress Enter to continue...")

                        elif choice == "2":
                            print("\n" + "-"*50)
                            print("ADDING TO ORDER")
                            print("-"*50)
                            self.order_single_drink()
                            # after adding, return to management menu
                            continue

                        elif choice == "3":
                            print("\n" + "-"*50)
                            print("ADJUST DRINK/TOPPING")
                            print("-"*50)
                            self.modify_order()

                        elif choice == "4":
                            print("\n" + "-"*50)
                            print("REMOVE DRINK")
                            print("-"*50)
                            self.remove_from_order()

                        elif choice == "5":
                            print("\n" + "-"*50)
                            print("PROCEEDING TO CHECKOUT")
                            print("-"*50)
                            checkout_result = self.checkout()
                            if checkout_result == "cancelled":
                                continue  # back to management menu
                            else:
                                # Successful checkout; leave ordering entirely
                                return

                        else:
                            print("Invalid choice. Please enter 1-5.")

                else:
                    print("Please enter 'y' or 'n'.")
                    continue

    # Modify existing drinks in the order
    def modify_order(self):
        """Allow users to modify existing drinks in their order"""
        if not self.items:
            print("No items in order to modify.")
            input("Press Enter to continue...")
            return
        
        print("Current order:")
        self.show_order()
        
        try:
            drink_num = int(input("Enter the number of the drink to modify (1-{}): ".format(len(self.items))))
            if 1 <= drink_num <= len(self.items):
                drink = self.items[drink_num - 1]
                print(f"Modifying: {drink}")
                
                # Show modification options
                print("\nWhat would you like to change?")
                print("1. Size")
                print("2. Temperature")
                print("3. Toppings")
                
                mod_choice = input("Select option (1-3): ").strip()
                change_made = False
                
                if mod_choice == "1":
                    while True:
                        new_size = input("New size (M/L): ").upper()
                        if new_size in ["M", "L"]:
                            drink.set_size(new_size)
                            print(f"Size changed to {new_size}")
                            change_made = True
                            break
                        else:
                            print("Invalid size. Please enter M or L.")
                
                elif mod_choice == "2":
                    while True:
                        new_temp = input("New temperature (Hot/Iced): ").title()
                        if new_temp in ["Hot", "Iced"]:
                            drink.set_temperature(new_temp)
                            print(f"Temperature changed to {new_temp}")
                            change_made = True
                            break
                        else:
                            print("Invalid temperature. Please enter Hot or Iced.")
                
                elif mod_choice == "3":
                    print("Current toppings:", ", ".join(drink.toppings) if drink.toppings else "None")
                    action = input("Add (a) or remove (r) toppings? ").strip().lower()
                    
                    if action == "a":
                        from menu import toppings_menu
                        print("Available toppings:")
                        for topping_name, price in toppings_menu.items():
                            print(f"• {topping_name} - ${price:.2f}")
                        
                        topping_name = input("Enter topping name: ").strip()
                        # Case-insensitive search
                        found_topping = None
                        for menu_topping in toppings_menu.keys():
                            if menu_topping.lower() == topping_name.lower():
                                found_topping = menu_topping
                                break
                        
                        if found_topping:
                            if drink.add_topping(found_topping, toppings_menu[found_topping]):
                                print(f"Added {found_topping}")
                                change_made = True
                            # If add_topping returns False, it's already added
                        else:
                            print("Topping not found.")
                    
                    elif action == "r":
                        if drink.toppings:
                            print("Current toppings:", ", ".join(drink.toppings))
                            topping_to_remove = input("Enter topping name to remove: ").strip()
                            # Case-insensitive match against existing toppings
                            canonical_remove = None
                            for existing in drink.toppings:
                                if existing.lower() == topping_to_remove.lower():
                                    canonical_remove = existing
                                    break
                            if canonical_remove is not None:
                                drink.remove_topping(canonical_remove)
                                print(f"Removed {canonical_remove}")
                                change_made = True
                            else:
                                print("Topping not found in drink.")
                        else:
                            print("No toppings to remove.")
                    
                    else:
                        print("Invalid choice.")
                
                else:
                    print("Invalid choice.")
                
                if change_made:
                    print("Drink modified successfully!")
                else:
                    print("No changes made.")
            else:
                print("Invalid drink number.")
        except ValueError:
            print("Please enter a valid number.")
        
        # Return to order management
        input("\nPress Enter to continue...")

    def remove_from_order(self):
        """Allow users to remove drinks from their order"""
        if not self.items:
            print("No items in order to remove.")
            input("Press Enter to continue...")
            return
        
        print("Current order:")
        self.show_order()
        
        try:
            drink_num = int(input("Enter the number of the drink to remove (1-{}): ".format(len(self.items))))
            if 1 <= drink_num <= len(self.items):
                drink = self.items[drink_num - 1]
                self.remove_item(drink)
            else:
                print("Invalid drink number.")
        except ValueError:
            print("Please enter a valid number.")

        # Return to order management
        input("\nPress Enter to continue...")

    # Show order summary
    def show_order(self): 
        if not self.items:
            print("No items in order.")
            return
        else:
            for i, item in enumerate(self.items, 1):
                # Format drink display with size, temperature, and toppings
                size_display = "Large" if item.size == "L" else "Medium"
                temp_display = item.temperature
                toppings_display = f" w/ {', '.join(item.toppings)}" if item.toppings else ""
                print(f"{i}. {size_display} {temp_display} {item.name}{toppings_display} - ${item.get_total_price():.2f}")
            print(f"Total: ${self.total():.2f}\n")

    # Handle check out process
    def checkout(self):  
        if not self.items:
            print("Order is empty")
            input("Press Enter to continue...")
            return "cancelled"
        self.show_order()

        while True: # Checks user input
            confirm = input("Proceed to checkout? (y/n) ").strip().lower()
            if confirm in ('yes', 'y'):
                print("\n" + "-"*50)
                print("ORDER CONFIRMED")
                print("-"*50)
                print("Here are your drinks:")
                for i, drink in enumerate(self.items, 1):
                    size_display = "Large" if drink.size == "L" else "Medium"
                    temp_display = drink.temperature
                    toppings_display = f" w/ {', '.join(drink.toppings)}" if drink.toppings else ""
                    print(f" {i}. {size_display} {temp_display} {drink.name}{toppings_display}")
                print("\nEnjoy, Thank you for coming. Hope to see you again!!\n")
                self.items.clear()
                return True
            if confirm in ('no', 'n'):
                print("Checkout cancelled. Returning to order management...")
                return "cancelled"
            print("Please enter 'y' or 'n'.")
