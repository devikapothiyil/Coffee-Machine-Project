#This is the code of implementing  coffee machine project without using oop concepts
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
def espresso(cash_debited,account):
    if MENU["espresso"]["ingredients"]["water"]<=resources["water"]:
        if MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            if cash_debited< MENU["espresso"]["cost"]:
                print("Sorry,Insufficient Amount!!")
            else:
                print("Here is your ESPRESSO :)\n Balance:",cash_debited-MENU["espresso"]["cost"])
                resources["water"]-=50
                resources["coffee"]-=18
                account += MENU["espresso"]["cost"]
        else:
            print("Sorry,There is no enough Coffee powder")
    else:
        print("Sorry,There is no enough Water")
    return account

def latte(cash_debited,account):
    if MENU["latte"]["ingredients"]["water"]<=resources["water"]:
        if MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]:
            if MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
                if cash_debited < MENU["latte"]["cost"]:
                    print("Sorry,Insufficient Amount!!")
                else:
                    print("Here is your LATTE :)\n Balance:", cash_debited - MENU["latte"]["cost"])
                    resources["water"] -= 200
                    resources["coffee"] -= 24
                    resources["milk"]-=150
                    account += MENU["latte"]["cost"]
            else:
                print("Sorry,There is no enough Milk")
        else:
            print("Sorry,There is no enough Coffee powder")
    else:
        print("Sorry,There is no enough Water")
    return account
def cappuccino(cash_debited,account):
    if MENU["cappuccino"]["ingredients"]["water"]<=resources["water"]:
        if MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
            if MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
                if cash_debited < MENU["cappuccino"]["cost"]:
                    print("Sorry,Insufficient Amount!!")
                else:
                    print("Here is your CAPPUCCINO :)\n Balance:", cash_debited - MENU["cappuccino"]["cost"])
                    resources["water"] -= 250
                    resources["coffee"] -= 24
                    resources["milk"] -= 100
                    account += MENU["cappuccino"]["cost"]
            else:
                print("Sorry,There is no enough Milk")
        else:
            print("Sorry,There is no enough Coffee powder")
    else:
        print("Sorry,There is no enough Water")
    return account
more_customer=True
money=0
while more_customer==True:
    select=input("What would you like?[espresso,latte,cappuccino]:\n").lower()

    if select == "report":
        for key,value in resources.items():
            print(f"{key}:{value}")
        print(f"Money:{money}")
    else:
        cash = int(input("Enter the money you have:"))
        if select=="espresso":
            money=espresso(cash,money)
        elif select=="latte":
            money=latte(cash,money)
        elif select=="cappuccino":
            money=cappuccino(cash,money)
        else:
            print("Please enter an item from the menu!!")
    customers_left=input("Is there any more customers left?Type yes/no").lower()
    if customers_left=="no":
        more_customer=False
