
# 03_encapsulation.md

## 🔓 Real-World Cybersecurity Use Case

You’re building a **password manager tool** for internal use during red teaming. You want to securely store passwords and avoid exposing them directly.  
Encapsulation lets you protect sensitive data like credentials, hashes, and tokens inside classes.

---

## 💻 Python Code First – SecurePasswordManager Example

```python
class SecurePasswordManager:
    def __init__(self):
        self.__credentials = {}  # private attribute

    def add_password(self, site, password):
        self.__credentials[site] = password

    def get_password(self, site):
        return self.__credentials.get(site, "Not found")

    def show_all_sites(self):
        return list(self.__credentials.keys())

# Example usage
if __name__ == "__main__":
    manager = SecurePasswordManager()
    manager.add_password("gmail.com", "hunter2")
    manager.add_password("example.com", "redteam123")
    
    print(manager.get_password("gmail.com"))         # hunter2
    print(manager.show_all_sites())                  # ['gmail.com', 'example.com']
    
    # This won't work (protected by encapsulation)
    # print(manager.__credentials)
```

---

## 📘 Concept Explanation

### What is Encapsulation?

Encapsulation means **hiding internal details** of how your class works.  
You keep attributes **private**, so other parts of the code can’t modify them directly.

- `__credentials` is **private** — you can’t access it outside the class.
- The class controls how others interact with its data using **methods** like `add_password()` or `get_password()`.

Why is this important?
- It protects critical information.
- It prevents bugs from accidental overwrites.
- It ensures logic flows through controlled methods.

---

## 🛠 Offensive Security Application

Encapsulation is super useful when:
- Handling **sensitive data** (e.g., passwords, tokens, cookies)
- Tracking **found vulnerabilities** or **exploit chains** in memory
- Building tools where only certain parts of data should be changed (e.g., shellcode buffers, credential storage)

Encapsulation = safer tools with less unexpected behavior.

---

## 🔐 Connection to SOLID

This supports:
- ✅ **Single Responsibility Principle** (methods handle one thing)
- ✅ **Open/Closed Principle** (you can extend the tool without breaking how passwords are stored)

By **encapsulating the storage logic**, you reduce risk and keep your class clean and maintainable.

---

## ✅ Exercises / Next Steps

1. 🧪 Try to print or modify `__credentials` from outside the class. What happens?
2. 🔐 Add a method that masks the password (e.g., returns `*****`).
3. 🧰 Extend the class to support deleting passwords securely.

---

## 🔗 Related Modules

- Previously: `02_attributes_methods.md` – we learned how to define variables and functions inside classes.
- Coming up: `04_inheritance.md` – we’ll learn how to **extend** this class to support encryption, password expiry, and more!
