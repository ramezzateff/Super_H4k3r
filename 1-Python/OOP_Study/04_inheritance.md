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


# Example usage
if __name__ == "__main__":
    port_scan = PortScanner("192.168.1.1")
    port_scan.scan()
    port_scan.report()

    sub_scan = SubdomainScanner("example.com")
    sub_scan.scan()
    sub_scan.report()
📘 Concept Explanation
What is Inheritance?
Inheritance allows one class (child) to reuse and extend the code from another class (parent).

Scanner is the base class (parent).

PortScanner and SubdomainScanner are child classes.

They inherit attributes like target, results, and methods like report().

This makes your code more modular, reusable, and organized.

🛠 Offensive Security Application
You can use inheritance to:

Build toolchains (e.g., all tools inherit from ToolBase)

Extend scanners (e.g., base scanner class → add DNS, port, vuln scanning)

Reuse methods (e.g., logging, reporting, formatting output)

Inheritance helps you keep a single base logic and extend specific features cleanly.

🔐 Connection to SOLID
This supports:

✅ Open/Closed Principle: Classes are open for extension but closed for modification.

You extend the base Scanner without touching its code.

✅ Exercises / Next Steps
🧪 Add a VulnerabilityScanner class that inherits from Scanner and simulates checking for CVEs.

🧰 Add a run_all() method that takes a list of scanners and calls scan() + report() on each.

🔗 Related Modules
Previously: 03_encapsulation.md – we learned how to protect internal data.

Coming up: 05_polymorphism.md – we’ll learn how to call the same method name on different objects (like scan()), and each does something different!