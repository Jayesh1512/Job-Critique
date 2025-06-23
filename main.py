from utils.snowflake_connection import get_connection
from setup.create_objects import create_snowflake_objects
from load.load_data import load_and_stage_data
from transform.company_analysis import create_company_analysis
from transform.industry_analysis import create_industry_analysis
from transform.posting_trends import create_posting_trends

def main():
    conn = get_connection()
    
    # Step 1: Create Snowflake structures
    create_snowflake_objects(conn)

    # Step 2: Load data into Snowflake
    load_and_stage_data(conn)

    # Step 3: Apply transformations and create derived tables
    create_company_analysis(conn)
    create_industry_analysis(conn)
    create_posting_trends(conn)

    conn.close()
    print("ETL completed successfully!")

if __name__ == "__main__":
    main()
