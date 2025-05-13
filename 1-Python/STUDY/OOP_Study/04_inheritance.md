# 04_inheritance.md

## 🔓 Real-World Cybersecurity Use Case

You’re building a **multi-purpose scanner**.

- One class does **port scanning**
- Another performs **subdomain brute-forcing**
- A third checks for **vulnerabilities**

Using **inheritance**, you can create a base `Scanner` class and then extend it for each type of scanner.

---

## 💻 Python Code First – Scanner Inheritance Example

```python
class Scanner:
    def __init__(self, target):
        self.target = target
        self.results = []

    def report(self):
        print(f"[+] Scan Results for {self.target}")
        for item in self.results:
            print(f" - {item}")


class PortScanner(Scanner):
    def scan(self):
        print(f"[*] Scanning ports on {self.target}")
        # Simulated scan
        self.results = [22, 80, 443]


class SubdomainScanner(Scanner):
    def scan(self):
        print(f"[*] Brute-forcing subdomains on {self.target}")
        # Simulated brute force
        self.results = ["mail.example.com", "dev.example.com"]


## Example usage
if __name__ == "__main__":
    port_scan = PortScanner("192.168.1.1")
    port_scan.scan()
    port_scan.report()

    sub_scan = SubdomainScanner("example.com")
    sub_scan.scan()
    sub_scan.report()
```

## 📘 Concept Explanation

### What is Inheritance?
**Inheritance** is when a class derives or inherits functionality from another class.

### 🔹 What is a Superclass / Base Class / Parent Class?
These are all terms for the original class that others inherit from. In our case:
```python
class Scanner:
```
### 🔹 What is a Subclass?
The new class that inherits from a base class. It gains all the parent’s methods and attributes but can:
    - Add new behavior
    - Override old behavior

Example:
```python
class PortScanner(Scanner):

```
### 🔹 How to Inherit a Class
Use this syntax:

```python
class ChildClass(ParentClass):
```
You can even inherit from multiple classes:

```python
class ExploitTool(Logger, PayloadBuilder):
```
### 🔹 Default Parent Class in Python?
If you don’t specify any parent, your class inherits from Python’s built-in:
```python
class object
```

So technically:
```python
class Scanner:  # is the same as
class Scanner(object):
```

### Overriding Methods or Attributes
You can replace a method in a subclass by defining it again:

```python
class SubdomainScanner(Scanner):
    def scan(self):  # Overrides Scanner.scan()
        pass
```

### 🔹 What Attributes/Methods Are Inherited?
All public and protected attributes and methods are inherited. Private ones (with __) are not directly accessible in child classes.


### Why is this important?

It promotes code reusability.

It allows you to add specific functionality without changing the core logic of the base class.

This makes your code more modular, reusable, and organized.

---

## 🛠 Offensive Security Application
Inheritance is a great tool when:

- Inheritance helps you build modular, reusable security tools.
- Base class = shared logic (init, report)
- Subclasses = custom actions (port scan, vuln check, brute-force)

### 🔐 Examples:
1. BaseScanner → PortScanner, SubdomainScanner, CVEChecker
2. BaseExploit → BufferOverflow, SQLiExploit, XSSPayload
3. LoginTool → SSHBruteForcer, WebLoginFuzzer

### In offensive security:

- Password cracking tools can use inheritance to create specialized classes for different algorithms or methods (brute force, dictionary attacks, etc.).

- Exploitation frameworks can inherit from a base class for general payload delivery while allowing more specific implementations (like buffer overflow, or web shell payloads).

- Inheritance = efficient code and enhanced functionality.

- Inheritance helps you keep a single base logic and extend specific features cleanly.

---

## 🔐 Connection to SOLID
This supports:

- ✅ O - Open/Closed Principle: Classes are open for extension but closed for modification.
    - You extend the base Scanner without touching its code.
- ✅ L - Liskov Substitution Principle (a child class should be substitutable for the parent class)

By using inheritance, you can maintain a clean and extendable codebase that adheres to key software design principles.

---

## 🧠 Why Inheritance Matters in Red Teaming
- You can create families of tools with shared structure
- One ToolFramework class → dozens of specialized modules
- Easily scale scripts from simple recon to full exploit delivery

Inheritance = more tools, less code.

---

##✅ Exercises / Next Steps
1. 🧪 Add a `VulnerabilityScanner` class that inherits from `Scanner` and simulates checking for CVEs.
2. 🧰 Add a `run_all()` method that takes a list of scanners and calls `scan()` + `report()` on each.
3. 🔧 Add an extra attribute in PortScanner to simulate open/closed ports filtering.
4. 🔄 Override report() in SubdomainScanner to show a fancier output.

---

## 🔗 Related Modules
- Previously: `03_encapsulation.md` – we learned how to protect internal logic and data.
- Coming up: `05_polymorphism.md` – we’ll learn how to call the same method name on different objects (like `scan()`), and each does something different!