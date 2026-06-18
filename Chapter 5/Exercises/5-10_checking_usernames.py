current_users = ['Madelyn', 'John', 'Priya', 'Marcus', 'Elena']
new_users = ['JOHN', 'sofia', 'madelyn', 'liam', 'priya']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that username is taken. Please enter a new username.")
    else:
        print(f"Welcome {new_user}, you are now part of us")