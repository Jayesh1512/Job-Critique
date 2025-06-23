create or replace view JOBS_DW.JOBS_SCHEMA.VW_JOB_POSTING_TRENDS(
	YEAR,
	QUARTER,
	MONTH,
	MONTH_NAME,
	JOB_COUNT,
	COMPANY_COUNT,
	INDUSTRY_COUNT,
	AVG_SALARY
) as
            SELECT
                d.year,
                d.quarter,
                d.month,
                d.month_name,
                COUNT(*) AS job_count,
                COUNT(DISTINCT f.company_key) AS company_count,
                COUNT(DISTINCT f.industry_key) AS industry_count,
                AVG(f.avg_salary) AS avg_salary
            FROM fact_job_postings f
            JOIN dim_date d ON f.posting_date_key = d.date_key
            GROUP BY d.year, d.quarter, d.month, d.month_name
            ORDER BY d.year, d.month;