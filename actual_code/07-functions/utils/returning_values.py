def add(number1, number2, debugging=False):
    if debugging:
        print(f"DEBUGGING: {number1}, {number2} - result is {number1 + number2}")

    return number1 + number2

result1 = add(1, 2, True)
result2 = add(3, 4)

print(add(1,2) + add(3,4))
print(add(result1,result2))
print(add(add(1,2), add(3,4)))

def analyse_numbers(number1, number2):
    sum_result = add(number1, number2)
    differnece = number1 - number2

    return f"Sum: {sum_result}, Difference: {differnece}"
