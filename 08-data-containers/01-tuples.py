empty_tuple = ()
empty_tuple = tuple()

print(empty_tuple)
print(type(empty_tuple))

#            0  1  2  3  4  5   6  7   8   9   10     position or index
fib_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
print(fib_tuple[5])
print(fib_tuple[2:7])
print(fib_tuple[2:])
print(fib_tuple[:7])

print(len(fib_tuple))

print(fib_tuple.count(1))  # how many times does 2 occur inside my tuple
# print(fib_tuple.index(19))

target = 55
if target in fib_tuple:
    print(f"{target} is at position {fib_tuple.index(target)}")
else:
    print(f"{target} is not in fib_tuple")

for number in fib_tuple:
    print(f"{number} is at position {fib_tuple.index(number)}")

hit = (12.4, -3.1, 0.0)  # x,y,z
x = hit[0]
y = hit[1]
z = hit[2]

# unpacking -> destructuring
x, y, z = hit

track_1 = (0.5, 1.2, -0.3)
track_2 = (1.1, 2.2, 3.3)
track_3 = (0.0, -2.0, 0.2)

event = (track_1, track_2, track_3)
print(event)
print(event[2][1])

user = ("Kevin", 3, False)
user_new = ("kevin", False, 3)

# tuple of types of a tuple