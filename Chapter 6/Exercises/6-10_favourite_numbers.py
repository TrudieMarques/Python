favorite_numbers = {
    'jaden': [7, 8, 9],
    'priya': [13, 14,],
    'marcus': [42, 43, 44, 45],
    'elena': [3, 4, 5],
    'liam': [100, 101, 102, 103]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}:")
    for number in numbers:
        print(f" {number}")
