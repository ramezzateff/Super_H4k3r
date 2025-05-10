
# 01_class_object.md

## 🔓 Real-World Cybersecurity Use Case

Let’s say you’re building a **subdomain brute-force tool**. Each subdomain attempt can be represented as an "object", and your tool structure can be a class. This lets you manage scanning logic cleanly, reuse it, and expand it later.

---

## 💻 Python Code First – Subdomain Brute-Forcer Example

```python
import requests

class SubdomainScanner:
    def __init__(self, domain):
        self.domain = domain
        self.found_subdomains = []

    def scan(self, wordlist):
        for sub in wordlist:
            url = f"http://{sub}.{self.domain}"
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    print(f"[+] Found: {url}")
                    self.found_subdomains.append(url)
            except requests.ConnectionError:
                pass

# Example Usage
if __name__ == "__main__":
    wordlist = ['www', 'mail', 'ftp', 'admin']
    scanner = SubdomainScanner("example.com")
    scanner.scan(wordlist)
```

---

## 📘 Concept Explanation

### What is a Class?
- A **class** is a blueprint or template for creating objects.
- Think of it like a **tool definition** — it tells Python what kind of data and functions (called methods) the tool has.

### What is an Object?
- An **object** is a copy of that tool you can use.
- In our example, `scanner = SubdomainScanner("example.com")` creates an actual instance of the scanner tool for a specific domain.

Classes keep your code organized and reusable. Instead of writing separate functions and variables everywhere, you group them inside a class.

---

## 🛠 Offensive Security Application

Why are classes important in hacking tools?

- You can wrap scanners, payload builders, encoders, and exploit logic into **self-contained, reusable objects**.
- You can reuse the same class for different targets (`SubdomainScanner("example.com")`, `SubdomainScanner("target.com")`).
- This makes your tools easier to scale — imagine scanning multiple domains using multiple instances of the class.

**When to use classes?**
- When your tool needs to manage state (like found subdomains, login attempts, results)
- When you plan to add more functionality (like logging, saving output, threading)

---

## 🔐 Connection to SOLID

This relates to the **Single Responsibility Principle (SRP)**:
> A class should only have one reason to change.

Here, `SubdomainScanner` has one job: scanning for subdomains. It doesn’t handle logging, file saving, or threading — these can be separate classes later.

---

## ✅ Exercises / Next Steps

1. 🔧 Modify the class to also save the results to a file (`results.txt`).
2. 🔀 Extend it to accept a `https` option and test both `http` and `https` schemes.

---

## 🔗 Related Modules

- This sets the foundation for:  
  - `02_attributes_methods.md` – which explains how to customize what your objects can do.  
  - `03_encapsulation.md` – where we’ll protect internal logic like the found subdomains list.
