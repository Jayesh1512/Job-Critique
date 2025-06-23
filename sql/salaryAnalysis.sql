create or replace view JOBS_DW.JOBS_SCHEMA.VW_REMOTE_WORK_ANALYSIS(
	INDUSTRY,
	JOB_TYPE,
	REMOTE_FLAG,
	JOB_COUNT,
	AVG_SALARY,
	PERCENTAGE
) as
            SELECT
                i.industry,
                jt.job_type,
                f.remote_flag,
                COUNT(*) AS job_count,
                AVG(f.avg_salary) AS avg_salary,
                COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY i.industry) AS percentage
            FROM fact_job_postings f
            JOIN dim_industry i ON f.industry_key = i.industry_key
            JOIN dim_job_type jt ON f.job_type_key = jt.job_type_key
            GROUP BY i.industry, jt.job_type, f.remote_flag
            ORDER BY i.industry, jt.job_type, f.remote_flag;