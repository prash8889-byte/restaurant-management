def display_menu(menu):
    print('='* 50)
    print(str.center("Welcome to the Restaurant!", 50))
    print('='* 50)
    print(str.center("View Menu", 50))
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
def take_order(menu):
    order = {}
    item = input("enter the item you want to order :").title()
    while item != "Done":
        if item in menu:
            quantity = int(input(f"How many {item}s would you like to order?"))
            if quantity <= 0:
                print("Invalid quantity. Please enter a positive number.")
            else:
                order[item] = quantity
        else:
            print(f"Sorry, {item} is not on the menu.")
        item = input("enter the item you want to order :").title()
    return order
def calculate_total(order, menu):
    total_bill = 0
    for item, quantity in order.items():
        total_bill += menu[item] * quantity
    return total_bill
def print_bill(menu, order, total_bill):
    discount = total_bill *0.1 
    if total_bill > 1000:
        discount = total_bill * 0.1
    else:
        discount = 0
    total_bill -= discount

    print('='* 20)
    print(str.center("order Summary", 20))
    print('='* 20)
    for item, quantity in order.items():
        print(f"{item} x {quantity} = ${menu[item] * quantity:.2f}")
    if discount > 0:
        print(f"Discount: -${discount:.2f}")
    print('='* 20)
    print(f"Total Bill: ${total_bill:.2f}")
def main():
    menu = {
        "Pizza": 12.99,
        "Burger": 8.99,
        "Pasta": 10.99,
        "Salad": 6.99,
        "Soda": 1.99
    }
    display_menu(menu)
    order = take_order(menu)
    total_bill = calculate_total(order, menu)
    print_bill(menu, order, total_bill)
main()

