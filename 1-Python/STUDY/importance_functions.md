# 📘 Python Reference Functions
A personal cheat-sheet for important and commonly used Python functions.

---

## 1. Core String Functions
> str.join(iterable)
- Purpose: Joins elements of an iterable (like a list) into a single string.
- Example: 
'''python
names = ['Ramez', 'Ali', 'Sara']
result = ', '.join(names)  # 'Ramez, Ali, Sara'
'''

---

> str.split(separator)
- Purpose: Splits a string into a list using the specified separator.
- Example:

'''python
ip = '192.168.1.1'
parts = ip.split('.')  # ['192', '168', '1', '1']
'''

---

> format(value, format_spec)
- Purpose: Formats a value (like an integer) into a specific representation.
- Common Use Case: Convert integer to binary.

Example:
'''python
binary = format(192, '08b')  # '11000000'
'''