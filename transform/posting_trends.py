def create_posting_trends(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE OR REPLACE TABLE job_posting_trends AS
        SELECT DATE_TRUNC('MONTH', posting_date) AS posting_month,
               COUNT(*) AS job_count,
               COUNT(DISTINCT company) AS company_count,
               COUNT(DISTINCT industry) AS industry_count
        FROM raw_jobs
        GROUP BY posting_month
        ORDER BY posting_month
        """)
