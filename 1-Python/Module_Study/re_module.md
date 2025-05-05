
# 🧠 Python `re` Module – Regular Expressions Made Simple

---

## 1. 🔍 Simple Definition

The `re` module in Python provides support for **Regular Expressions** — a powerful tool for **pattern matching**, **searching**, and **text manipulation**.  
It lets you find strings that match a pattern (like emails, IPs, or phone numbers) and do something with them (extract, replace, validate, etc.).

---

## 2. 🌍 Real-world Use Cases

| Use Case | Description |
|----------|-------------|
| ✅ Data Validation | Check if input matches email, IP, date format. |
| ✅ Data Extraction | Extract emails, hashtags, IPs, domains from text. |
| ✅ Log Analysis | Filter or parse server logs (e.g. status codes, URLs). |
| ✅ Form Input Cleaning | Remove extra spaces, special chars, or normalize data. |
| ✅ Scraping | Extract content from HTML or web data. |

---

## 3. 🧱 Core Functions and Concepts

| Function | Description |
|----------|-------------|
| `re.search()` | Search for the first match in the string. |
| `re.match()` | Match only at the beginning of the string. |
| `re.findall()` | Return **all** matches in a list. |
| `re.sub()` | Replace matches with a string. |
| `re.split()` | Split string by the matched pattern. |
| `re.compile()` | Compile a pattern for reuse (good for performance). |

---

## 🧩 Special Regex Patterns

| Pattern | Meaning |
|--------|---------|
| `.` | Any character (except newline) |
| `\d` | Digit (0-9) |
| `\w` | Word character (letters, digits, _) |
| `\s` | Whitespace |
| `^` | Start of string |
| `$` | End of string |
| `[...]` | Match any one of the characters |
| `+`, `*`, `?` | Quantifiers |
| `()` | Grouping |

---

## 4. 💻 Mini Code Example

```python
import re

text = "My email is example123@test.com and my IP is 192.168.1.1"

# Extract email
email = re.search(r"[\w.-]+@[\w.-]+", text)
print("Email:", email.group())

# Extract all numbers
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

# Replace IP address with [REDACTED]
sanitized = re.sub(r"\d+\.\d+\.\d+\.\d+", "[REDACTED]", text)
print("Cleaned Text:", sanitized)
```

---

## 5. 🛠 Practical Notes

- Use **raw strings** (with `r""`) to avoid escaping issues (`\` becomes just `\`).
- `re.search()` returns a match object → use `.group()` to get the match.
- `re.findall()` gives you a list of all matches.
- `re.sub()` is great for sanitizing or formatting.
- Regex can be tricky — test your patterns at [regex101.com](https://regex101.com)

---

## 6. 🔐 Related Domains

| Field | Use Case |
|-------|----------|
| **Cybersecurity** | Detect IPs, credentials, URLs in logs or payloads. |
| **Web Scraping** | Extract product info, prices, links. |
| **Data Cleaning** | Format phone numbers, emails, or names. |
| **Automation** | Filter command outputs, clean logs. |
| **Network Analysis** | Parse protocols, IPs, ports from data streams. |

---

## ✅ Summary

The `re` module is one of Python’s most powerful tools for working with text. If you want to extract, validate, or manipulate strings based on patterns — this is your go-to module.
