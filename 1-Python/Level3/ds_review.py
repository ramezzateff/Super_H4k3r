# ================================
# 📚 Python Data Structures Reference
# Lists, Tuples, Dictionaries, Sets & Nested Structures
# ================================

# ===== Lists =====
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.insert(2, 99)
my_list.remove(3)
popped = my_list.pop()
print(my_list[0], my_list[-1])
print(my_list[1:4])
for item in my_list:
    print(item)
my_list.sort()
my_list.reverse()
even_numbers = [x for x in my_list if x % 2 == 0]

# ===== Tuples =====
my_tuple = (10, 20, 30)
print(my_tuple[1])
for item in my_tuple:
    print(item)
a, b, c = my_tuple
print(a, b, c)

# ===== Dictionaries =====
my_dict = {
    "name": "Ramez",
    "age": 20,
    "track": "Cybersecurity"
}
print(my_dict["name"])
print(my_dict.get("city", "Not found"))
my_dict["email"] = "ramez@example.com"
my_dict["age"] = 21
del my_dict["track"]
for key, value in my_dict.items():
    print(key, value)
print(list(my_dict.keys()))
print(list(my_dict.values()))
if "name" in my_dict:
    print("Name exists")

# ===== Sets =====
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.remove(2)
my_set.update([6, 7])
print(3 in my_set)
for item in my_set:
    print(item)
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # Intersection
print(set1 | set2)  # Union
print(set1 - set2)  # Difference

# ===== Nested Structures =====
# List of lists
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # Output: 2

# Dictionary of dictionaries
users = {
    "user1": {"name": "Ramez", "age": 20},
    "user2": {"name": "Ali", "age": 22}
}
print(users["user1"]["name"])

# Dictionary with list values
scores = {
    "math": [90, 85, 92],
    "science": [88, 79, 95]
}
print(scores["math"][1])  # Output: 85

