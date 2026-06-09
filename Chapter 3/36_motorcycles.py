# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# # Modify the list by changing an item
# motorcycles[0] = "ducati"
# print(motorcycles)

# # Adding items to the end of the list using .append()
# motorcycles.append("ducati")
# print(motorcycles)

# motorcycles = []
# motorcycles.append("honda")
# print(motorcycles)
# motorcycles.append("yamaha")
# print(motorcycles)
# motorcycles.append("suzuki")
# print(motorcycles)


#Insert items into a list using .insert()
# motorcycles = ["honda", "yamaha", "suzuki"]
# motorcycles.insert(0, "ducati")
# motorcycles.insert(2, "test")
# print(motorcycles)

# # Removing an item using del statement
# del motorcycles[1]
# del motorcycles[1]
# print(motorcycles)

# # Removing an item using .pop() method
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# #Popping items from any position in a list
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Removing an Item by Value
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

