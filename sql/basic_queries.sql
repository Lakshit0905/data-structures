-- ============================================================
-- SQL Basic Queries for SDET Interviews
-- ============================================================
-- Topic: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, LIKE, NULL checks
-- ============================================================

-- ── SCHEMA SETUP ─────────────────────────────────────────────

CREATE TABLE employees (
    emp_id      INT PRIMARY KEY,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    department  VARCHAR(50),
    salary      DECIMAL(10, 2),
    hire_date   DATE,
    manager_id  INT,
    email       VARCHAR(100)
);

INSERT INTO employees VALUES
(1,  'Alice',   'Smith',   'Engineering', 95000, '2020-01-15', NULL,  'alice@company.com'),
(2,  'Bob',     'Jones',   'QA',          75000, '2019-03-22', 1,     'bob@company.com'),
(3,  'Carol',   'White',   'Engineering', 85000, '2021-07-01', 1,     'carol@company.com'),
(4,  'David',   'Brown',   'QA',          72000, '2022-02-10', 2,     'david@company.com'),
(5,  'Eve',     'Davis',   'HR',          60000, '2018-11-30', NULL,  NULL),
(6,  'Frank',   'Miller',  'Engineering', 92000, '2020-06-15', 1,     'frank@company.com'),
(7,  'Grace',   'Wilson',  'QA',          78000, '2021-09-01', 2,     'grace@company.com'),
(8,  'Henry',   'Moore',   'HR',          55000, '2023-01-05', 5,     'henry@company.com'),
(9,  'Iris',    'Taylor',  'Engineering', 110000,'2017-04-20', 1,     'iris@company.com'),
(10, 'Jack',    'Anderson','QA',          68000, '2022-08-14', 2,     NULL);

-- ── BASIC SELECT ─────────────────────────────────────────────

-- 1. Select all employees
SELECT * FROM employees;

-- 2. Select specific columns
SELECT emp_id, first_name, last_name, salary
FROM employees;

-- 3. Select with alias
SELECT
    emp_id AS "Employee ID",
    first_name || ' ' || last_name AS "Full Name",
    salary AS "Annual Salary"
FROM employees;

-- ── WHERE CLAUSE ─────────────────────────────────────────────

-- 4. Employees in QA department
SELECT * FROM employees WHERE department = 'QA';

-- 5. Employees with salary above 80000
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 80000
ORDER BY salary DESC;

-- 6. Employees hired in 2020 or later
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= '2020-01-01'
ORDER BY hire_date;

-- 7. Multiple conditions (AND / OR)
SELECT * FROM employees
WHERE department = 'Engineering' AND salary > 90000;

SELECT * FROM employees
WHERE department = 'QA' OR department = 'HR';

-- ── NULL CHECKS (critical for SDET data validation!) ─────────

-- 8. Find employees with NULL email (missing data validation)
SELECT emp_id, first_name, last_name, email
FROM employees
WHERE email IS NULL;

-- 9. Find employees WITH an email
SELECT emp_id, first_name, last_name, email
FROM employees
WHERE email IS NOT NULL;

-- 10. Find employees with no manager (top-level)
SELECT * FROM employees WHERE manager_id IS NULL;

-- ── DISTINCT ─────────────────────────────────────────────────

-- 11. Get unique departments
SELECT DISTINCT department FROM employees ORDER BY department;

-- ── LIKE (pattern matching) ───────────────────────────────────

-- 12. Employees whose first name starts with 'A'
SELECT * FROM employees WHERE first_name LIKE 'A%';

-- 13. Employees whose email contains '@company'
SELECT * FROM employees WHERE email LIKE '%@company%';

-- ── ORDER BY and LIMIT ────────────────────────────────────────

-- 14. Top 3 highest paid employees
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- 15. Lowest paid employees
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary ASC
LIMIT 3;

-- ── IN / BETWEEN ─────────────────────────────────────────────

-- 16. Employees in specific departments
SELECT * FROM employees
WHERE department IN ('Engineering', 'QA');

-- 17. Employees with salary between 70000 and 90000
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 70000 AND 90000
ORDER BY salary;
