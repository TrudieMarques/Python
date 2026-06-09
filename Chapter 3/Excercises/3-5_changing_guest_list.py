guests = ["elvis", "sarah", "piet"]
print(guests[1].title())

guests[1] = "michael"
print(guests)

print(f"Hi {guests[0].title()}, you are invited to dinner.")
print(f"Hi {guests[1].title()}, you are invited to dinner.")
print(f"Hi {guests[2].title()}, you are invited to dinner.")