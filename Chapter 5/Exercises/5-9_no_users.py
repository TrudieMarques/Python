# usernames = ["sarah", "john", "admin", "peter", "zoe", "andrew"]

# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print(f"Hello {username.title()}, thank you for logging in again.")
# else:
#     print("We need to find some users!")


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")