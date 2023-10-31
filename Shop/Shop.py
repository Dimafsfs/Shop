# Define a dictionary of menu items with prices in GBP
menu = {
    "Burger": 4.99,
    "Pizza": 6.99,
    "Fries": 1.99,
    "Soda": 0.99,
}
 
# Initialize an empty list to store the user's order
order = []
 
# Function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: £{price:.2f}")
 
# Function to take an order
def take_order():
    display_menu()
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ").capitalize()
        if item == 'Done':
            break
        elif item in menu:
            order.append(item)
        else:
            print("Invalid item. Please select from the menu.")
 
# Function to calculate the total cost of the order
def calculate_total(order):
    total = 0
    for item in order:
        total += menu[item]
    return total
 
# Function to display the order and the total cost
def display_order(order, total):
    print("Your order:")
    for item in order:
        print(item)
    print(f"Total: £{total:.2f}")
 
# Main program loop
while True:
    print("\nWelcome to the Food Ordering System!")
    take_order()
    total = calculate_total(order)
    display_order(order, total)
    order = []  # Reset the order for the next customer
    another_order = input("Place another order? (yes/no): ").lower()
    if another_order != "yes":
        break
 
print("Thank you for using the Food Ordering System. Have a great day!")