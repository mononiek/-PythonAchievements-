#Maak een programma met daarin de volgende 2 lijsten:

#GroceryList
#ShoppingCart

#Vul beide lijsten met boodschappen (strings). Bijvoorbeeld: "Milk", "Cheese", "Sausage", etc.

#Vergelijk met behulp van loops de inhoud van beide lijsten met elkaar.

#Als de lijsten overeenkomen geeft je programma het bericht: "Done shopping"

#Zo niet: "Continue Shopping"

#Hier begint de code.

import time

print("Ohw HI!\n I'm going to do groceries right now\n And this is my grocery list:")

time.sleep(1)

Grocerylist = {"pasta", "chocolate", "Brocoli", "chicken", "cookies"}
print(Grocerylist)

time.sleep(1)

print("I'm only in a bit of a hurry so I'm gonna get started and try to find everthing.\n I'll keep you updated!")

time.sleep(1)

Shoppingcart = {"pasta", "chocolate", "Brocoli", "chicken", "cookies"}


lenghtGrocerylist = 0

for product in Grocerylist:
    lenghtGrocerylist += 1
    print("Continue Shopping")


if (lenghtGrocerylist == 5):
    print("Done shopping")
    print("Ok. I'm done shopping now. \nSee you next time!")
        
