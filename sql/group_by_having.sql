-- ============================================================
-- SQL GROUP BY, HAVING, and Aggregate Functions
-- for SDET Interviews
-- ============================================================

-- Using the employees table from basic_queries.sql

-- ── AGGREGATE FUNCTIONS ───────────────────────────────────────

-- 1. Total number of employees
SELECT COUNT(*) AS total_employees FROM employees;

-- 2. Average salary across all employees
SELECT ROUND(AVG(salary), 2) AS avg_salary FROM employees;

-- 3. Min and max salary
SELECT
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    MAX(salary) - MIN(salary) AS salary_range
FROM employees;

-- ── GROUP BY ─────────────────────────────────────────────────

-- 4. Employee count per department
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;

-- 5. Average salary per department
SELECT
    department,
    COUNT(*)                   AS headcount,
    ROUND(AVG(salary), 2)      AS avg_salary,
    MIN(salary)                AS min_salary,
    MAX(salary)                AS max_salary,
    SUM(salary)                AS total_payroll
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- ── HAVING (filter on grouped results) ────────────────────────

-- 6. Departments with more than 2 employees
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- 7. Departments with avg salary above 75000
SELECT
    department,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 75000
ORDER BY avg_salary DESC;

-- ── SDET Data Validation Use Cases ───────────────────────────

-- 8. Find departments with NULL emails (data quality check)
SELECT
    department,
    COUNT(*)                              AS total,
    SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS missing_emails,
    ROUND(
        100.0 * SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS pct_missing
FROM employees
GROUP BY department;

-- 9. Duplicate email detection
SELECT
    email,
    COUNT(*) AS occurrences
FROM employees
WHERE email IS NOT NULL
GROUP BY email
HAVING COUNT(*) > 1;

-- 10. Salary distribution by department (bucket analysis)
SELECT
    department,
    SUM(CASE WHEN salary < 70000 THEN 1 ELSE 0 END)              AS "< 70k",
    SUM(CASE WHEN salary BETWEEN 70000 AND 89999 THEN 1 ELSE 0 END) AS "70k-90k",
    SUM(CASE WHEN salary >= 90000 THEN 1 ELSE 0 END)             AS ">= 90k"
FROM employees
GROUP BY department
ORDER BY department;

-- 11. Year-over-year hire analysis
SELECT
    EXTRACT(YEAR FROM hire_date) AS hire_year,
    COUNT(*)                     AS new_hires
FROM employees
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY hire_year;
