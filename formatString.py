#Hello John Doe. Your current balance is $53.44.


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % (data[0],data[1],data[2]))
