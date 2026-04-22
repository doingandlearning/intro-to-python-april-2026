# Step 3: optional km to miles with simple validation
km_text = input('Please input the distance in kilometres: ')
if km_text.replace(".", "").isnumeric():
    km = float(km_text)
    print(f'You entered the distance {km} in kilometres')
    print(f'The distance in miles is {round(km * 0.6214, 3)}')
else:
    print('Not an positive float number')