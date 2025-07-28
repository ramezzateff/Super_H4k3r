# 🐧 Linux: File & Permissions Tasks

This task set focuses on hands-on Linux file system operations, permission handling, and disk usage analysis. You’ll practice everything from creating files and symbolic links to managing permissions and monitoring storage.

---

## 📂 Tasks Overview

| # | Task Description | File |
|--:|------------------|------|
| 1️⃣ | Create a file and write `"Hello Linux"` into it. | `01_create_file.sh` |
| 2️⃣ | Check the size of a specific file in bytes. | `02_file_size.sh` |
| 3️⃣ | List all files (including hidden) in a directory with their permissions and sizes. | `03_list_files.sh` |
| 4️⃣ | Change the permissions of a script to make it executable. | `04_make_executable.sh` |
| 5️⃣ | Recursively change the owner of all files in a directory to a specific user. | `05_chown_recursive.sh` |
| 6️⃣ | Find all files larger than 100MB on the system. | `06_find_large_files.sh` |
| 7️⃣ | Create a symbolic link to an existing file. | `07_symlink.sh` |
| 8️⃣ | Display the owner and permissions of a file. | `08_file_owner_perm.sh` |
| 9️⃣ | Compare the contents of two text files. | `09_compare_files.sh` |
| 🔟 | Show the disk usage of each subdirectory inside `/home`. | `10_disk_usage_home.sh` |

---

## 🛠 Folder Structure
├── 01_create_file.sh
├── 02_file_size.sh
├── 03_list_files.sh
├── 04_make_executable.sh
├── 05_chown_recursive.sh
├── 06_find_large_files.sh
├── 07_symlink.sh
├── 08_file_owner_perm.sh
├── 09_compare_files.sh
└── 10_disk_usage_home.sh


---

## 💡 Notes

- Scripts should be executable (`chmod +x script.sh`)
- Use safe and non-destructive commands while testing
- All commands should be POSIX-compliant (`bash` or `sh`)

---

## ✅ Output Example

For each script, the output should be printed clearly to the terminal.  
Example for `01_create_file.sh`:

