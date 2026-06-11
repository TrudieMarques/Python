#Checking for Inequaltiy

# requested_topping = "mushrooms"

# if requested_topping != "anchovies":
#     print("Hold the anchovies!")



#Page 82

# requested_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms.")
# if "pepperoni" in requested_toppings:
#     print("Adding pepperoni.")
# if "extra cheese" in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")



#Page 85 - Checking for special items

# requested_toppings = ["mushrooms", "green peppers","extra cheese"]

# for topping in requested_toppings:
#     print(f"Adding {topping}.")

# print("\nFnished making your pizza!")



#Page 86 - Checking for special items with 'if' statement

# requested_toppings = ["mushrooms", "green peppers","extra cheese"]

# for topping in requested_toppings:
#     if topping == "green peppers":
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {topping}.")

# print("\nFnished making your pizza!")



#Page 86 - Checking that a list is not empty

# #Test 1
# requested_toppings = []

# #Test 2
# # requested_toppings = ["mushrooms", "ham"]

# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping}.")
#     print("\nFinished making your pizza!")
       
# else:
#     print(f"Are you sure you want a plain pizza?")



#Page 87 - Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
