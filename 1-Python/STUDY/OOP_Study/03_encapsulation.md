# 03_encapsulation.md

## 🔓 Real-World Cybersecurity Use Case

Imagine you're building a **password cracking tool** or **brute-force engine**, and you store sensitive information like:
- Successful credentials
- API keys
- Tokens
- Number of failed attempts

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

    def mask_password(self, site):
        if site in self.__credentials:
            return '*' * len(self.__credentials[site])
        return "Not found"

# Example usage
if __name__ == "__main__":
    manager = SecurePasswordManager()
    manager.add_password("gmail.com", "hunter2")
    manager.add_password("example.com", "redteam123")

    print(manager.get_password("gmail.com"))         # hunter2
    print(manager.mask_password("example.com"))      # ***********
    print(manager.show_all_sites())                  # ['gmail.com', 'example.com']

    # 🔐 This will fail (encapsulation in action!)
    # print(manager.__credentials)

```

---

## 📘 Concept Explanation

### What is Encapsulation?

`Encapsulation` is about **hiding internal details** of a class:
    - Protect sensitive data by making attributes **private**.
    - Allow controlled access through methods like getters/setters.
Think of it as locking sensitive data inside a safe and only giving access through carefully designed doors.

- `__credentials` is **private attribute** — you can’t access it outside the class.
- The class controls how others interact with its data using **methods** like `add_password()` or `get_password()`.

Why is this important?
- It protects critical information.
- It prevents bugs from accidental overwrites.
- It ensures logic flows through controlled methods.


## 💡 What is Data Abstraction vs Encapsulation vs Information Hiding?
| Concept | Meaning |
|-------------|----------|
| Encapsulation | Bundling data + logic together; hiding how it works. |
| Abstraction | Showing only what matters; hiding the “how”. |
| Information Hiding | Preventing direct access to internal attributes. |


## 🔑 Public, Protected, and Private Attributes

| Concept   | Meaning       | Access Level |
|-----------|---------------|-------------------------------------------- |
| Public    | self.username | Can be accessed everywhere.                 |
| Protected | _token        | Shouldn’t be accessed outside (convention). |
| Private   | __secret      | Name-mangled (hard to access directly).     |
---

## 🧪 How to Use Getters and Setters

```python
class PayloadManager:
    def __init__(self):
        self.__payload = None

    def set_payload(self, data):
        if "<script>" not in data:
            self.__payload = data

    def get_payload(self):
        return self.__payload
```
🔍 This protects payloads from being overwritten with unsafe data.

## 🧠 Why Encapsulation Matters in Hacking Tools
- Prevents tools from leaking sensitive values.
- Enforces controlled access to payloads, credentials, tokens, and session data.
- Avoids breaking tools by blocking unauthorized changes to internal state.

🔐 Imagine if another part of your script accidentally overwrote found passwords — you'd lose hours of brute-force results.

---
## 🔧 Related Python Techniques
- `__dict__`: Even private vars show here with mangled names (_ClassName__attr).
- getattr(obj, "name", default): Get attributes dynamically and safely.
- hasattr(obj, "attr"): Check if something exists before touching it.
- property: The Pythonic way to create safe, readable getters/setters.

---

## 🛠 Offensive Security Application

Encapsulation is super useful when:
- Handling **sensitive data** (e.g., passwords, tokens, cookies)
- Tracking **found vulnerabilities** or **exploit chains** in memory
- Building tools where only certain parts of data should be changed (e.g., shellcode buffers, credential storage)

### In offensive security:
    - Password management tools often need to hide internal credentials but still allow access to them when necessary.
    - Tools like Brute Force or Exploits can expose sensitive data like authentication tokens or API keys, so encapsulating how they're stored and accessed ensures safer operations.
    - Encapsulation = safer tools with less unexpected behavior.

---

## 🔐 Connection to SOLID

This supports: **S O**
- ✅ **S – Single Responsibility Principle:** (methods handle one thing, adding passwords, masking them).
- ✅ **O – Open/Closed Principle:** (you can extend the tool without breaking how passwords are stored (add encryptadding passwords, masking them).ion))

By **encapsulating the storage logic**, you reduce risk and keep your class clean and maintainable, You can always extend the class to handle more complex operations (like encryption or expiry), without affecting the core logic of managing credentials.

---

## ✅ Exercises / Next Steps

1. 🧪 Try to print or modify `__credentials` from outside the class. What happens?
2. 🔐 Add a method that masks the password (e.g., returns `*****`).
3. 🧰 Extend the class to support deleting passwords securely.
4. 🛠 Try adding encryption to the password storage and adjusting the mask_password() function to show encrypted or decrypted values based on the password state.

---

## 🔗 Related Modules

- `02_attributes_methods.md` – Attributes define what the tool holds. Methods control actions.
- `04_inheritance.md` – You’ll learn how to build secure extensions like EncryptedPasswordManager or TokenManager.
