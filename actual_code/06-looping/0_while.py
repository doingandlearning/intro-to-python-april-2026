user_input = input("Give me your password: ")
real_password = "password123"
attempts_tried = 1

while user_input != real_password and attempts_tried < 3:
    print("Wrong password. Try again.")
    user_input = input("Give me your password: ")
    # attempts_tried = attempts_tried + 1
    attempts_tried += 1

if attempts_tried < 3:
    print("Here are your secret documents.")
else:
    print("Unauthorized. You have been reported to the police.")