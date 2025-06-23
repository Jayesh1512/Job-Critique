def create_snowflake_objects(conn):
    with conn.cursor() as cur:
        cur.execute("CREATE WAREHOUSE IF NOT EXISTS PROJECT_WH WITH WAREHOUSE_SIZE='X-SMALL' AUTO_SUSPEND=300 AUTO_RESUME=TRUE")
        cur.execute("CREATE DATABASE IF NOT EXISTS JOBS_DB")
        cur.execute("CREATE SCHEMA IF NOT EXISTS JOBS_DB.JOBS_SCHEMA")
        cur.execute("USE WAREHOUSE PROJECT_WH")
        cur.execute("USE DATABASE JOBS_DB")
        cur.execute("USE SCHEMA JOBS_SCHEMA")
