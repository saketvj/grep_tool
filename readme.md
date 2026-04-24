# 📄 Mini Grep Tool (Python)

A lightweight implementation of the Unix `grep` command built using Python.  
This tool allows searching for patterns in files (or standard input) with support for basic flags and regular expressions.

---

## 🚀 Features

- 🔍 Pattern searching using **regular expressions (`re`)**
- 📁 Recursive file search (`-r`)
- 🔤 Case-insensitive matching (`-i`)
- 🔄 Inverted matching (`-v`)
- 📥 Reads from **stdin** if no file is provided
- 🧾 Displays output in `filename: line` format

---

## 📦 Requirements

- Python 3.x  
- No external dependencies (uses built-in modules only)

---

## 🛠️ Usage

```bash
python3 grep.py <flags (optional)> <pattern> <file>


🧑‍💻 5 Key Learnings from This Project
CLI Argument Parsing
Learned how sys.argv works and how to extract flags and inputs.
File & Directory Handling
Used pathlib to traverse files and directories recursively.
Recursive Programming
Implemented directory traversal using recursion.
Regular Expressions (re)
Learned how to search patterns using re.search() and flags like IGNORECASE.
Designing a Real CLI Tool
Understood how to structure a program:
Input → Processing → Output
Separation of concerns (parsing, matching, printing)