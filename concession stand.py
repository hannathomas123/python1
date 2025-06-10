menu = {"pizza" : 5.00,
        "burger" : 15.00,
        "popcorn": 8.00,
        "lime juice" : 5.00,
        "mango juice" : 4.00}

cart = []
total = 0

for key,value in menu.items():
        print(f"{key:13} : {value:.2f}")


while True:
        food =  input("select the food item (q to quit):").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

for food in cart:
        total += menu.get(food)
        print(food, end=" ")

print()
print(f"Total price is: ${total}")
