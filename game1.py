print("Welcome to Question Man!")
# print("Fntroduction")

print("\n")

print("First question:")

print("\n")

print("What colors are on the American flag?")

print("\n")

print("1) green, yellow, and black")
print("2) blue, pink, and purple")
print("3) red, white, and blue")

print("\n")

print("Please select a number:")

answer = input("Your answer:").strip().lower()

if answer == "3":
    print("Correct!")
else:
    print("Wrong, you have to climb Mount Everest!")
