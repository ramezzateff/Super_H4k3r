#!/usr/bin/python3
# Write a function that removes duplicates from a list
def remove_duplicates(input_list):
    result = []  # Initialize an empty list to store non-duplicate elements
    seen = set()  # Initialize a set to keep track of seen elements

    for item in input_list:  # Iterate over each item in the input list
        if item not in seen:  # Check if the item has been seen before
            seen.add(item)  # Add item to the set of seen items
            result.append(item)

    return result  # Return the list with duplicates removed


original_list = [1, 2, 2, 3, 4, 4, 5]
new_list = remove_duplicates(original_list)
print(f"Original list: {original_list}")
print(f"List after duplicates removed: {new_list}")
