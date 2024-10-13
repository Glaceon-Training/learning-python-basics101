MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(orders):
    if orders == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"]:
            if MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False

    if orders == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"]:
            if MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
                if MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]:
                    return True
                else:
                    print("Sorry there is not enough coffee.")
                    return False

            else:
                print("Sorry there is not enough milk.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False

    if orders == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"]:
            if MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
                if MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
                    return True
                else:
                    print("Sorry there is not enough coffee.")
                    return False
            else:
                print("Sorry there is not enough milk.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False


def calculate_change(orders, quarters, dimes, nickles, pennies):
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01

    coin_inserted = (quarters * quarter) + (dimes * dime) + (nickles * nickle) + (pennies * penny)

    if orders == "espresso":
        if coin_inserted >= MENU["espresso"]["cost"]:
            change = round(coin_inserted - MENU["espresso"]["cost"], 2)
            return change
        else:
            return False
    elif orders == "latte":
        if coin_inserted >= MENU["latte"]["cost"]:
            change = round(coin_inserted - MENU["latte"]["cost"], 2)
            return change
        else:
            return False
    elif orders == "cappuccino":
        if coin_inserted >= MENU["cappuccino"]["cost"]:
            change = round(coin_inserted - MENU["cappuccino"]["cost"], 2)
            return change
        else:
            return False


def calculate_income(orders, moneys):
    if orders == "espresso":
        moneys += MENU["espresso"]["cost"]
    elif orders == "latte":
        moneys += MENU["latte"]["cost"]
    elif orders == "cappuccino":
        moneys += MENU["cappuccino"]["cost"]

    return moneys


def resource_subtraction(orders):
    if orders == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    elif orders == "latte":
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
    elif orders == "cappuccino":
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]


def get_report():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: ${money}")


money = 0
machine_is_running = True

while machine_is_running:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        get_report()
        machine_is_running = False
    else:
        resource_checking = check_resources(order)
        if resource_checking is not False:
            print("Please insert coin.")

            quarter_coin = int(input("how many quarters?: "))
            dime_coin = int(input("how many dimes?: "))
            nickle_coin = int(input("how many nickles?: "))
            penny_coin = int(input("how many pennies?: "))

            changes = calculate_change(order, quarter_coin, dime_coin, nickle_coin, penny_coin)
            if changes is not False:
                print(f"Here is ${changes} in change.")
                print(f"Here is your {order}. Enjoy!")
                money = calculate_income(order, money)
                resource_subtraction(order)
            else:
                print("Sorry that's not enough money. Money refunded.")
                machine_is_running = False

        else:
            machine_is_running = False
