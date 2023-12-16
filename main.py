from menu_data import MENU, resources


# TODO 4:check if resources are sufficient
def is_sufficient(ingredients_order):
    """Return True if order can be made otherwise it returns False"""
    is_enough = True
    for item in ingredients_order:
        if ingredients_order[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}!")
            is_enough = False
    return is_enough


# TODO 5 process the coins
def process_coin():
    print("Please insert coin: ")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


# TODO 6 check transaction
def check_transaction(price):
    if price > MENU[user_choice]["cost"]:
        change = round(price - MENU[user_choice]["cost"], 2)
        print(f"Here is ${change} dollars in change")
        return True
    else:
        print("Sorry that is not enough money. Money refunded. ")


# TODO 6 calculate money
def calculate_money(money):
    money = MENU[user_choice]["cost"]
    return money


# TODO 7 make coffee
def make_coffee(drink_name, ingredients_order):
    for item in ingredients_order:
        resources[item] = resources[item] - ingredients_order[item]
    return f"Here is your cup of {drink_name}. Enjoy!"


total_money = 0
machine_on = True

# TODO: 1 Ask the user what they would like
while machine_on:
    user_choice = input(" What would you like? (espresso/latte/cappuccino) ")

    # TODO 2 Turn off machine with secret word off
    if user_choice == "off":
        machine_on = False

    # TODO 3 print report
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
