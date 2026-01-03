---
layout: default
title: Shell Programming
---

# Shell Programming

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Shell](#introduction-to-shell)
- [Types of Shells](#types-of-shells)
- [Shell Scripting Basics](#shell-scripting-basics)
- [Variables](#variables)
- [Operators](#operators)
- [Control Structures](#control-structures)
- [Loops](#loops)
- [Functions](#functions)
- [Arrays](#arrays)
- [File Operations](#file-operations)
- [Input/Output](#inputoutput)
- [Practical Examples](#practical-examples)

---

## Introduction to Shell

### What is a Shell?

> A **Shell** is a command-line interpreter that provides a user interface to the operating system services. It acts as an intermediary between the user and the kernel.

```
┌─────────────────────────────────────────┐
│              User                       │
│               ↓                         │
│    ┌─────────────────────┐              │
│    │       Shell         │              │
│    │  (Command Interpreter)             │
│    └─────────────────────┘              │
│               ↓                         │
│    ┌─────────────────────┐              │
│    │       Kernel        │              │
│    └─────────────────────┘              │
│               ↓                         │
│           Hardware                      │
└─────────────────────────────────────────┘
```

### Shell Functions

1. **Command Interpretation**: Parses and executes commands
2. **Programming Language**: Supports scripting
3. **Environment Customization**: Allows personalization
4. **Pipe and Redirection**: Connects commands

---

## Types of Shells

| Shell | Path | Description |
|-------|------|-------------|
| **Bourne Shell (sh)** | `/bin/sh` | Original UNIX shell |
| **Bash (Bourne Again)** | `/bin/bash` | Most popular, default on most Linux |
| **C Shell (csh)** | `/bin/csh` | C-like syntax |
| **Korn Shell (ksh)** | `/bin/ksh` | Enhanced Bourne shell |
| **Z Shell (zsh)** | `/bin/zsh` | Extended bash with more features |
| **Fish** | `/usr/bin/fish` | User-friendly, modern shell |

### Checking Current Shell

```bash
echo $SHELL         # Default shell
echo $0             # Current shell
cat /etc/shells     # Available shells
```

---

## Shell Scripting Basics

### Creating a Shell Script

```bash
#!/bin/bash
# This is a comment
# Script: hello.sh

echo "Hello, World!"
```

### Making Script Executable

```bash
chmod +x hello.sh
./hello.sh
```

### Script Execution Methods

```bash
# Method 1: Direct execution (needs execute permission)
./script.sh

# Method 2: Using bash interpreter
bash script.sh

# Method 3: Source (runs in current shell)
source script.sh
. script.sh
```

### Shebang Line

The first line `#!/bin/bash` is called the **shebang** or **hashbang**. It tells the system which interpreter to use.

```bash
#!/bin/bash      # Use Bash
#!/bin/sh        # Use Bourne shell
#!/usr/bin/env python3   # Use Python
```

---

## Variables

### Declaring Variables

```bash
# No spaces around =
name="John"
age=25
pi=3.14

# Using variables
echo $name
echo ${name}        # Preferred for clarity
echo "Hello, $name"
echo "Hello, ${name}!"
```

### Variable Types

```bash
# String variables
greeting="Hello World"

# Numeric variables
count=10

# Read-only variables
readonly PI=3.14159

# Remove variable
unset name
```

### Special Variables

| Variable | Description |
|----------|-------------|
| `$0` | Script name |
| `$1, $2, ...` | Positional parameters |
| `$#` | Number of arguments |
| `$@` | All arguments (separate strings) |
| `$*` | All arguments (single string) |
| `$?` | Exit status of last command |
| `$$` | Current process ID |
| `$!` | Last background process ID |

### Example: Using Special Variables

```bash
#!/bin/bash
# script: args.sh

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Number of arguments: $#"
echo "All arguments: $@"
echo "Process ID: $$"
```

### Command Substitution

```bash
# Using $()
current_date=$(date)
file_count=$(ls | wc -l)

# Using backticks (older, less preferred)
current_date=`date`

echo "Today is: $current_date"
echo "Files in directory: $file_count"
```

### Environment Variables

```bash
# View all environment variables
env
printenv

# Common environment variables
echo $HOME      # Home directory
echo $PATH      # Executable paths
echo $USER      # Current user
echo $PWD       # Current directory

# Export variable to child processes
export MY_VAR="value"
```

---

## Operators

### Arithmetic Operators

```bash
# Using let
let "sum = 5 + 3"
let "product = 5 * 3"

# Using $(( ))
result=$((10 + 5))
result=$((10 - 5))
result=$((10 * 5))
result=$((10 / 5))
result=$((10 % 3))   # Modulus
result=$((2 ** 3))   # Exponentiation

# Using expr
result=$(expr 10 + 5)
result=$(expr 10 \* 5)  # Escape *
```

### Comparison Operators (Numeric)

| Operator | Description |
|----------|-------------|
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `-gt` | Greater than |
| `-lt` | Less than |
| `-ge` | Greater than or equal |
| `-le` | Less than or equal |

### Comparison Operators (String)

| Operator | Description |
|----------|-------------|
| `=` or `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than (ASCII) |
| `>` | Greater than (ASCII) |
| `-z` | String is empty |
| `-n` | String is not empty |

### File Test Operators

| Operator | Description |
|----------|-------------|
| `-e` | File exists |
| `-f` | Is a regular file |
| `-d` | Is a directory |
| `-r` | Is readable |
| `-w` | Is writable |
| `-x` | Is executable |
| `-s` | File size > 0 |
| `-L` | Is a symbolic link |

### Logical Operators

| Operator | Description |
|----------|-------------|
| `!` | NOT |
| `-a` or `&&` | AND |
| `-o` or `||` | OR |

---

## Control Structures

### if Statement

```bash
# Basic if
if [ condition ]; then
    commands
fi

# if-else
if [ condition ]; then
    commands
else
    commands
fi

# if-elif-else
if [ condition1 ]; then
    commands
elif [ condition2 ]; then
    commands
else
    commands
fi
```

### Examples

```bash
#!/bin/bash

# Numeric comparison
age=20
if [ $age -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are a minor"
fi

# String comparison
name="John"
if [ "$name" = "John" ]; then
    echo "Hello, John!"
fi

# File check
if [ -f "/etc/passwd" ]; then
    echo "File exists"
fi

# Multiple conditions
if [ $age -ge 18 ] && [ $age -lt 65 ]; then
    echo "Working age"
fi
```

### Using [[ ]] (Extended Test)

```bash
# Better string handling
if [[ "$string" == "pattern"* ]]; then
    echo "Matches pattern"
fi

# Regex matching
if [[ "$email" =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]]; then
    echo "Valid email format"
fi
```

### case Statement

```bash
#!/bin/bash

fruit="apple"

case $fruit in
    "apple")
        echo "It's an apple"
        ;;
    "banana"|"orange")
        echo "It's a banana or orange"
        ;;
    *)
        echo "Unknown fruit"
        ;;
esac
```

### Menu Example

```bash
#!/bin/bash

echo "Select an option:"
echo "1. Display date"
echo "2. Display users"
echo "3. Display uptime"
echo "4. Exit"

read choice

case $choice in
    1) date ;;
    2) who ;;
    3) uptime ;;
    4) exit 0 ;;
    *) echo "Invalid option" ;;
esac
```

---

## Loops

### for Loop

```bash
# List iteration
for item in apple banana cherry; do
    echo "Fruit: $item"
done

# Range (Bash 3+)
for i in {1..5}; do
    echo "Number: $i"
done

# Range with step
for i in {0..10..2}; do
    echo "Even: $i"
done

# C-style for loop
for ((i=1; i<=5; i++)); do
    echo "Count: $i"
done

# Iterate over files
for file in *.txt; do
    echo "Processing: $file"
done

# Iterate over command output
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done
```

### while Loop

```bash
#!/bin/bash

# Basic while loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Reading file line by line
while read line; do
    echo "Line: $line"
done < filename.txt

# Infinite loop
while true; do
    echo "Running..."
    sleep 1
done
```

### until Loop

```bash
#!/bin/bash

# Until loop (opposite of while)
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### Loop Control

```bash
# break - exit loop
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done

# continue - skip iteration
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue
    fi
    echo $i
done
```

---

## Functions

### Defining Functions

```bash
# Method 1
function greet {
    echo "Hello, $1!"
}

# Method 2 (POSIX compliant)
greet() {
    echo "Hello, $1!"
}

# Calling function
greet "World"
greet "John"
```

### Function with Return Value

```bash
#!/bin/bash

add() {
    local sum=$(($1 + $2))
    echo $sum
}

# Capture return value
result=$(add 5 3)
echo "Sum: $result"
```

### Function with Local Variables

```bash
#!/bin/bash

calculate() {
    local num1=$1
    local num2=$2
    local result=$((num1 * num2))
    echo $result
}

result=$(calculate 4 5)
echo "Product: $result"
```

### Recursive Function

```bash
#!/bin/bash

factorial() {
    if [ $1 -le 1 ]; then
        echo 1
    else
        local prev=$(factorial $(($1 - 1)))
        echo $(($1 * prev))
    fi
}

echo "Factorial of 5: $(factorial 5)"
```

---

## Arrays

### Declaring Arrays

```bash
# Method 1: Direct declaration
fruits=("apple" "banana" "cherry")

# Method 2: Individual assignment
colors[0]="red"
colors[1]="green"
colors[2]="blue"

# Method 3: Using declare
declare -a numbers=(1 2 3 4 5)
```

### Accessing Array Elements

```bash
# Single element
echo ${fruits[0]}       # First element
echo ${fruits[1]}       # Second element

# All elements
echo ${fruits[@]}       # All elements
echo ${fruits[*]}       # All as single string

# Array length
echo ${#fruits[@]}      # Number of elements

# Length of element
echo ${#fruits[0]}      # Length of first element
```

### Array Operations

```bash
#!/bin/bash

fruits=("apple" "banana" "cherry")

# Add element
fruits+=("date")

# Remove element
unset fruits[1]

# Iterate over array
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Slice array
echo ${fruits[@]:1:2}   # Elements 1 and 2

# Get indices
echo ${!fruits[@]}      # Print indices
```

### Associative Arrays (Bash 4+)

```bash
#!/bin/bash

# Declare associative array
declare -A user

user["name"]="John"
user["age"]=30
user["city"]="New York"

# Access elements
echo "Name: ${user["name"]}"
echo "Age: ${user["age"]}"

# Iterate
for key in "${!user[@]}"; do
    echo "$key: ${user[$key]}"
done
```

---

## File Operations

### Reading Files

```bash
#!/bin/bash

# Read entire file
content=$(cat filename.txt)

# Read line by line
while IFS= read -r line; do
    echo "Line: $line"
done < filename.txt

# Read with line numbers
line_num=1
while read line; do
    echo "$line_num: $line"
    ((line_num++))
done < filename.txt
```

### Writing to Files

```bash
#!/bin/bash

# Overwrite file
echo "Hello World" > output.txt

# Append to file
echo "New line" >> output.txt

# Write multiple lines
cat > output.txt << EOF
Line 1
Line 2
Line 3
EOF

# Here document
cat << EOF
This is a here document.
It can span multiple lines.
Variables work: $HOME
EOF
```

### File Testing

```bash
#!/bin/bash

file="/etc/passwd"

if [ -e "$file" ]; then
    echo "File exists"
fi

if [ -f "$file" ]; then
    echo "It's a regular file"
fi

if [ -d "/home" ]; then
    echo "It's a directory"
fi

if [ -r "$file" ]; then
    echo "File is readable"
fi

if [ -w "$file" ]; then
    echo "File is writable"
fi

if [ -x "$file" ]; then
    echo "File is executable"
fi

if [ -s "$file" ]; then
    echo "File is not empty"
fi
```

---

## Input/Output

### Reading User Input

```bash
#!/bin/bash

# Basic read
echo "Enter your name:"
read name
echo "Hello, $name!"

# Read with prompt
read -p "Enter your age: " age

# Read silently (for passwords)
read -s -p "Enter password: " password
echo

# Read with timeout
read -t 5 -p "Quick! Enter something: " input

# Read into array
read -a colors -p "Enter colors: "
echo "First color: ${colors[0]}"
```

### select Statement (Menu)

```bash
#!/bin/bash

echo "Select your favorite fruit:"

select fruit in "Apple" "Banana" "Cherry" "Quit"; do
    case $fruit in
        "Apple")
            echo "You selected Apple"
            ;;
        "Banana")
            echo "You selected Banana"
            ;;
        "Cherry")
            echo "You selected Cherry"
            ;;
        "Quit")
            echo "Goodbye!"
            break
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
done
```

### Formatting Output

```bash
#!/bin/bash

# printf for formatted output
printf "Name: %s\n" "John"
printf "Age: %d\n" 25
printf "Price: %.2f\n" 19.99
printf "%-10s %5d\n" "Item" 100

# Table formatting
printf "%-15s %-10s %10s\n" "Name" "Age" "Salary"
printf "%-15s %-10d %10.2f\n" "John" 30 50000.00
printf "%-15s %-10d %10.2f\n" "Jane" 25 45000.50
```

---

## Practical Examples

### Example 1: Backup Script

```bash
#!/bin/bash

# Backup script
# Usage: ./backup.sh source_dir backup_dir

SOURCE=$1
BACKUP=$2
DATE=$(date +%Y%m%d_%H%M%S)

if [ -z "$SOURCE" ] || [ -z "$BACKUP" ]; then
    echo "Usage: $0 source_dir backup_dir"
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "Error: Source directory does not exist"
    exit 1
fi

mkdir -p "$BACKUP"

ARCHIVE="$BACKUP/backup_$DATE.tar.gz"
tar -czf "$ARCHIVE" "$SOURCE"

if [ $? -eq 0 ]; then
    echo "Backup successful: $ARCHIVE"
else
    echo "Backup failed!"
    exit 1
fi
```

### Example 2: System Monitor

```bash
#!/bin/bash

# System monitoring script

clear
echo "================================"
echo "      SYSTEM MONITOR"
echo "================================"
echo

echo "--- System Information ---"
echo "Hostname: $(hostname)"
echo "Kernel: $(uname -r)"
echo "Uptime: $(uptime -p)"
echo

echo "--- Memory Usage ---"
free -h | head -2
echo

echo "--- Disk Usage ---"
df -h | grep -E '^/dev/'
echo

echo "--- Top 5 Processes (CPU) ---"
ps aux --sort=-%cpu | head -6
echo

echo "--- Logged in Users ---"
who
```

### Example 3: Log Analyzer

```bash
#!/bin/bash

# Log file analyzer

LOGFILE=${1:-/var/log/syslog}

if [ ! -f "$LOGFILE" ]; then
    echo "Log file not found: $LOGFILE"
    exit 1
fi

echo "Analyzing: $LOGFILE"
echo "========================"

echo -e "\nTotal lines: $(wc -l < "$LOGFILE")"
echo -e "\nError count: $(grep -ci 'error' "$LOGFILE")"
echo -e "Warning count: $(grep -ci 'warning' "$LOGFILE")"

echo -e "\n--- Last 10 errors ---"
grep -i 'error' "$LOGFILE" | tail -10
```

### Example 4: User Creation Script

```bash
#!/bin/bash

# User creation script (requires root)

if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

read -p "Enter username: " username
read -s -p "Enter password: " password
echo
read -p "Enter full name: " fullname

# Check if user exists
if id "$username" &>/dev/null; then
    echo "User already exists"
    exit 1
fi

# Create user
useradd -m -c "$fullname" "$username"
echo "$username:$password" | chpasswd

if [ $? -eq 0 ]; then
    echo "User $username created successfully"
else
    echo "Failed to create user"
    exit 1
fi
```

### Example 5: Calculator

```bash
#!/bin/bash

# Simple calculator

calculator() {
    echo "Simple Calculator"
    echo "=================="
    
    read -p "Enter first number: " num1
    read -p "Enter operator (+, -, *, /): " operator
    read -p "Enter second number: " num2
    
    case $operator in
        +)
            result=$(echo "$num1 + $num2" | bc)
            ;;
        -)
            result=$(echo "$num1 - $num2" | bc)
            ;;
        \*)
            result=$(echo "$num1 * $num2" | bc)
            ;;
        /)
            if [ "$num2" = "0" ]; then
                echo "Error: Division by zero"
                return 1
            fi
            result=$(echo "scale=2; $num1 / $num2" | bc)
            ;;
        *)
            echo "Invalid operator"
            return 1
            ;;
    esac
    
    echo "Result: $num1 $operator $num2 = $result"
}

calculator
```

---

## Best Practices

1. **Always quote variables**: `"$variable"` prevents word splitting
2. **Use meaningful variable names**: `user_count` instead of `uc`
3. **Add comments**: Explain complex logic
4. **Check command success**: Use `$?` or `if command; then`
5. **Handle errors**: Validate inputs and handle edge cases
6. **Use functions**: Organize code into reusable functions
7. **Use `set -e`**: Exit on first error
8. **Use `set -u`**: Exit on undefined variables
9. **Use shellcheck**: Lint your scripts

---

## Summary

- Shell is a command interpreter between user and kernel
- Bash is the most common shell on Linux
- Scripts start with shebang (`#!/bin/bash`)
- Variables store data; special variables provide script info
- Control structures include if, case, for, while, until
- Functions provide code reusability
- Arrays store collections of data
- Proper error handling is essential

---

[← Previous: Introduction to Linux](02-introduction-to-linux.md) | [Next: Processes →](04-processes.md)
