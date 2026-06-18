cities = {
    "pretoria" : {
        "country" : "south africa",
        "approx_pop" : "3.29 million",
        "fact" : "admin capital"
    },
    "new york" : {
        "country" : "usa",
        "approx_pop" : "20 million",
        "fact" : "very windy"
    },
    "dublin" : {
        "country" : "ireland",
        "approx_pop" : "1.3 million",
        "fact" : "has over 770 pubs"
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f" Country: {info["country"].title()}")
    print(f" Approx population: {info["approx_pop"].title()}")
    print(f" Fact: {info["fact"].title()}")