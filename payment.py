
def calculate_price(order):
    menu_prices = {
        "Burger": 5,
        "Pizza": 8,
        "Pasta": 7
    }
    
    if order in menu_prices:
        return menu_prices[order]
    else:
        print("Invalid order.")
        return 0

def process_payment(total_price):
    print(f"The total price is: ${total_price}")
    payment = float(input("Enter payment amount: $"))
    
    if payment >= total_price:
        print("Payment successful! Enjoy your food.")
    else:
        print("Insufficient funds. Please try again.")

if __name__ == "__main__":
    order = input("Enter your order (Burger, Pizza, Pasta): ")
    total_price = calculate_price(order)
    if total_price > 0:
        process_payment(total_price)
