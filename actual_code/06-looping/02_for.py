number_to_find = 3

for attempt_number in range(10):
    if attempt_number == number_to_find:
        print("Found it!", number_to_find)
        break
    else:
        print(f"Still looking for {number_to_find}! it's not {attempt_number}")

for _ in range(3):
    print("Hello")


for attempt_number in range(10):
    if attempt_number % 2  == 0:
        continue
    print("We only like odd numbers.")
    print(f"Hello number {attempt_number}")


