age = input("How old are you?\n")

decades = int(age) // 10
years = int(age) % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old.")