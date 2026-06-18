
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


# aliens = []
# for alien_number in range(30):
#     new_alien = {"colour" : "green", "points" : 5, "speed" : "slow"}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)

# print("...")

# print(f"\nTotal number of aliens: {len(aliens)}")


# aliens = []
# for alien_number in range(30):
#     new_alien = {"colour" : "green", "points" : 5, "speed" : "slow"}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien["colour"] == "green":
#         alien["colour"] = "yellow"
#         alien["speed"] = "medium"
#         alien["points"] = 10

# for alien in aliens[:5]:
#     print(alien)
# print("...")

aliens = []
for alien_number in range(30):
    new_alien = {"colour" : "green", "points" : 5, "speed" : "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["colour"] == "yellow":
        alien["colour"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:10]:
    print(alien)
print("...")