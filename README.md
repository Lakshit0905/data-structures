# 🧪 Data Structures for SDET Interviews

> A complete, beginner-to-intermediate Python interview preparation repository built for Software Development Engineers in Test (SDET) roles in the USA.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Pytest-orange)](https://pytest.org/)

---

## 📌 Why This Repository?

- Data structure & algorithm problems (LeetCode-style, beginner/intermediate)
- SDET-specific coding: JSON validation, log parsing, API response comparison
- SQL queries for data validation
- Test automation utility coding
- API testing logic problems

This repository covers **all of these** in one place with clean Python 3 code, detailed explanations, and ready-to-run pytest tests.

---

## 📂 Topics Covered

| # | Topic | Description |
|---|-------|-------------|
| 1 | [Arrays & Strings](./arrays_strings/) | Reverse, two sum, anagram, duplicates |
| 2 | [HashMap / Dictionary](./hashmap/) | Frequency counter, group anagrams |
| 3 | [Two Pointers](./two_pointers/) | Palindrome, pair sum, move zeroes |
| 4 | [Sliding Window](./sliding_window/) | Max subarray sum, longest substring |
| 5 | [Sorting & Searching](./sorting_searching/) | Binary search, merge arrays, missing number |
| 6 | [Recursion](./recursion/) | Factorial, Fibonacci, sum of array |
| 7 | [Stack & Queue](./stack_queue/) | Valid parentheses, next greater element |
| 8 | [Linked List](./linked_list/) | Reverse, detect cycle, find middle |
| 9 | [SQL](./sql/) | Joins, window functions, data validation |
| 10 | [SDET Specific](./sdet_specific/) | API compare, JSON validate, log parsing |

---

## 🚀 How to Run

### Prerequisites
```bash
python3 --version   # Requires Python 3.8+
pip install -r requirements.txt
```

### Run any Python file
```bash
cd data-structures-for-sdet-interviews
python3 arrays_strings/two_sum.py
python3 sdet_specific/validate_json_schema.py
```

### Run all tests with pytest
```bash
pytest tests/ -v
pytest tests/ -v --tb=short    # shorter traceback
pytest tests/test_arrays_strings.py -v   # specific file
```

---

## 📅 30-Day SDET Interview Preparation Plan

| Week | Days | Focus |
|------|------|-------|
| **Week 1** | Day 1–2 | Arrays & Strings |
| | Day 3–4 | HashMap & Dictionary |
| | Day 5–6 | Two Pointers |
| | Day 7 | Review + Mock Problems |
| **Week 2** | Day 8–9 | Sliding Window |
| | Day 10–11 | Sorting & Searching |
| | Day 12–13 | Recursion Basics |
| | Day 14 | Review + Mock Problems |
| **Week 3** | Day 15–16 | Stack & Queue |
| | Day 17–18 | Linked List Basics |
| | Day 19–20 | Binary Search |
| | Day 21 | Review + Mock Problems |
| **Week 4** | Day 22–23 | SQL for SDET |
| | Day 24–25 | SDET-Specific Coding |
| | Day 26–27 | API Testing Logic |
| | Day 28–29 | Full Mock Interview |
| | Day 30 | Review Weak Areas |

---

## 🗺️ SDET Interview Roadmap

```
SDET Interview Preparation
│
├── 1. Coding Round (LeetCode-style, Easy–Medium)
│   ├── Arrays, Strings, HashMap
│   ├── Two Pointers, Sliding Window
│   ├── Binary Search, Sorting
│   └── Basic Recursion, Stack, Queue
│
├── 2. SDET-Specific Coding
│   ├── JSON / API response validation
│   ├── Log file parsing
│   ├── Test data generation
│   └── Retry logic, test utilities
│
├── 3. SQL Round
│   ├── SELECT, WHERE, GROUP BY, HAVING
│   ├── JOINs (INNER, LEFT, RIGHT)
│   ├── Window Functions (ROW_NUMBER, RANK)
│   └── Data validation queries
│
├── 4. System Design for QA (Senior roles)
│   ├── Test automation framework design
│   └── CI/CD pipeline understanding
│
└── 5. Behavioral Round
    ├── Bug advocacy stories
    └── Cross-team collaboration examples
```

---

## 💼 GitHub Portfolio Explanation

This repository demonstrates:
- **Problem-solving ability** with clean, readable Python 3 code
- **QA mindset** through SDET-specific utility problems
- **SQL proficiency** for data validation tasks common in SDET roles
- **Testing culture** with pytest unit tests for every module
- **Code organization** with well-structured folders and documentation

Recruiters and hiring managers can navigate by topic, run the tests, and see real examples of SDET interview readiness.

---

## 📝 Resume Bullet Point

After completing this repository, add this to your resume:

> **SDET Interview Preparation Project** | Python, SQL, pytest | [GitHub Link]
> Built a comprehensive coding interview preparation repository covering 13 core topics including arrays, hashmaps, sliding window, SQL data validation, and SDET-specific utilities (JSON validation, API comparison, log parsing). Implemented 50+ coding problems with pytest unit tests and documented time/space complexity for each solution.

---

## 👩‍💻 For Recruiters & Interviewers

- Each Python file contains the **problem statement, solution, complexity analysis, and example I/O**
- All solutions are tested with **pytest** — run `pytest tests/ -v` to see results
- SQL files include **data validation patterns** commonly used in SDET interviews
- SDET-specific problems reflect **real-world QA automation utility tasks**

---

## 🛠️ Git Setup Commands

```bash
git init
git add .
git commit -m "Initial commit: Python data structures for SDET interviews"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

---

## 📄 License

MIT License — free to use, fork, and learn from.
