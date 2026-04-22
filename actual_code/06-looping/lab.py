# 5! = 5 x 4 x 3 x 2 x 1
# 0! = 1
# 3.5!

import math



user_input = input("Give me an integer number n: ")

if not user_input.isdigit():
    print("Sorry. This is invalid. You need to enter a positive integer.")
else:
    upper_limit = int(user_input)

    factorial = 1
    while upper_limit > 0:
        factorial = factorial * upper_limit
        upper_limit -= 1


    #
    # for attempt_number in range(1, upper_limit+1):
    #     # factorial = factorial * attempt_number
    #     factorial *= attempt_number
    print(f"The factorial of {user_input}! is {factorial}")
    if math.factorial(int(user_input)) == factorial:
        print("Your solution is correct.")