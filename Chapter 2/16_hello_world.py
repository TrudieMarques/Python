#This code reassigns the same variable a few times and prints it after each change — but there's a typo on the last line that will cause an error.

message = "Hello Python world!" 
print(message)                          # prints: Hello Python world!

message = "Hello Python Crash Course world!"
print(message)                          # prints: Hello Python Crash Course world!

message = "Hello Python Crash Course reader!"
print(mesage)                           # ERROR: 'mesage' is misspelled