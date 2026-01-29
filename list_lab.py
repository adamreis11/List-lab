# list_lab.py

# --------------------
# SERIES 1
# --------------------

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print("Series 1:")
print(fruits)

# Add a fruit to the end
new_fruit = input("Add another fruit: ")
fruits.append(new_fruit)
print(fruits)

# Ask user for a number (1-based) and show fruit
num = int(input("Pick a number: "))
print(f"You picked {num}, which corresponds to: {fruits[num - 1]}")

# Add fruit using + operator
fruits = ["Grapes"] + fruits
print(fruits)

# Add fruit using insert()
fruits.insert(0, "Bananas")
print(fruits)

# Display fruits starting with P
print("Fruits that start with P:")
for fruit in fruits:
    if fruit.startswith("P"):
        print(fruit)


# --------------------
# SERIES 2
# --------------------

print("\nSeries 2:")
print(fruits)

# Remove last fruit
fruits.pop()
print(fruits)

# Ask user for a fruit to delete
delete_fruit = input("Enter a fruit to delete: ")
if delete_fruit in fruits:
    fruits.remove(delete_fruit)
print(fruits)


# --------------------
# SERIES 3
# --------------------

print("\nSeries 3:")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]  # reset

new_list = []
for fruit in fruits:
    while True:
        answer = input(f"Do you like {fruit.lower()}? (yes/no) ").lower()
        if answer == "yes":
            new_list.append(fruit)
            break
        elif answer == "no":
            break
        else:
            print("Please answer 'yes' or 'no'.")

print("Fruits you like:", new_list)


# --------------------
# SERIES 4
# --------------------

print("\nSeries 4:")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]  # reset

# Make reversed copy
reversed_list = [fruit[::-1] for fruit in fruits]

# Delete last item from original list
fruits.pop()

print("Original list:", fruits)
print("Reversed list:", reversed_list)
