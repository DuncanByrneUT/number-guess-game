import random

# grabbing the range from 1 (-1) to 100 (101)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please use a number larger than 0")
        quit()
else:
    print("Please use a number")
    quit()


random_number = random.randint(0, top_of_range)

# section that loops game until user gets the correct answer

print(random_number)
