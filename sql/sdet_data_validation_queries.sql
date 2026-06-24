-- ============================================================
-- SDET Data Validation SQL Queries
-- ============================================================
-- Real-world QA/SDET interview SQL problems:
--   - Source vs target table comparison
--   - NULL/missing data checks
--   - Duplicate record detection
--   - Count reconciliation
--   - Data type and format validation
-- ============================================================

-- ── SCHEMA: Source and Target tables ─────────────────────────
-- Simulates a data migration or ETL validation scenario

CREATE TABLE source_customers (
    customer_id  INT,
    first_name   VARCHAR(50),
    last_name    VARCHAR(50),
    email        VARCHAR(100),
    phone        VARCHAR(20),
    status       VARCHAR(20),
    created_date DATE
);

CREATE TABLE target_customers (
    customer_id  INT,
    first_name   VARCHAR(50),
    last_name    VARCHAR(50),
    email        VARCHAR(100),
    phone        VARCHAR(20),
    status       VARCHAR(20),
    created_date DATE
);

INSERT INTO source_customers VALUES
(1, 'Alice',  'Smith',  'alice@test.com',  '555-1001', 'ACTIVE',    '2023-01-01'),
(2, 'Bob',    'Jones',  'bob@test.com',    '555-1002', 'INACTIVE',  '2023-02-15'),
(3, 'Carol',  'White',  NULL,              '555-1003', 'ACTIVE',    '2023-03-10'),
(4, 'David',  'Brown',  'david@test.com',  NULL,       'ACTIVE',    '2023-04-20'),
(5, 'Eve',    'Davis',  'eve@test.com',    '555-1005', 'PENDING',   '2023-05-05'),
(6, 'Frank',  'Miller', 'frank@test.com',  '555-1006', 'ACTIVE',    '2023-06-01');

INSERT INTO target_customers VALUES
(1, 'Alice',  'Smith',  'alice@test.com',  '555-1001', 'ACTIVE',    '2023-01-01'),
(2, 'Bob',    'Jones',  'bob@test.com',    '555-1002', 'ACTIVE',    '2023-02-15'),  -- status changed!
(3, 'Carol',  'White',  NULL,              '555-1003', 'ACTIVE',    '2023-03-10'),
(4, 'David',  'Brown',  'david@test.com',  NULL,       'ACTIVE',    '2023-04-20'),
(5, 'Eve',    'Davis',  'eve@test.com',    '555-1005', 'PENDING',   '2023-05-05');
-- Frank is MISSING from target!

-- ============================================================
-- VALIDATION QUERY 1: Row Count Comparison
-- ============================================================
SELECT
    'source_customers' AS table_name,
    COUNT(*)           AS row_count
FROM source_customers

UNION ALL

SELECT
    'target_customers',
    COUNT(*)
FROM target_customers;
-- Expected: same count. If different → migration issue!

-- ============================================================
-- VALIDATION QUERY 2: Records in SOURCE but NOT in TARGET
-- ============================================================
SELECT s.*
FROM source_customers s
LEFT JOIN target_customers t ON s.customer_id = t.customer_id
WHERE t.customer_id IS NULL;
-- Returns Frank → missing from target

-- ============================================================
-- VALIDATION QUERY 3: Records in TARGET but NOT in SOURCE
-- ============================================================
SELECT t.*
FROM target_customers t
LEFT JOIN source_customers s ON t.customer_id = s.customer_id
WHERE s.customer_id IS NULL;

-- ============================================================
-- VALIDATION QUERY 4: Data Mismatch Between Source and Target
-- ============================================================
SELECT
    s.customer_id,
    'status' AS mismatched_column,
    s.status AS source_value,
    t.status AS target_value
FROM source_customers s
INNER JOIN target_customers t ON s.customer_id = t.customer_id
WHERE s.status != t.status

UNION ALL

SELECT
    s.customer_id,
    'email',
    s.email,
    t.email
FROM source_customers s
INNER JOIN target_customers t ON s.customer_id = t.customer_id
WHERE (s.email IS DISTINCT FROM t.email);

-- ============================================================
-- VALIDATION QUERY 5: NULL Value Check
-- ============================================================
SELECT
    'source' AS source,
    SUM(CASE WHEN email   IS NULL THEN 1 ELSE 0 END) AS null_emails,
    SUM(CASE WHEN phone   IS NULL THEN 1 ELSE 0 END) AS null_phones,
    SUM(CASE WHEN status  IS NULL THEN 1 ELSE 0 END) AS null_status
FROM source_customers

UNION ALL

SELECT
    'target',
    SUM(CASE WHEN email   IS NULL THEN 1 ELSE 0 END),
    SUM(CASE WHEN phone   IS NULL THEN 1 ELSE 0 END),
    SUM(CASE WHEN status  IS NULL THEN 1 ELSE 0 END)
FROM target_customers;

-- ============================================================
-- VALIDATION QUERY 6: Duplicate Record Detection
-- ============================================================
SELECT
    customer_id,
    COUNT(*) AS occurrences
FROM source_customers
GROUP BY customer_id
HAVING COUNT(*) > 1;  -- customer_id should be unique

-- Duplicate emails check
SELECT
    email,
    COUNT(*) AS count
FROM source_customers
WHERE email IS NOT NULL
GROUP BY email
HAVING COUNT(*) > 1;

-- ============================================================
-- VALIDATION QUERY 7: Status Value Validation (allowed values)
-- ============================================================
SELECT customer_id, status
FROM source_customers
WHERE status NOT IN ('ACTIVE', 'INACTIVE', 'PENDING', 'SUSPENDED');

-- ============================================================
-- VALIDATION QUERY 8: Full Reconciliation Summary Report
-- ============================================================
WITH source_count AS (SELECT COUNT(*) AS cnt FROM source_customers),
     target_count AS (SELECT COUNT(*) AS cnt FROM target_customers),
     missing_in_target AS (
         SELECT COUNT(*) AS cnt
         FROM source_customers s
         LEFT JOIN target_customers t ON s.customer_id = t.customer_id
         WHERE t.customer_id IS NULL
     ),
     mismatched AS (
         SELECT COUNT(*) AS cnt
         FROM source_customers s
         INNER JOIN target_customers t ON s.customer_id = t.customer_id
         WHERE s.status != t.status
     )
SELECT
    sc.cnt  AS source_rows,
    tc.cnt  AS target_rows,
    (sc.cnt - tc.cnt) AS row_difference,
    mit.cnt AS missing_in_target,
    mm.cnt  AS status_mismatches
FROM source_count sc, target_count tc, missing_in_target mit, mismatched mm;
