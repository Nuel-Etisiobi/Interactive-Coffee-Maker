from menu_data import MENU, resources


# check if resources are sufficient
def is_sufficient(ingredients_order):
    """Return True if order can be made otherwise it returns False"""
    is_enough = True
    for item in ingredients_order:
        if ingredients_order[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}!")
            is_enough = False
    return is_enough


# process the money. For use case in Nigeria, the coin is purchased at the coffee shop using the naira currency
def process_coin():
    try:
        total = int(input("how many bronze? ")) * 25
        return total
    except ValueError:
        print("Please input an integer")
    

# check transaction to know if the money inserted is enough to buy the coffee otherwise refund
def check_transaction(price):
    try:
        if price > MENU[user_choice]["cost"]:
            change = round(price - MENU[user_choice]["cost"], 2)
            print(f"Here is ${change} dollars in change")
            return True
        else:
            print("Sorry that is not enough money. Money refunded. ")
    except TypeError:
        print("Please insert an integer")


# calculate the money inserted
def calculate_money(money):
    money = MENU[user_choice]["cost"]
    return money


# make coffee
def make_coffee(drink_name, ingredients_order):
    for item in ingredients_order:
        resources[item] = resources[item] - ingredients_order[item]
    return f"Here is your cup of {drink_name}. Enjoy!"


total_money = 0
machine_on = True

# Ask the user what they would like
while machine_on:
    user_choice = input(" What would you like? (espresso/latte/cappuccino) ")

    # Turn off machine with secret word off
    if user_choice == "off":
        machine_on = False

    # print report
    elif user_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {total_money}")
    else:
        drink = MENU[user_choice]
        if is_sufficient(drink["ingredients"]):
            total_money += calculate_money(total_money)
            payment = process_coin()
            print(f"the amount you paid: {payment}")
            if check_transaction(payment):
                print(make_coffee(user_choice, drink["ingredients"]))
