
def display_menu():
    print("Welcome to the Food Ordering System!")
    print("Menu:")
    print("1. Burger - $5")
    print("2. Pizza - $8")
    print("3. Pasta - $7")

def place_order():
    display_menu()
    choice = int(input("Enter the number of the item you want to order: "))
    
    if choice == 1:
        print("You ordered a Burger!")
        return "Burger"
    elif choice == 2:
        print("You ordered a Pizza!")
        return "Pizza"
    elif choice == 3:
        print("You ordered Pasta!")
        return "Pasta"
    else:
        print("Invalid choice, please try again.")
        return place_order()

if __name__ == "__main__":
    order = place_order()
    print(f"Your order is: {order}")
