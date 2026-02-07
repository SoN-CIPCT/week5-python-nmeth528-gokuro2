# homework5_george_okuro.py
# NMETH-528 Week 5: Working with Lists and Tuples

# -------------------
# List Exercise
# -------------------

items = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

print("Items in the list:")
for item in items:
    print(item)

print(f"\nThe first two items in the list are: {items[0]}, {items[1]}")

middle_items = items[2:4]
print(f"The middle two items in the list are: {middle_items[0]}, {middle_items[1]}")

print(f"The first and last items in the list are: {items[0]}, {items[-1]}")

# -------------------
# Tuple Exercise
# -------------------

menu = ("pizza", "burger", "salad", "pasta", "soup")

print("\nOriginal menu:")
for food in menu:
    print(food)

updated_menu = ("pizza", "tacos", "salad", "pasta", "sandwich")

print("\nUpdated menu:")
for food in updated_menu:
    print(food)
