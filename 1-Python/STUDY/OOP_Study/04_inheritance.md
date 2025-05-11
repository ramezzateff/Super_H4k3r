# 04_inheritance.md

## 🔓 Real-World Cybersecurity Use Case

You’re building a **multi-purpose scanner**. One scanner does port scanning, another does subdomain brute-forcing. Both share some common behavior: they target hosts, run, and report results.

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
Inheritance allows a class to inherit attributes and methods from another class. It’s a way of creating hierarchies of classes, where a more general class (parent) can be extended by a more specific class (child).

- `Scanner` is the base class (parent).

- `PortScanner` and `SubdomainScanner` are child classes.

They inherit attributes like `target`, `results`, and methods like `report()`.

### Why is this important?

It promotes code reusability.

It allows you to add specific functionality without changing the core logic of the base class.

This makes your code more modular, reusable, and organized.

---

## 🛠 Offensive Security Application
Inheritance is a great tool when:

- Building modular security tools that have common functionality (e.g., different types of scans or attacks that all need a basic setup).
- Extending pre-existing tools for specialized use cases (e.g., a basic scanning tool that can be enhanced with encryption, logging, or reporting).
- Creating customizable frameworks for ethical hacking tools, where one class handles core actions and others extend it for specific tasks.

### In offensive security:

- Password cracking tools can use inheritance to create specialized classes for different algorithms or methods (brute force, dictionary attacks, etc.).

- Exploitation frameworks can inherit from a base class for general payload delivery while allowing more specific implementations (like buffer overflow, or web shell payloads).

- Inheritance = efficient code and enhanced functionality.

- Inheritance helps you keep a single base logic and extend specific features cleanly.

---

## 🔐 Connection to SOLID
This supports:

- ✅ Open/Closed Principle: Classes are open for extension but closed for modification.
    - You extend the base Scanner without touching its code.
- ✅ Liskov Substitution Principle (a child class should be substitutable for the parent class)

By using inheritance, you can maintain a clean and extendable codebase that adheres to key software design principles.

---

##✅ Exercises / Next Steps
1. 🧪 Add a `VulnerabilityScanner` class that inherits from `Scanner` and simulates checking for CVEs.

2. 🧰 Add a `run_all()` method that takes a list of scanners and calls `scan()` + `report()` on each.

---

## 🔗 Related Modules
- Previously: `03_encapsulation.md` – we learned how to protect internal data.

- Coming up: `05_polymorphism.md` – we’ll learn how to call the same method name on different objects (like `scan()`), and each does something different!