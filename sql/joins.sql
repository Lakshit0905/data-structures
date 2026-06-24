-- ============================================================
-- SQL JOINs for SDET Interviews
-- ============================================================
-- Topics: INNER JOIN, LEFT JOIN, RIGHT JOIN, SELF JOIN,
--         and data validation using joins
-- ============================================================

-- ── SCHEMA SETUP ─────────────────────────────────────────────

CREATE TABLE departments (
    dept_id    INT PRIMARY KEY,
    dept_name  VARCHAR(50),
    location   VARCHAR(50),
    budget     DECIMAL(12, 2)
);

CREATE TABLE employees (
    emp_id      INT PRIMARY KEY,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    dept_id     INT,
    salary      DECIMAL(10, 2),
    manager_id  INT
);

CREATE TABLE projects (
    project_id   INT PRIMARY KEY,
    project_name VARCHAR(100),
    dept_id      INT,
    status       VARCHAR(20)
);

CREATE TABLE emp_projects (
    emp_id     INT,
    project_id INT,
    role       VARCHAR(50)
);

INSERT INTO departments VALUES
(1, 'Engineering', 'New York',   500000),
(2, 'QA',         'Austin',     200000),
(3, 'HR',         'Chicago',    150000),
(4, 'Finance',    'New York',   300000);

INSERT INTO employees VALUES
(1,  'Alice', 'Smith', 1, 95000, NULL),
(2,  'Bob',   'Jones', 2, 75000, 1),
(3,  'Carol', 'White', 1, 85000, 1),
(4,  'David', 'Brown', 2, 72000, 2),
(5,  'Eve',   'Davis', 3, 60000, NULL),
(6,  'Frank', 'Miller',NULL, 92000, 1);  -- No dept assigned (orphan)

INSERT INTO projects VALUES
(101, 'Payment Gateway',  1, 'Active'),
(102, 'Login Automation', 2, 'Active'),
(103, 'HR Portal',        3, 'Completed'),
(104, 'Data Pipeline',    1, 'Active'),
(105, 'Unknown Project',  99,'Active');  -- Dept 99 doesn't exist (orphan)

INSERT INTO emp_projects VALUES
(1, 101, 'Lead'),
(2, 102, 'Tester'),
(3, 101, 'Developer'),
(4, 102, 'Senior Tester'),
(1, 104, 'Architect');

-- ── INNER JOIN ────────────────────────────────────────────────

-- 1. Employees with their department names (only matched rows)
SELECT
    e.emp_id,
    e.first_name,
    e.last_name,
    d.dept_name,
    e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
ORDER BY e.emp_id;
-- Note: Frank (dept_id=NULL) is NOT included

-- ── LEFT JOIN ─────────────────────────────────────────────────

-- 2. ALL employees, with department (NULL if no dept assigned)
SELECT
    e.emp_id,
    e.first_name,
    e.last_name,
    d.dept_name,   -- Will be NULL for Frank
    e.salary
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
ORDER BY e.emp_id;

-- ── SDET Data Validation: Find employees with NO department ──
-- 3. Orphan employees (not linked to any department)
SELECT e.emp_id, e.first_name, e.last_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;  -- Rows where join found no match

-- ── SDET: Find departments with NO employees ─────────────────
-- 4. Empty departments
SELECT d.dept_id, d.dept_name
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- ── MULTI-TABLE JOIN ─────────────────────────────────────────

-- 5. Employee → project assignments with full details
SELECT
    e.first_name,
    e.last_name,
    p.project_name,
    ep.role,
    d.dept_name
FROM emp_projects ep
INNER JOIN employees e  ON ep.emp_id     = e.emp_id
INNER JOIN projects  p  ON ep.project_id = p.project_id
INNER JOIN departments d ON e.dept_id    = d.dept_id
ORDER BY e.first_name;

-- ── SELF JOIN ─────────────────────────────────────────────────

-- 6. Employees with their manager's name (self-join)
SELECT
    e.first_name  AS employee,
    m.first_name  AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id
ORDER BY e.emp_id;

-- ── SDET: Validate referential integrity ─────────────────────

-- 7. Projects with invalid department (dept_id doesn't exist)
SELECT p.project_id, p.project_name, p.dept_id AS "Invalid Dept ID"
FROM projects p
LEFT JOIN departments d ON p.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- 8. Count records per join type — source vs target validation
-- (Compare row counts to catch data migration issues)
SELECT
    'employees_with_dept'   AS check_name,
    COUNT(*)                AS record_count
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id

UNION ALL

SELECT
    'employees_without_dept',
    COUNT(*)
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
