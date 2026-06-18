favourite_places = {
    "alice" : ["new york"],
    "bob" : ["botswana", "namibia"],
    "charlie" : ["kruger np", "cape town", "durban"]
    }

for name, places in favourite_places.items():
    print(f"\n{name.title()}:")
    for place in places:
        print(f"{place.title()}")

