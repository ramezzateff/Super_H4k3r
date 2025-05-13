
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
- Think of it like a **tool definition** — it tells Python what kind of **attributes** (data) and **method** (functions) the tool has.
- Think of a class like the blueprint of a hacking tool - it defines what the tool cacn do.


### What is an **Object/Instance**?
- An **Object/Instance** is a copy based on the class blueprint
like that tool you can actually use, built from the class.
- In our example
    `scanner = SubdomainScanner("example.com")`  
    here, `scanner` is and **object/instance** of the `SubdomainScanner` class.

Classes keep your code organized and reusable. Instead of writing separate functions and variables everywhere, you group them inside a class.

---

### What is the Difference Between a Class and an Object?

| Class                   | Object                               |
|------------------------ |------------------------------------- |
| A design or templat     | A live version built from that design|
| Defines structure       | Has real data inside                 |
| E.g., SubdomainScanner  | E.g., scanner = SubdomainScanner(...)|

---

### 🔹 What is a Reference, Assignment, and Alias?
#### When you assign one object to another variable, you're creating a reference:

```python
scanner1 = SubdomainScanner("example.com")
scanner2 = scanner1  # scanner2 is an alias, both point to the same object

```
- Changing scanner2.domain would also change scanner1.domain, because they are both pointing to the same object in memory.

---

### 🔹 What is self in Python Classes?
- self refers to the current object (like "this" in other languages), think of it, the self can be a bag where you can put any attribute inside of it and share its own attribute with any method in that class
- It allows each object to keep **its own copy** of variables and methods.
- Without `self`, all objects would share the same data.
- You must include self as the first argument in every method inside a class:
```python
def __init__(self, domain):  # self.domain refers to this object's data

```

---

### 🔹 What is the Special __init__ Method?
- `__init__()` is **the constructor and special method** in Python classes.
- It runs **automatically** when you create a new object from the class.
- It's called the **constructor** because it “constructs” the object and sets up its initial attributes.
- can call any `method` inside it by calling `self.method()`
- You use it to set up initial attributes:
```python
def __init__(self, domain):
    self.domain = domain # inital attribute
    self.scan() # calling a method to run automatic when object = SubdomainScanner
```

---

## 🔹 How Do Objects Represent Real-World Entities in Security Tools?
Objects can represent:
    - A target (TargetScanner(ip))
    - A payload builder (PayloadBuilder(type='xss'))
    - A brute-force session (LoginBruteForcer(url))
- You map real-world hacking tasks to Python objects that are reusable and organized.

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

Here, `SubdomainScanner` has one job: scanning for subdomains.
It doesn’t handle logging, file saving, or threading — these can be separate classes later.

---

## 🧠 Checkpoints: Key Takeaways
- ✅ A class defines what an object is and does.
- ✅ An object is a working version of a class.
- ✅ __init__() sets up the object when it's created.
- ✅ self refers to the object itself — always use it in methods.
- ✅ Objects help map real security tasks to reusable code.

## 🧪  Exercises / Next Steps

1. 🔧 Add a method to SubdomainScanner that saves results to a file.
2. 🌐 Modify the scan() method to check both http and https schemes.
3. 🔁 Create a second scanner object and run it on a different domain — reuse the class.

---

## 🔗 Related Modules

`00_python_why_oop.md` – Why Python and OOP are great for hackers.
`02_attributes_methods.md` – Learn how objects store data and run logic (attributes + methods).
