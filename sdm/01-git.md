---
layout: default
title: Git Version Control
---

# Git Version Control

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Version Control](#introduction-to-version-control)
- [Git Basics](#git-basics)
- [Git Configuration](#git-configuration)
- [Basic Git Workflow](#basic-git-workflow)
- [Branching and Merging](#branching-and-merging)
- [Remote Repositories](#remote-repositories)
- [Advanced Git Operations](#advanced-git-operations)
- [Git Best Practices](#git-best-practices)

---

## Introduction to Version Control

### What is Version Control?

> **Version Control** is a system that records changes to files over time so you can recall specific versions later.

### Types of Version Control Systems

| Type | Description | Examples |
|------|-------------|----------|
| **Local VCS** | Database on local computer | RCS |
| **Centralized VCS** | Single central server | SVN, CVS |
| **Distributed VCS** | Full mirror on each client | Git, Mercurial |

### Why Git?

- **Distributed**: Every clone is a full backup
- **Fast**: Most operations are local
- **Branching**: Lightweight branching and merging
- **Data Integrity**: SHA-1 hashing for all content

---

## Git Basics

### Git Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Working Directory                    │
│                  (Your project files)                   │
└────────────────────────┬────────────────────────────────┘
                         │ git add
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    Staging Area                         │
│                 (Index / Cache)                         │
└────────────────────────┬────────────────────────────────┘
                         │ git commit
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   Local Repository                      │
│                    (.git folder)                        │
└────────────────────────┬────────────────────────────────┘
                         │ git push
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  Remote Repository                      │
│               (GitHub, GitLab, etc.)                    │
└─────────────────────────────────────────────────────────┘
```

### Git Object Types

| Object | Description |
|--------|-------------|
| **Blob** | File contents |
| **Tree** | Directory structure |
| **Commit** | Snapshot of project |
| **Tag** | Reference to a commit |

---

## Git Configuration

### Configuration Levels

```bash
# System level (all users)
git config --system

# User level (current user)
git config --global

# Repository level (current repo)
git config --local
```

### Essential Configuration

```bash
# Set identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Set default editor
git config --global core.editor "code --wait"

# Set default branch name
git config --global init.defaultBranch main

# View all settings
git config --list

# View specific setting
git config user.name
```

---

## Basic Git Workflow

### Initializing a Repository

```bash
# Create new repository
mkdir project && cd project
git init

# Clone existing repository
git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git
```

### Basic Commands

```bash
# Check status
git status

# Add files to staging
git add filename           # Add specific file
git add .                  # Add all files
git add *.js               # Add by pattern
git add -p                 # Interactive staging

# Commit changes
git commit -m "commit message"
git commit -am "message"   # Add tracked files and commit
git commit --amend         # Modify last commit

# View history
git log                    # Full log
git log --oneline          # Compact log
git log --graph            # Visual branch graph
git log -n 5               # Last 5 commits

# View changes
git diff                   # Working vs staging
git diff --staged          # Staging vs last commit
git diff HEAD              # Working vs last commit
git diff branch1 branch2   # Compare branches
```

### Undoing Changes

```bash
# Unstage files
git reset HEAD filename
git restore --staged filename

# Discard working directory changes
git checkout -- filename
git restore filename

# Revert a commit (creates new commit)
git revert commit_hash

# Reset to previous commit
git reset --soft HEAD~1    # Keep changes staged
git reset --mixed HEAD~1   # Keep changes unstaged
git reset --hard HEAD~1    # Discard changes
```

---

## Branching and Merging

### Branch Basics

```bash
# List branches
git branch                  # Local branches
git branch -r               # Remote branches
git branch -a               # All branches

# Create branch
git branch feature-name

# Switch branch
git checkout branch-name
git switch branch-name      # Git 2.23+

# Create and switch
git checkout -b feature-name
git switch -c feature-name

# Delete branch
git branch -d branch-name   # Safe delete
git branch -D branch-name   # Force delete

# Rename branch
git branch -m old-name new-name
```

### Branching Model

```
main:     ●───●───●───────●───●───●
               \         /
feature:        ●───●───●
```

### Merging

```bash
# Merge branch into current branch
git checkout main
git merge feature-branch

# Types of merges:
# 1. Fast-forward (no new commit)
# 2. Three-way merge (creates merge commit)
```

### Fast-Forward Merge

```
Before:
main:    ●───●───●
              \
feature:       ●───●───●

After:
main:    ●───●───●───●───●───●
                     (feature merged)
```

### Three-Way Merge

```
Before:
main:    ●───●───●───●
              \
feature:       ●───●

After:
main:    ●───●───●───●───●  (merge commit)
              \         /
feature:       ●───●───┘
```

### Handling Merge Conflicts

```bash
# During merge conflict
git status                  # See conflicted files

# In conflicted file:
<<<<<<< HEAD
current branch content
=======
incoming branch content
>>>>>>> feature-branch

# Resolve manually, then:
git add resolved-file
git commit -m "Merge feature-branch"
```

### Rebasing

```bash
# Rebase current branch onto main
git checkout feature
git rebase main

# Interactive rebase
git rebase -i HEAD~3

# Continue after resolving conflicts
git rebase --continue

# Abort rebase
git rebase --abort
```

**Before Rebase:**
```
main:    ●───●───●───●
              \
feature:       ●───●
```

**After Rebase:**
```
main:    ●───●───●───●
                      \
feature:               ●───●
```

---

## Remote Repositories

### Remote Commands

```bash
# Add remote
git remote add origin https://github.com/user/repo.git

# List remotes
git remote -v

# Rename remote
git remote rename origin upstream

# Remove remote
git remote remove upstream

# Show remote info
git remote show origin
```

### Push and Pull

```bash
# Push to remote
git push origin main
git push -u origin main     # Set upstream
git push                    # After -u, just push

# Pull from remote
git pull origin main
git pull                    # Pull from upstream

# Fetch without merge
git fetch origin
git fetch --all

# Push new branch
git push -u origin feature-branch

# Delete remote branch
git push origin --delete branch-name
```

### Pull Request Workflow

```
1. Fork repository on GitHub
2. Clone your fork locally
3. Add upstream remote
4. Create feature branch
5. Make changes and commit
6. Push to your fork
7. Create Pull Request on GitHub
8. Code review and discussion
9. Merge by maintainer
```

---

## Advanced Git Operations

### Stashing

```bash
# Save work in progress
git stash
git stash push -m "message"

# List stashes
git stash list

# Apply stash
git stash apply             # Keep in stash list
git stash pop               # Remove from list

# Apply specific stash
git stash apply stash@{2}

# Drop stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

### Cherry-Pick

```bash
# Apply specific commit to current branch
git cherry-pick commit_hash

# Cherry-pick without committing
git cherry-pick -n commit_hash
```

### Tags

```bash
# List tags
git tag

# Create lightweight tag
git tag v1.0

# Create annotated tag
git tag -a v1.0 -m "Version 1.0"

# Push tags
git push origin v1.0
git push origin --tags

# Delete tag
git tag -d v1.0
git push origin --delete v1.0
```

### Git Bisect

```bash
# Find bug-introducing commit
git bisect start
git bisect bad              # Current commit is bad
git bisect good commit_hash # Known good commit

# Git will checkout middle commit
# Test and mark:
git bisect good  # or
git bisect bad

# When done:
git bisect reset
```

### Submodules

```bash
# Add submodule
git submodule add https://github.com/user/lib.git

# Clone with submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Update submodules
git submodule update --init --recursive
```

---

## Git Best Practices

### Commit Messages

```
Format:
<type>(<scope>): <subject>

<body>

<footer>

Example:
feat(auth): add password reset functionality

- Add forgot password form
- Send reset email with token
- Implement token verification

Closes #123
```

### Commit Message Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation |
| `style` | Formatting (no code change) |
| `refactor` | Code restructuring |
| `test` | Adding tests |
| `chore` | Maintenance |

### Branching Strategy (Git Flow)

```
┌─────────────────────────────────────────────────────────┐
│ main       ●─────────────●─────────────●               │
│             \           /             /                 │
│ release      \    ●────●             /                 │
│               \  /                  /                   │
│ develop  ●─────●────●────●────●────●                   │
│           \              /     \                        │
│ feature    ●────●───────●       ●────●                 │
│                                       \                 │
│ hotfix                                 ●───●            │
└─────────────────────────────────────────────────────────┘
```

### GitHub Flow (Simpler)

```
main:    ●───●───●───●───●───●
              \         /
feature:       ●───●───●
               (PR + Review)
```

### .gitignore

```gitignore
# Compiled files
*.class
*.pyc
*.o

# Dependencies
node_modules/
vendor/

# IDE
.idea/
.vscode/
*.swp

# Environment
.env
.env.local

# Build
dist/
build/
out/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
```

---

## Git Commands Cheat Sheet

```
┌────────────────────────────────────────────────────────────────────────────┐
│                           GIT COMMANDS QUICK REFERENCE                     │
├────────────────────────────────────────────────────────────────────────────┤
│ SETUP                                                                      │
│   git init                Create repository                                │
│   git clone <url>         Clone repository                                 │
│   git config              Configure settings                               │
├────────────────────────────────────────────────────────────────────────────┤
│ BASIC WORKFLOW                                                             │
│   git status              Check status                                     │
│   git add <file>          Stage changes                                    │
│   git commit -m "msg"     Commit changes                                   │
│   git log                 View history                                     │
├────────────────────────────────────────────────────────────────────────────┤
│ BRANCHING                                                                  │
│   git branch              List branches                                    │
│   git branch <name>       Create branch                                    │
│   git checkout <branch>   Switch branch                                    │
│   git merge <branch>      Merge branch                                     │
│   git rebase <branch>     Rebase onto branch                              │
├────────────────────────────────────────────────────────────────────────────┤
│ REMOTE                                                                     │
│   git remote -v           List remotes                                     │
│   git push                Push changes                                     │
│   git pull                Pull changes                                     │
│   git fetch               Fetch without merge                              │
├────────────────────────────────────────────────────────────────────────────┤
│ UNDO                                                                       │
│   git reset               Reset staging                                    │
│   git revert              Undo commit (safe)                              │
│   git checkout --         Discard changes                                  │
│   git stash               Save work temporarily                           │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Summary

- Git is a distributed version control system
- Three areas: Working Directory, Staging, Repository
- Branching enables parallel development
- Remote repositories allow collaboration
- Follow best practices for commits and branching

---

[Next: Software Engineering →](02-software-engineering.md)
