# 📘 Bash Scripting for Absolute Beginners

Welcome to your **first step into the world of Bash scripting!**
This guide is for anyone who knows how to use Linux and the terminal, but has *zero* experience with scripting or programming.

We'll go step by step, keeping things simple, clear, and practical.

---

## 1. 🐚 Introduction to Bash Scripting

### What is Bash?

Bash stands for **Bourne Again SHell**. It's the most common command-line shell used on Linux.
It's what you use when typing commands into the terminal.

### What is a Bash Script?

A Bash script is just a **text file** containing a series of Bash commands. Instead of typing each command manually, you save them in a file and run them all at once.

### Why Use Bash Scripts?

* Automate boring or repetitive tasks
* Run multiple commands together
* Build small tools and systems

### How to Run a Bash Script

1. Write your script in a file (e.g. `myscript.sh`)
2. Make it executable: `chmod +x myscript.sh`
3. Run it: `./myscript.sh`

---

## 2. 🖊️ First Script and Syntax Basics

### Your First Script

Create a file called `hello.sh` and write this:

```bash
#!/bin/bash

echo "Hello, world!"
```

### What is `#!/bin/bash`?

This is called a **shebang**. It tells Linux to run the script using Bash.

### The `echo` Command

`echo` is used to print text on the screen:

```bash
echo "Welcome to Bash!"
echo "Today's date is: $(date)"
```

---

## 3. 🔢 Variables and User Input

### Declaring Variables

```bash
name="Ramez"
echo "Hello, $name!"
```

Note: **No spaces** around `=` when assigning variables.

### Reading User Input

```bash
echo "What's your name?"
read username
echo "Nice to meet you, $username!"
```

### Quoting and Escaping

* Use `"double quotes"` when referencing variables.
* Use `\` to escape characters:

```bash
echo "He said: \"Hello\""
```

---

## 4. 🔁 Conditions and Logic

### if, else, elif

```bash
if [ $age -ge 18 ]; then
  echo "You're an adult."
elif [ $age -ge 13 ]; then
  echo "You're a teenager."
else
  echo "You're a child."
fi
```

### Comparison Operators

| Type    | Operator | Meaning        |
| ------- | -------- | -------------- |
| Numbers | `-eq`    | equal          |
|         | `-ne`    | not equal      |
|         | `-gt`    | greater than   |
|         | `-lt`    | less than      |
| Strings | `=`      | equal          |
|         | `!=`     | not equal      |
| Files   | `-f`     | is a file      |
|         | `-d`     | is a directory |

### `[[ ]]` vs `[ ]`

Both are used to test conditions. `[[ ]]` is newer and safer.

---

## 5. 🔂 Loops and Repetition

### for loop

```bash
for name in Ramez Sarah Ali; do
  echo "Hello $name"
done
```

### while loop

```bash
count=1
while [ $count -le 5 ]; do
  echo "Count is $count"
  ((count++))
done
```

### break and continue

```bash
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    continue
  fi
  echo $i
  if [ $i -eq 8 ]; then
    break
  fi
done
```

---

## 6. 🧩 Functions in Bash

### Defining and Calling Functions

```bash
say_hello() {
  echo "Hello, $1!"
}

say_hello Ramez
```

### Return Values

```bash
add() {
  result=$(( $1 + $2 ))
  echo $result
}

sum=$(add 3 5)
echo "Sum is $sum"
```

---

## 7. 📂 Working with Files and Directories

### Check if File or Directory Exists

```bash
if [ -f file.txt ]; then
  echo "File exists."
fi
```

### Read File Line by Line

```bash
while read line; do
  echo "Line: $line"
done < file.txt
```

### Create and Write to a File

```bash
echo "Hello" > file.txt   # overwrite
echo "World" >> file.txt  # append
```

---

## 8. 🛠 Useful Bash Commands

| Command | What it Does                    |
| ------- | ------------------------------- |
| `cat`   | Shows contents of a file        |
| `grep`  | Searches for text in files      |
| `cut`   | Cuts sections of text           |
| `awk`   | Text processing (e.g. column 1) |
| `sed`   | Replaces text in files          |
| `wc`    | Word/line count                 |
| `sort`  | Sorts lines in a file           |
| `uniq`  | Removes duplicates              |
| `xargs` | Builds command lines from input |

Examples:

```bash
grep "error" logs.txt
cut -d":" -f1 file.txt
awk '{print $1}' file.txt
sed 's/old/new/g' file.txt
```

---

## 9. 💻 System Information Scripting

```bash
echo "OS: $(uname -o)"
echo "Kernel: $(uname -r)"
echo "CPU: $(lscpu | grep 'Model name')"
echo "RAM: $(free -h | grep Mem)"
echo "Disk: $(df -h | grep '^/')"
echo "Uptime: $(uptime -p)"
echo "IP: $(hostname -I)"
echo "Hostname: $(hostname)"
```

---

## 10. 🎯 Script Arguments and Exit Codes

### Script Arguments

```bash
# script.sh
echo "First arg: $1"
echo "All args: $@"
echo "Number of args: $#"
```

### Exit Codes

```bash
if [ ! -f myfile ]; then
  echo "File missing"
  exit 1
fi
```

### trap and set

```bash
trap "echo Goodbye!" EXIT
set -e  # stop script on error
```

---

## 11. ✅ Real-World Bash Scripting Examples

### Monitor CPU and RAM

```bash
while true; do
  clear
  echo "CPU:"
  top -bn1 | grep "Cpu(s)"
  echo "\nMemory:"
  free -h
  sleep 2
done
```

### Backup a Directory

```bash
backup_dir="backup_$(date +%F_%T)"
mkdir $backup_dir
cp -r myfolder/* $backup_dir
echo "Backup done at $backup_dir"
```

### Find and Kill a Process

```bash
ps aux | grep firefox
kill $(pgrep firefox)
```

### Analyze Log File

```bash
grep "ERROR" app.log | wc -l
```

---

## 12. 📏 Best Practices

* Use `#!/bin/bash` at the top
* Use functions for reuse
* Add comments to explain steps
* Use `set -e` to stop on errors
* Use clear and meaningful variable names
* Test your scripts in parts

---

## 13. 📚 Resources and Next Steps

* Practice:

  * [https://www.hackerrank.com/domains/tutorials/10-days-of-linux](https://www.hackerrank.com/domains/tutorials/10-days-of-linux)
  * [https://linuxcommand.org/lc3\_learning\_the\_shell.php](https://linuxcommand.org/lc3_learning_the_shell.php)

* GitHub Repos:

  * `github.com/dylanaraps/pure-bash-bible`
  * `github.com/Idnan/bash-guide`

* Combine with Python:

  * Use Bash to automate
  * Use Python for complex processing
  * Call Python scripts from Bash using: `python3 script.py`

---

Happy scripting! 🎉
