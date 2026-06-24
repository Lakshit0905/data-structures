-- ============================================================
-- SQL Window Functions for SDET Interviews
-- ============================================================
-- Topics: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD,
--         PARTITION BY, running totals
-- ============================================================

-- Using employees table from basic_queries.sql

-- ── ROW_NUMBER ────────────────────────────────────────────────

-- 1. Assign a unique row number to each employee within their department
--    (sorted by salary descending)
SELECT
    first_name,
    last_name,
    department,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS row_num
FROM employees;

-- ── RANK vs DENSE_RANK ────────────────────────────────────────

-- 2. Rank employees by salary within each department
--    RANK: skips ranks for ties (1,1,3)
--    DENSE_RANK: no gaps (1,1,2)
SELECT
    first_name,
    department,
    salary,
    RANK()       OVER (PARTITION BY department ORDER BY salary DESC) AS rank_num,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank_num
FROM employees;

-- ── TOP N PER GROUP ──────────────────────────────────────────

-- 3. Top 2 highest-paid employees per department (common interview question!)
SELECT * FROM (
    SELECT
        first_name,
        last_name,
        department,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rn
    FROM employees
) ranked
WHERE rn <= 2
ORDER BY department, rn;

-- ── RUNNING TOTAL ────────────────────────────────────────────

-- 4. Running total of salaries ordered by hire date
SELECT
    first_name,
    hire_date,
    salary,
    SUM(salary) OVER (
        ORDER BY hire_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM employees
ORDER BY hire_date;

-- ── LAG and LEAD ─────────────────────────────────────────────

-- 5. Compare each employee's salary to the previous employee (by salary)
SELECT
    first_name,
    salary,
    LAG(salary, 1)  OVER (ORDER BY salary) AS prev_salary,
    LEAD(salary, 1) OVER (ORDER BY salary) AS next_salary,
    salary - LAG(salary, 1) OVER (ORDER BY salary) AS diff_from_prev
FROM employees
ORDER BY salary;

-- ── PERCENT_RANK ─────────────────────────────────────────────

-- 6. Salary percentile ranking within company
SELECT
    first_name,
    salary,
    ROUND(PERCENT_RANK() OVER (ORDER BY salary) * 100, 1) AS salary_percentile
FROM employees
ORDER BY salary;

-- ── SDET Use Case: Find Duplicate Records with ROW_NUMBER ─────

-- 7. Identify duplicate rows (same name + department) — keep only the first
--    (Common in ETL/data migration testing)
WITH ranked_dupes AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY first_name, department
            ORDER BY emp_id
        ) AS rn
    FROM employees
)
SELECT * FROM ranked_dupes WHERE rn > 1;  -- These are the duplicates to remove

-- 8. Running count of hires per department over time
SELECT
    department,
    hire_date,
    first_name,
    COUNT(*) OVER (
        PARTITION BY department
        ORDER BY hire_date
    ) AS running_hire_count
FROM employees
ORDER BY department, hire_date;
