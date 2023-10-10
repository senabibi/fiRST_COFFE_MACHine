from menu import MENU,resources,logo
import os
is_off=False
profit=0
def make_coffee(chosen_drink,order_ingredients):
    for ingrediens in order_ingredients:
        resources[ingrediens]==order_ingredients[ingrediens]
    print(f"Her is your {chosen_drink}☕")    

def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient]>=resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True 

def process_coins():
    print("Please insert coins")
    total=int(input("How many quarters?:"))*0.25
    total+=int(input("How many dimes?:"))*.1
    total+=int(input("How many nickles?:"))*.05
    total+=int(input("How many pennies?:"))*.01
    return total
def check_money(payment,drink_cost):  
    global profit  
    if payment>=drink_cost:
        money_back=round(payment-drink_cost,2)
        print(f"Here is ${money_back} in change.")
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money .Monet refunded.")
        return False    

while not is_off:
    print(logo)
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_off=True
        os.system('cls')
    elif choice=="report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")   
    else:
        chosen_drink=MENU[choice]
        if check_resources(chosen_drink["ingredients"]):
            payment=process_coins()
            if check_money(payment,chosen_drink["cost"]):
                make_coffee(choice,chosen_drink["ingredients"])




        
