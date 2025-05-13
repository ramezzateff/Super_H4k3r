# 02_attributes_methods.md

## 🔓 Real-World Cybersecurity Use Case
Imagine you're developing a login brute-force tool. You want to store each target's login page and a list of usernames/passwords. You'll also need methods to try credentials and store results.

- **Attributes** represent the tool’s configuration and state.
- **Methods** represent the tool’s actions or logic.

---

## 💻 Python Code First – Brute Force Tool Example
```python
import requests

class LoginBruteForcer:
    def __init__(self, target_url):
        ''' __init__ sets up the object with attributes '''
        self.target_url = target_url  # attribute
        self.successful_logins = []   # attribute
        self.try_login()          # calling a method to add to object automatically

    def try_login(self, username, password):  # method
        response = requests.post(self.target_url, data={'username': username, 'password': password})
        if "Welcome" in response.text:
            print(f"[+] Login successful: {username}:{password}")
            self.successful_logins.append((username, password))

    def run(self, wordlist):  # method
        for username, password in wordlist:
            self.try_login(username, password)
    def __str__(self):
        return f'BruteForcer({self.target_url})'

# Example usage
if __name__ == "__main__":
    wordlist = [('admin', 'admin123'), ('admin', '123456'), ('root', 'toor')]
    bruteforcer = LoginBruteForcer("http://example.com/login")
    bruteforcer.run(wordlist)
```

## 📘 Concept Explanation

### 🔹 What Is an Attribute?

Attributes are variables attached to an object.
They store information about the object’s current state.

In our example:
- `target_url` is an attribute that holds the login page URL.
- `successful_logins` stores valid login combinations found.

### 🔹 What Is a Method?
- A **method** is a function defined inside a class.
- It performs actions using the object’s data (via `self`).

In our tool:
- `try_login()` is a method that tries a username/password.
- `run()` is a method that loops through credentials.

### 🔹 What’s the Difference Between Attribute and Property?
- An **attribute** is a variable on an object (`self.url`).
- A **property** is an attribute accessed using getter/setter logic — useful for validation and control.

```python
class Tool:
    def __init__(self):
        self._api_key = "123"

    @property
    def api_key(self):
        return self._api_key
```

### 🔹 Instance vs Class Attributes
- **Instance attribute** → specific to each object.
- **Class attribute** → shared across all instances.

```python
class Exploit:
    version = "1.0"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

### 🔹 Dynamically Adding Attributes
```python
scanner = LoginBruteForcer("http://target")
scanner.delay = 3  # dynamically added
```

### 🔹 The `__dict__` Attribute
- Holds all instance attributes as a dictionary:
```python
print(scanner.__dict__)
```

### 🔹 Using `getattr()`
```python
getattr(scanner, 'target_url')  # Returns the value
```

### 🔹 Getters and Setters (Pythonic Way)
```python
class SecureField:
    def __init__(self):
        self._token = None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        if value.startswith("sk-"):
            self._token = value
```

### 🔹 `__str__` vs `__repr__`
- `__str__` → human-readable (for `print()`)
- `__repr__` → dev-readable (for debugging)

```python
class Host:
    def __str__(self): return "Human"
    def __repr__(self): return "Dev"
```



---


## 🛠 Offensive Security Application

Attributes and methods help you:
- Store tool state (IP, ports, creds, responses)
- Automate actions (scan, connect, exploit)
- Separate data from logic (modular code)

Examples:
- Brute-force tools (store targets, handle attempts)
- Port scanners (track open ports, define scan logic)
- Exploit chains (track vulnerable targets, run steps)

They help organize logic cleanly:

- **Attributes** = tool configuration or state (IP, ports, credentials)
- **Methods** = actions your tool performs (scan, send, fuzz, etc.)

---

## 🔐 Connection to SOLID

This strengthens the **Single Responsibility Principle (SRP)**:

> “Each method should have one job.”

- `try_login()` only tries one login
- `run()` handles the brute-force loop
- `__init__` sets up the object(tool)

Keeping logic modular helps you test and reuse code.

- **Encapsulation Ready**: We’ll protect attributes in the next module using naming conventions (`_var`, `__var`) and property decorators.


---

## ✅ Exercises / Next Steps

1. ➕ Add a method to show only successful logins.
2. 🧪 Add an attribute for request delay and use `time.sleep()`.
3. 🔐 Use a property to make `target_url` read-only.
4. 🧰 Use `__repr__` to improve debugging output.

---

## 🔗 Related Modules

- **Previously**: `01_class_object.md` – learned what classes and objects are.
- **Coming Up**: `03_encapsulation.md` – how to protect internal attributes like `successful_logins`.
