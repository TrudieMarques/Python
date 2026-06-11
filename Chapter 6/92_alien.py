#Page 92 - A simple dictionary

#Dictionaries can be in one line OR
# alien_0 = {"colour" : "green", "points" : 5}

#one underneath the other
# alien_0 = {
#     "colour" : "green",
#     "points" : 5
#     }

# print(alien_0["colour"])
# print(alien_0["points"])



#Page 93 - Accessing Values in a dictionary

# alien_0 = {
#     "colour" : "green",
#     "points" : 5
#     }
# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")



#Page 93 - Adding new key-vaue pairs

# alien_0 = {
#     "colour" : "green",
#     "points" : 5
#     }

# print(alien_0)

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25

# print(alien_0)



#Page 94 - Starting with an empty dictionary

# alien_0 = {}

# alien_0["colour"] = "green"
# alien_0["points"] = 5

# print(alien_0)



#Page 94 - Modifying values in a dictionary

# alien_0 = {"colour" : "green"}
# print(f"The alien is {alien_0['colour']}")

# alien_0["colour"] = "yellow"
# print(f"The alien is {alien_0['colour']}")


#Page 95

# alien_0 = {"x_position" : 0,
#            "y_position" : 25,
#            "speed" : "medium"
#            }
# print(f"Original position: {alien_0['x_position']}")

# if alien_0["speed"] == "slow" :
#     x_increment = 1
# elif alien_0["speed"] == "medium" :
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0["x_position"] = alien_0["x_position"] + x_increment

# print(f"New position: {alien_0["x_position"]}")



#Page 96 - Removing key-value pairs !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)



#Page 97 - Using g() to access values

alien_0 = {
    'color': 'green',
    'speed': 'slow'
    }
#Test 1
# print(alien_0['points'])

#Test 2
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)