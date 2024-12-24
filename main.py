import random
from http.cookiejar import user_domain_match

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
guesses = 0
# section that loops game until user gets the correct answer
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please use a number next time")
        continue
    if user_guess == random_number:
        print("Congrats! You got it!!!!!! :D")
        break
    else:
        if user_guess > random_number:
            print("Too low! Try again!")
        else:
            print("Too high! Try again!")


print("It took you ", guesses, "guesses")
