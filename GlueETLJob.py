import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize the SparkContext and GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Initialize the Glue Job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ---- ETL LOGIC GOES HERE ----
# 1. Read data from Glue Catalog
# 2. Apply transformations
# 3. Write transformed data to S3 and store in Glue Catalog (processed data)

# Read data from Glue Catalog (your raw CSV table)
raw_database_name = 'main_raw_data'  # Replace with your raw data Glue database name
raw_table_name = 'sales/rawData'     # Replace with your raw data Glue table name

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database=raw_database_name, 
    table_name=raw_table_name
)

# Convert to DataFrame for transformation
data_frame = dynamic_frame.toDF()

# Transformations
# Select specific columns
transformed_df = data_frame.select("id", "name", "host_id", "host_name")

# Convert DataFrame back to DynamicFrame
transformed_dynamic_frame = DynamicFrame.fromDF(transformed_df, glueContext, "transformed_dynamic_frame")

# ---- 1. Write Transformed Data to S3 ----
# Define the S3 output path
output_s3_path = "s3://sales-etl-bucket/cleanData/"

# Write the transformed data back to S3 in CSV format
glueContext.write_dynamic_frame.from_options(
    transformed_dynamic_frame,
    connection_type="s3",
    connection_options={"path": output_s3_path},  # Ensure a single path is provided
    format="parquet"  # Change to 'parquet' if you want to use Parquet
)

# ---- End of ETL Logic ----

# Commit the Glue job (required)
job.commit()
