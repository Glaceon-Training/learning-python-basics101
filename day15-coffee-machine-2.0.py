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


def check_resources(orders_ingredients):
    """Check whether resources needed to make coffee is sufficient"""
    for item in orders_ingredients:
        if orders_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def coins_inserted():
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total


def process_coins(money_received, order_cost):
    if money_received >= order_cost:
        change = round(money_received - order_cost, 2)
        print(f"Here is ${change} in change")
        global income
        income += order_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def make_coffee(orders, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {orders} ☕️. Enjoy!")


def refill_resources(resources_items):
    for item in resources_items:
        if resources_items[item] == 0:
            if item == "water":
                resources_items[item] += 300
            elif item == "milk":
                resources_items[item] += 200
            else:
                resources_items[item] += 100


def get_report():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: ${income}")


income = 0
machine_is_running = True

while machine_is_running:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        machine_is_running = False
    elif order == "report":
        get_report()
    else:
        coffee = MENU[order]
        if check_resources(coffee["ingredients"]):
            payment = coins_inserted()
            if process_coins(payment, coffee["cost"]):
                make_coffee(order, coffee["ingredients"])
        refill_resources(resources)
