guests = ["elvis", "michael", "piet"]
print(guests)

print(f"Hi {guests[0].title()}, I found a bigger dinner table.")
print(f"Hi {guests[1].title()}, I found a bigger dinner table.")
print(f"Hi {guests[2].title()}, I found a bigger dinner table.")

guests.insert(0, "joice")
guests.insert(2, "jan")
guests.insert(4, "lisa")
print(guests)

print(f"Hi {guests[0].title()}, you are invited to dinner.")
print(f"Hi {guests[1].title()}, you are invited to dinner.")
print(f"Hi {guests[2].title()}, you are invited to dinner.")
print(f"Hi {guests[3].title()}, you are invited to dinner.")
print(f"Hi {guests[4].title()}, you are invited to dinner.")
print(f"Hi {guests[5].title()}, you are invited to dinner.")
