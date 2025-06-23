def create_industry_analysis(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE OR REPLACE TABLE industry_analysis AS
        SELECT industry,
               COUNT(*) AS job_count,
               COUNT(DISTINCT company) AS company_count,
               COUNT(DISTINCT job_type) AS job_type_count,
               COUNT(DISTINCT experience_level) AS experience_level_count
        FROM raw_jobs
        GROUP BY industry
        ORDER BY job_count DESC
        """)
