#            012345 6789
my_string = 'Hello!Goodbye!'

"He isn't coming out today"

my_second_string = f"Hello!"
'He said, "Python is great!"'

my_third_string = f'''
He said, "Python is great, isn't it?"
She said, "It's okay"'''

print(my_string)

word = "Hello"
word_starts_at = my_string.find(word)

if word_starts_at == -1:
    print("Could not find word.")

print(my_string[7])
print(my_string[7:10])  # substringing - splicing

print(len(my_string))  # how long?
print(my_string.replace("Goodbye", "Hello"))
print(my_string.upper())
print(my_string.lower())
print(my_string.center(100))
print(my_string.ljust(100))
print(my_string.rjust(100))
print("one".isdigit())

print(str(True))
print(str(4.123) + 1)