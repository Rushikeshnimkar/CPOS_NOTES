---
layout: default
title: Introduction to Linux
---

# Introduction to Linux

[← Back to Home](../index.md)

---

## Table of Contents
- [History of Linux](#history-of-linux)
- [Linux Architecture](#linux-architecture)
- [Linux Distributions](#linux-distributions)
- [Linux File System Hierarchy](#linux-file-system-hierarchy)
- [Basic Linux Commands](#basic-linux-commands)
- [User and Permission Management](#user-and-permission-management)
- [File Permissions](#file-permissions)
- [Package Management](#package-management)

---

## History of Linux

### Timeline

| Year | Event |
|------|-------|
| 1969 | UNIX developed at AT&T Bell Labs |
| 1983 | Richard Stallman starts GNU Project |
| 1991 | Linus Torvalds releases Linux kernel 0.01 |
| 1992 | Linux released under GNU GPL |
| 1993 | Slackware and Debian distributions released |
| 1994 | Linux kernel 1.0 released |
| 2004 | Ubuntu 4.10 released |
| Present | Linux powers servers, Android, supercomputers |

### Key Figures

- **Linus Torvalds**: Created Linux kernel
- **Richard Stallman**: Started GNU Project, free software movement
- **Dennis Ritchie & Ken Thompson**: Created UNIX

### What is Linux?

> Linux is a free, open-source, UNIX-like operating system kernel first released by Linus Torvalds in 1991.

**Key Characteristics:**
- **Open Source**: Source code is freely available
- **Multi-user**: Multiple users can use simultaneously
- **Multi-tasking**: Multiple processes can run concurrently
- **Portable**: Runs on various hardware architectures
- **Secure**: Strong security features
- **Stable**: Known for reliability

---

## Linux Architecture

```
┌────────────────────────────────────────────────────┐
│                   User Space                       │
│  ┌──────────────────────────────────────────────┐ │
│  │            Applications                       │ │
│  │   (Web Browser, Text Editor, Terminal, etc.) │ │
│  └──────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────┐ │
│  │              Shell (Bash, Zsh)                │ │
│  └──────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────┐ │
│  │          System Libraries (glibc)             │ │
│  └──────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────┤
│                  Kernel Space                      │
│  ┌──────────────────────────────────────────────┐ │
│  │              Linux Kernel                     │ │
│  │  ┌────────────┬────────────┬───────────────┐ │ │
│  │  │ Process    │ Memory     │ File System   │ │ │
│  │  │ Management │ Management │ Management    │ │ │
│  │  ├────────────┼────────────┼───────────────┤ │ │
│  │  │ Device     │ Network    │ System Call   │ │ │
│  │  │ Drivers    │ Stack      │ Interface     │ │ │
│  │  └────────────┴────────────┴───────────────┘ │ │
│  └──────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────┤
│                    Hardware                        │
│       CPU │ Memory │ Disk │ Network │ Devices      │
└────────────────────────────────────────────────────┘
```

### Components

| Component | Description |
|-----------|-------------|
| **Kernel** | Core of the OS, manages hardware resources |
| **Shell** | Command interpreter, interface between user and kernel |
| **System Libraries** | Functions that help applications interact with kernel |
| **System Utilities** | Essential tools and programs |
| **Applications** | User programs |

---

## Linux Distributions

A **Linux distribution** (distro) is a complete OS built around the Linux kernel with additional software.

### Popular Distributions

| Distribution | Based On | Use Case | Package Manager |
|--------------|----------|----------|-----------------|
| **Ubuntu** | Debian | Desktop, Server, Cloud | apt |
| **Debian** | - | Server, Stability | apt |
| **Fedora** | Red Hat | Desktop, Cutting-edge | dnf |
| **CentOS/Rocky** | RHEL | Enterprise Server | yum/dnf |
| **Arch Linux** | - | Advanced Users | pacman |
| **Linux Mint** | Ubuntu | Desktop Beginners | apt |
| **Kali Linux** | Debian | Security/Pentesting | apt |
| **Alpine** | - | Containers | apk |

### Distribution Family Tree

```
         ┌─── Debian ─┬─── Ubuntu ──── Linux Mint
         │            └─── Kali Linux
UNIX ────┤
         │            ┌─── CentOS / Rocky Linux
         └─── Red Hat ┤
                      └─── Fedora
```

---

## Linux File System Hierarchy

```
/                     (Root directory)
├── bin/              (Essential user binaries)
├── boot/             (Boot loader files)
├── dev/              (Device files)
├── etc/              (System configuration files)
├── home/             (User home directories)
│   └── username/     (Individual user's home)
├── lib/              (Essential shared libraries)
├── media/            (Removable media mount points)
├── mnt/              (Temporary mount points)
├── opt/              (Optional software packages)
├── proc/             (Process information - virtual)
├── root/             (Root user's home directory)
├── sbin/             (System binaries)
├── sys/              (System information - virtual)
├── tmp/              (Temporary files)
├── usr/              (User utilities and applications)
│   ├── bin/          (User binaries)
│   ├── lib/          (Libraries)
│   ├── local/        (Locally installed software)
│   └── share/        (Shared data)
└── var/              (Variable data files)
    ├── log/          (Log files)
    ├── tmp/          (Temporary files)
    └── www/          (Web server files)
```

### Important Directories

| Directory | Purpose |
|-----------|---------|
| `/` | Root, top of the hierarchy |
| `/bin` | Essential command binaries (ls, cp, mv) |
| `/etc` | Configuration files |
| `/home` | User home directories |
| `/var` | Variable data (logs, mail, databases) |
| `/tmp` | Temporary files (cleared on reboot) |
| `/usr` | User utilities and applications |
| `/opt` | Optional/third-party software |

---

## Basic Linux Commands

### Navigation Commands

```bash
# Print working directory
pwd

# List directory contents
ls              # List files
ls -l           # Long format (detailed)
ls -a           # Show hidden files
ls -la          # Long format with hidden files
ls -lh          # Human-readable sizes

# Change directory
cd /path/to/dir     # Go to specific directory
cd ~                # Go to home directory
cd ..               # Go up one level
cd -                # Go to previous directory
```

### File Operations

```bash
# Create files and directories
touch filename          # Create empty file
mkdir dirname           # Create directory
mkdir -p dir1/dir2      # Create nested directories

# Copy files
cp source dest          # Copy file
cp -r source dest       # Copy directory recursively

# Move/Rename files
mv source dest          # Move or rename

# Remove files
rm filename             # Remove file
rm -r dirname           # Remove directory recursively
rm -f filename          # Force remove
rm -rf dirname          # Force remove directory

# View file contents
cat filename            # Display entire file
less filename           # Page through file
head filename           # First 10 lines
head -n 20 filename     # First 20 lines
tail filename           # Last 10 lines
tail -f filename        # Follow file (for logs)
```

### File Content Operations

```bash
# Search in files
grep "pattern" filename         # Search for pattern
grep -r "pattern" directory     # Recursive search
grep -i "pattern" filename      # Case insensitive
grep -n "pattern" filename      # Show line numbers

# Text processing
wc filename             # Word, line, character count
wc -l filename          # Line count only
sort filename           # Sort lines
uniq filename           # Remove duplicates
cut -d',' -f1 file      # Extract first field
```

### System Information

```bash
# System information
uname -a                # All system info
hostname                # Show hostname
uptime                  # System uptime
whoami                  # Current user

# Disk usage
df -h                   # Disk space usage
du -sh directory        # Directory size

# Memory usage
free -h                 # Memory usage

# Process information
ps                      # Current processes
ps aux                  # All processes
top                     # Interactive process viewer
htop                    # Enhanced process viewer
```

### File Permissions

```bash
# Change permissions
chmod 755 filename      # rwxr-xr-x
chmod +x filename       # Add execute permission
chmod u+w filename      # Add write for user

# Change ownership
chown user filename             # Change owner
chown user:group filename       # Change owner and group
chgrp group filename            # Change group only
```

### Networking

```bash
# Network information
ip addr                 # IP addresses
ifconfig                # Network interfaces (older)
ping hostname           # Test connectivity
curl url                # Fetch URL content
wget url                # Download file

# Network diagnostics
netstat -an             # Network connections
ss -an                  # Socket statistics
traceroute hostname     # Trace packet route
```

### Package Management

```bash
# Debian/Ubuntu (apt)
sudo apt update                 # Update package list
sudo apt upgrade                # Upgrade packages
sudo apt install package        # Install package
sudo apt remove package         # Remove package
sudo apt search keyword         # Search packages

# RHEL/CentOS (yum/dnf)
sudo yum update                 # Update packages
sudo yum install package        # Install package
sudo dnf install package        # Install (newer)

# Arch Linux (pacman)
sudo pacman -Syu                # Update system
sudo pacman -S package          # Install package
```

---

## User and Permission Management

### User Management Commands

```bash
# User operations
sudo useradd username           # Create user
sudo useradd -m username        # Create with home directory
sudo userdel username           # Delete user
sudo userdel -r username        # Delete with home directory
sudo passwd username            # Set/change password

# Group operations
sudo groupadd groupname         # Create group
sudo groupdel groupname         # Delete group
sudo usermod -aG group user     # Add user to group

# View user info
id username                     # User and group IDs
groups username                 # User's groups
cat /etc/passwd                 # All users
cat /etc/group                  # All groups
```

### User Files

| File | Purpose |
|------|---------|
| `/etc/passwd` | User account information |
| `/etc/shadow` | Encrypted passwords |
| `/etc/group` | Group information |
| `/etc/sudoers` | Sudo configuration |

### /etc/passwd Format

```
username:password:UID:GID:comment:home:shell
```

Example:
```
john:x:1001:1001:John Doe:/home/john:/bin/bash
```

---

## File Permissions

### Understanding Permissions

```
-rwxr-xr-- 1 user group 4096 Jan 1 10:00 filename
│├─┤├─┤├─┤
││  │  │
││  │  └── Others permissions (r--)
││  └───── Group permissions (r-x)
│└──────── User/Owner permissions (rwx)
└───────── File type (- = regular, d = directory, l = link)
```

### Permission Types

| Symbol | Meaning | File | Directory |
|--------|---------|------|-----------|
| `r` | Read | View contents | List contents |
| `w` | Write | Modify contents | Create/delete files |
| `x` | Execute | Run as program | Enter directory |
| `-` | No permission | - | - |

### Numeric (Octal) Permissions

| Number | Permission | Binary |
|--------|------------|--------|
| 0 | --- | 000 |
| 1 | --x | 001 |
| 2 | -w- | 010 |
| 3 | -wx | 011 |
| 4 | r-- | 100 |
| 5 | r-x | 101 |
| 6 | rw- | 110 |
| 7 | rwx | 111 |

### Common Permission Settings

| Octal | Symbolic | Use Case |
|-------|----------|----------|
| 755 | rwxr-xr-x | Executable, readable by all |
| 644 | rw-r--r-- | Regular files |
| 700 | rwx------ | Private scripts |
| 600 | rw------- | Private files |
| 777 | rwxrwxrwx | Full access (avoid!) |

### Changing Permissions

```bash
# Symbolic method
chmod u+x file          # Add execute for user
chmod g-w file          # Remove write for group
chmod o=r file          # Set others to read only
chmod a+r file          # Add read for all

# Numeric method
chmod 755 file          # rwxr-xr-x
chmod 644 file          # rw-r--r--
chmod 600 file          # rw-------
```

### Special Permissions

| Permission | Octal | Effect |
|------------|-------|--------|
| SUID | 4000 | Run with owner's privileges |
| SGID | 2000 | Run with group's privileges |
| Sticky Bit | 1000 | Only owner can delete files |

```bash
# Set special permissions
chmod 4755 file         # SUID + rwxr-xr-x
chmod 2755 directory    # SGID
chmod 1777 directory    # Sticky bit
```

---

## Package Management

### APT (Debian/Ubuntu)

```bash
# Update and upgrade
sudo apt update                 # Update package lists
sudo apt upgrade                # Upgrade installed packages
sudo apt full-upgrade           # Full system upgrade

# Install and remove
sudo apt install package        # Install
sudo apt remove package         # Remove (keep config)
sudo apt purge package          # Remove completely
sudo apt autoremove             # Remove unused packages

# Search and info
apt search keyword              # Search packages
apt show package                # Package information
apt list --installed            # List installed packages
```

### YUM/DNF (Red Hat/CentOS/Fedora)

```bash
# Basic operations
sudo dnf update                 # Update all packages
sudo dnf install package        # Install package
sudo dnf remove package         # Remove package

# Search and info
dnf search keyword              # Search
dnf info package                # Package info
dnf list installed              # List installed
```

### Pacman (Arch Linux)

```bash
sudo pacman -Syu                # Sync and update
sudo pacman -S package          # Install package
sudo pacman -R package          # Remove package
sudo pacman -Ss keyword         # Search
```

---

## Useful Tips

### Command Line Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + C` | Cancel current command |
| `Ctrl + Z` | Suspend current command |
| `Ctrl + D` | Exit shell |
| `Ctrl + L` | Clear screen |
| `Ctrl + A` | Move to beginning of line |
| `Ctrl + E` | Move to end of line |
| `Tab` | Auto-complete |
| `↑ / ↓` | Command history |

### Piping and Redirection

```bash
# Piping (|) - send output to another command
ls -l | grep ".txt"             # Filter output
cat file | sort | uniq          # Chain commands

# Redirection
command > file          # Output to file (overwrite)
command >> file         # Output to file (append)
command 2> file         # Error output to file
command &> file         # All output to file
command < file          # Input from file
```

### Background Processes

```bash
command &               # Run in background
jobs                    # List background jobs
fg %1                   # Bring job 1 to foreground
bg %1                   # Continue job 1 in background
nohup command &         # Run immune to hangups
```

---

## Summary

- Linux is a free, open-source, UNIX-like OS kernel
- Distributions combine the kernel with software packages
- File system follows a hierarchical structure starting from `/`
- Permissions use rwx for user, group, and others
- Package managers handle software installation

---

[← Previous: Introduction to OS](01-introduction-to-os.md) | [Next: Shell Programming →](03-shell-programming.md)
