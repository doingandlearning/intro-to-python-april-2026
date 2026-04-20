# 🧠 Extension Lab: Mad Libs with String Magic

Let’s build a silly Mad Libs generator with **extra string power**. You’ll gather inputs, build a story, then apply string methods to explore and transform it.

---

## Step 1: Gather the Ingredients

Ask the user for:

* A name
* An animal
* A number
* A colour
* A city
* A verb ending in -ing
* A type of food

```python
name = input("Enter a name: ")
animal = input("Enter an animal: ")
number = input("Enter a number: ")
colour = input("Enter a colour: ")
city = input("Enter a city: ")
verb = input("Enter a verb ending in -ing: ")
food = input("Enter a type of food: ")
```

---

## Step 2: Build the Story

Use `f-strings` or concatenation to construct a story.

```python
story = (
    f"One day, {name} saw a {colour} {animal} in {city}.\n"
    f"It was {verb} while eating {food}.\n"
    f"Locals said there were {number} of them!"
)

print("\n--- Your Story ---")
print(story)
```

---

## Step 3: Explore the Story with String Methods

Now, play with your story:

```python
print("\n--- Story Stats ---")
print("Length of story:", len(story))
print("Story in UPPERCASE:\n", story.upper())
print("Story in lowercase:\n", story.lower())
print("Story in Title Case:\n", story.title())
print("Replacing all 'a' with '*':\n", story.replace('a', '*'))
print("Does the story mention 'dragon'? ->", story.find("dragon"))
print("Does the story equal 'Hello World'? ->", story == "Hello World")
```

---

## Step 4: Type Inspection

Print the types of a few values:

```python
print("\n--- Type Check ---")
print("Type of name:", type(name))
print("Type of number (before conversion):", type(number))
print("Type of story:", type(story))
```

---

## Step 5: Bonus – Clean Up the Output

Ask the user for their **full name** and trim any extra whitespace before printing:

```python
full_name = input("\nEnter your full name with some extra spaces: ")
print("Raw input: '" + full_name + "'")
print("Cleaned up:", full_name.strip())
```

---

### ✅ You’ve Used:

* `input()`, `print()`, `type()`, `len()`
* String methods: `.upper()`, `.lower()`, `.title()`, `.replace()`, `.find()`, `.strip()`
* String formatting: `f"..."`, concatenation
* No flow control or functions
