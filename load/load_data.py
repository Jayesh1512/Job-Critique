import os

def load_and_stage_data(conn):
    filename = input("Enter the full path to your CSV file (e.g., ./data/jobs.csv): ").strip()
    
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist.")

    with conn.cursor() as cur:
        print("\n📦 Creating file format and stage...")
        cur.execute("""
        CREATE OR REPLACE FILE FORMAT jobs_csv_format
        TYPE = 'CSV'
        FIELD_OPTIONALLY_ENCLOSED_BY = '"'
        SKIP_HEADER = 1
        FIELD_DELIMITER = ','
        NULL_IF = ('NULL', 'null', '')
        EMPTY_FIELD_AS_NULL = TRUE
        """)

        cur.execute("""
        CREATE OR REPLACE STAGE jobs_stage
        FILE_FORMAT = jobs_csv_format
        DIRECTORY = (ENABLE = TRUE)
        """)

        print(f"\n🚀 Uploading file to Snowflake stage: {filename}")
        cur.execute(f"PUT 'file://{os.path.abspath(filename)}' @jobs_stage AUTO_COMPRESS=TRUE OVERWRITE=TRUE")

        print("✅ File uploaded to stage.")

        cur.execute("""
        CREATE OR REPLACE TABLE raw_jobs (
            job_id STRING,
            title STRING,
            company STRING,
            city STRING,
            state STRING,
            country STRING,
            salary_range STRING,
            job_type STRING,
            industry STRING,
            experience_level STRING,
            education_level STRING,
            skills_required STRING,
            posting_date DATE,
            application_deadline DATE,
            remote_flag BOOLEAN,
            job_description STRING,
            load_timestamp TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
        )
        CLUSTER BY (company, posting_date)
        """)

        cur.execute("CREATE OR REPLACE TEMPORARY TABLE temp_jobs LIKE raw_jobs")

        print("\n📥 Copying data into temp_jobs...")
        gz_file = os.path.basename(filename) + ".gz"
        copy_command = f"""
        COPY INTO temp_jobs (
            job_id, title, company, city, state, country,
            salary_range, job_type, industry,
            experience_level, education_level, skills_required,
            posting_date, application_deadline, remote_flag, job_description
        )
        FROM @jobs_stage/{gz_file}
        FILE_FORMAT = (FORMAT_NAME = 'jobs_csv_format')
        ON_ERROR = 'CONTINUE'
        """
        cur.execute(copy_command)

        cur.execute("INSERT INTO raw_jobs SELECT * FROM temp_jobs")

        cur.execute("SELECT COUNT(*) FROM raw_jobs")
        count = cur.fetchone()[0]
        print(f"\n✅ Loaded {count} rows into raw_jobs table.")
