#Page 96 - Dictionary of similar objects

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'rust',
# 'phil': 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

#continue p99 - Looping through all key-value pairs in a dictionary


# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favourite language is {language.title()}.")




#P101 Looping through all the keys in a dictionary

# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages:
#     print(name.title())

# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(f"\nHi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")


# #Another example using keys() method

# if "erin" not in favorite_languages.keys():
#     print("Erin, please take our poll!")


#Looping through keys in particular order

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


#Looping through all values in a dictionary

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

#P109 - A list in a dictionary

favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c',],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell']
}


for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")