# Python Module: `os`

## 1. Simple Definition

The `os` module in Python provides functions for interacting with the operating system. It allows you to perform tasks such as navigating the file system, reading environment variables, running system commands, and working with files and directories.

---

## 2. Real-world Use Cases

- Automating file organization (e.g., sorting files into folders by type)
- Building CLI tools that interact with the file system
- Reading or setting environment variables (for config or secrets)
- Creating and managing folders or logs in data pipelines
- Writing cross-platform scripts for DevOps and system admin tasks

---

## 3. Core Functions

| Function | Description |
|----------|-------------|
| `os.getcwd()` | Returns the current working directory |
| `os.listdir(path)` | Lists all files and folders in the given path |
| `os.mkdir(path)` | Creates a new directory |
| `os.makedirs(path)` | Recursively creates directories |
| `os.remove(path)` | Deletes a file |
| `os.rmdir(path)` | Deletes a folder |
| `os.rename(src, dst)` | Renames a file or folder |
| `os.path.join(a, b)` | Joins two paths correctly for the current OS |
| `os.path.exists(path)` | Checks if a path exists |
| `os.environ` | Accesses environment variables |

---

## 4. Mini Code Example

```python
import os

# Get current directory
print("Current directory:", os.getcwd())

# Create a new folder
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

# Rename folder
os.rename("test_folder", "renamed_folder")

# List files in the directory
print("Files in current directory:", os.listdir("."))

# Remove the folder
os.rmdir("renamed_folder")
print("Folder removed.")
```

---

## 5. Practical Notes

- Always check if a file/folder exists before deleting or renaming it using `os.path.exists()`.
- Use `os.path.join()` instead of manually concatenating paths (especially for cross-platform compatibility).
- `os` is ideal for lightweight scripting or automation but not for complex file manipulations — use `shutil` for more control.
- `os.environ` gives access to environment variables — useful for secrets or configurations.

---

## 6. Related Domains

- **Cybersecurity:** Read hidden files, manipulate environment variables, or write scripts for enumeration.
- **Automation:** Rename, move, or delete files automatically as part of scripts.
- **Data Science:** Organize datasets, automate cleaning, or create log directories dynamically.
- **DevOps:** Read environment config, prepare directories, or validate deployments.

---

> ✅ This file is ready to be added to your GitHub repo under:  
> `Super_H4k3r/1-Python/Level5/os_module_guide.md`
