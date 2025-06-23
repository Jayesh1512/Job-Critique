def create_company_analysis(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE OR REPLACE TABLE company_job_counts AS
        SELECT company,
               COUNT(*) AS job_count,
               COUNT(DISTINCT job_type) AS job_type_count,
               COUNT(DISTINCT industry) AS industry_count
        FROM raw_jobs
        GROUP BY company
        ORDER BY job_count DESC
        """)
