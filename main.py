import sys
from order import Order
from menu import display_menu

# Display the menu
display_menu()

# Main loop to handle user input
while True:
    choice1 = input("Enter your choice (1 or 2): ").strip()
    if choice1 == "1":
        order = Order()
        order.start_ordering()
        # Ask if they want to start a new session
        while True:
            new_session = input("\nWould you like to start a new order session? (y/n): ").strip().lower()
            if new_session in ['n', 'no']:
                print("Thank you, Goodbye!")
                sys.exit(0)
            elif new_session in ['y', 'yes']:
                display_menu()
                break
            else:
                print("Please enter 'y' or 'n'.")
    elif choice1 == "2":
        print("Thank you, Goodbye!")
        break
    else:
        print("Invalid input, please type 1 or 2.")
