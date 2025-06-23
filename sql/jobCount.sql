--- Top 10 Companies by Job Count
SELECT company, job_count
    FROM company_job_counts
    ORDER BY job_count DESC
    LIMIT 10