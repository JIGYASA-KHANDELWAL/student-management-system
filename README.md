# 🎓 Student Management System (Python)

*A lightweight, menu‑driven CLI application for managing student records*

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#-license)

---

## ✨ Overview

This **Student Management System** is a small yet functional console application written in pure Python. It helps you keep track of student data — add, view, search, update, and delete records — without any external dependencies or databases. Ideal for beginners to learn file handling, functions, and simple CRUD logic.

---

## 📑 Table of Contents

1. [Features](#-features)
2. [Demo](#-demo)
3. [Requirements](#-requirements)
4. [Installation](#-installation)
5. [Usage](#-usage)
6. [Project Structure](#-project-structure)
7. [License](#-license)

---

## 🚀 Features

* **Add** new student records (name, roll number/ID, class, etc.)
* **View** all stored students in a neat table
* **Search** by ID or name keyword
* **Update** a record’s fields selectively
* **Delete** obsolete records
* **Persistent storage** via a simple text (or CSV) file — runs on any machine without a database
* Clear **menu‑driven interface** for quick navigation

---

## 🎥 Demo

```text
===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Choose an option: _
```


---

## 🔧 Requirements

* **Python 3.8** or higher
  No third‑party libraries required.

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your‑username>/student-management-system.git
cd student-management-system

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Run the script
python student_management.py
```

---

## 🕹️ Usage

| Menu Option | Action                                                 |
| ----------- | ------------------------------------------------------ |
| **1**       | Add a new student (you’ll be prompted for each field). |
| **2**       | Display every student in a tabular view.               |
| **3**       | Search by roll number or partial name.                 |
| **4**       | Edit a chosen record’s fields.                         |
| **5**       | Remove a student permanently.                          |
| **6**       | Exit the application.                                  |

> **Tip:** All data is stored in `students.txt` (plain CSV). You can change the filename or format inside `student_management.py`.

---

## 🗂️ Project Structure

```
student-management-system/
├── student_management.py   # Main CLI application
├── students.txt            # Auto‑generated data file (after first run)
├── README.md               # You’re reading it!
```

---


---

## 📝 License

Distributed under the **MIT License**. See the [`LICENSE`](LICENSE) file for more information. Feel free to use, modify, and share!

---

### ✉️ Contact

Maintainer: **Jigyasa Khandelwal**
If you have questions, open an issue or connect on [LinkedIn](www.linkedin.com/in/jigyasa-khandelwal-989153298) 

---

> *Happy coding & keep learning!*
