my_pizzas = ["chicken", "mince", "feta"]
friend_pizzas = my_pizzas[:]

print(friend_pizzas)

my_pizzas.append("bacon")
friend_pizzas.append("vegetarian")


print(f"My facourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print(f"\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)