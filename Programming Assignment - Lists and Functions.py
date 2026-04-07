# Chapter 7 Exercises

# 7.4 Create the list
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5 Capitalize the person element
things[1] = things[1].capitalize()
print("After capitalizing Cinderella:", things)
# Yes, it DOES change the element in the list because strings are replaced in the list.

# 7.6 Make the cheesy element uppercase
things[0] = things[0].upper()
print("After making mozzarella uppercase:", things)

# 7.7 Delete the disease element
del things[2]
print("After deleting salmonella:", things)

# Chapter 9 Exercises

# 9.1 Function that returns a list
def good():
    return ['Harry', 'Ron', 'Hermione']

print("Good function output:", good())


# 9.2 Generator function for odd numbers
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

# Find and print the third odd number
count = 0
for number in get_odds():
    count += 1
    if count == 3:
        print("Third odd number:", number)
        break