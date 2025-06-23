create or replace view JOBS_DW.JOBS_SCHEMA.VW_TOP_SKILLS_BY_INDUSTRY(
	INDUSTRY,
	SKILL,
	SKILL_COUNT
) as
            WITH skill_counts AS (
                SELECT
                    i.industry,
                    s.skill,
                    COUNT(*) AS skill_count,
                    ROW_NUMBER() OVER (PARTITION BY i.industry ORDER BY COUNT(*) DESC) AS skill_rank
                FROM fact_job_postings f
                JOIN bridge_job_skills bs ON f.job_id = bs.job_id
                JOIN dim_skill s ON bs.skill_key = s.skill_key
                JOIN dim_industry i ON f.industry_key = i.industry_key
                GROUP BY i.industry, s.skill
            )
            SELECT
                industry,
                skill,
                skill_count
            FROM skill_counts
            WHERE skill_rank <= 10
            ORDER BY industry, skill_rank;