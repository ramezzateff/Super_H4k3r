
# 05_polymorphism.md

## 🎯 Real-World Cybersecurity Use Case

You're developing a **modular brute-force engine** that supports brute-forcing different protocols like SSH, FTP, and HTTP logins.

Each module must implement its own way to brute-force, but all should follow the same interface (e.g., a `.run()` method).  
This is where **polymorphism** helps you write tools that are easy to extend and maintain.

---

## 💻 Python Code – BruteForcer Interface Example

```python
class BruteForcer:
    def run(self):
        raise NotImplementedError("Subclasses must implement the run method.")


class SSHBruteForcer(BruteForcer):
    def run(self):
        print("[SSH] Trying credentials on port 22...")


class FTPBruteForcer(BruteForcer):
    def run(self):
        print("[FTP] Trying credentials on port 21...")


class HTTPBruteForcer(BruteForcer):
    def run(self):
        print("[HTTP] Sending POST requests to login endpoint...")


# Generic function that takes any brute forcer
def execute_brute_force(tool: BruteForcer):
    tool.run()


# Example usage
if __name__ == "__main__":
    brute_tools = [SSHBruteForcer(), FTPBruteForcer(), HTTPBruteForcer()]

    for tool in brute_tools:
        execute_brute_force(tool)
```

---

## 📘 Concept Explanation

### What is Polymorphism?

Polymorphism means **many forms** — different classes can define the same method (like `run()`), and you can call them in a generic way.

- Each brute-forcer tool implements its own `run()` method.
- But you can loop over all tools and just call `.run()` without caring which type they are.

This leads to cleaner, modular code with less duplication.

---

## 🛠 Offensive Security Application

Polymorphism is powerful when you're building tools like:
- Brute-force engines for SSH, FTP, HTTP, etc.
- Payload encoders (Base64, URL, Hex, etc.)
- Report generators (JSON, CSV, Text)

It helps avoid repetitive `if` conditions and makes your tools flexible and extensible.

---

## 🔐 Connection to SOLID

✅ **Open/Closed Principle**: You can add a new brute-forcer (like MySQL) by just adding a class without touching existing logic.

✅ **Liskov Substitution Principle**: You can use any subclass of `BruteForcer` in place of the base class, and the program will still work.

---

## ✅ Exercises / Next Steps

1. 🧪 Add a `MySQLBruteForcer` that inherits from `BruteForcer` and prints a fake login attempt.
2. ⏱ Modify `execute_brute_force()` to log the time taken by each brute-forcer.
3. 🧾 Create a generic `Reporter` class and subclasses like `JSONReporter`, `TextReporter`, etc., that use `output()` polymorphically.

---

## 🔗 Related Modules

- Previously: `04_inheritance.md` – we learned how classes can inherit behavior from other classes.
- Coming up: `06_abstraction.md` – you'll learn how to enforce certain structure using abstract base classes.
