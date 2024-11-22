# AWS ETL Workflow with Glue, S3, Step Functions, SNS, and Athena

This project demonstrates an end-to-end ETL (Extract, Transform, Load) process using AWS Glue, S3, Step Functions, SNS, and Athena. It automates the workflow to extract raw data from an S3 bucket, transform it using Glue PySpark, load the transformed data back into S3, catalog it with a Glue Crawler, and make it queryable with Athena. Notifications are sent via SNS upon completion of the workflow.

---

## Features

- **ETL Workflow with AWS Glue**: Perform data extraction, transformation, and loading with PySpark scripts.
- **Separate Databases**: Maintain separate Glue databases for raw and transformed data for better organization.
- **Automated Cataloging**: Use Glue Crawlers to update the Glue Data Catalog dynamically.
- **Query with Athena**: Query the transformed data easily using SQL-like syntax in AWS Athena.
- **Step Functions Orchestration**: Orchestrate the entire workflow seamlessly using AWS Step Functions.
- **Notifications via SNS**: Get email notifications upon the successful completion of the ETL process.

---

## Architecture

1. **Data Extraction**: Fetch raw data from an S3 bucket.
2. **Data Transformation**: Process and transform the data using a Glue PySpark script.
3. **Data Loading**: Load the transformed data back into another S3 bucket.
4. **Cataloging**: Use Glue Crawlers to catalog the raw and transformed data into separate Glue databases.
5. **Querying**: Query the transformed data via Athena for analytics.
6. **Notifications**: Send an SNS email notification when the process completes.

---

## Technologies Used

- **AWS Glue**: For ETL processes and cataloging.
- **AWS S3**: For data storage.
- **AWS Step Functions**: For orchestration of the ETL workflow.
- **AWS SNS**: For sending email notifications.
- **AWS Athena**: For querying the cataloged data.
- **PySpark**: For data transformation.

---

## Prerequisites

1. An AWS account with access to Glue, S3, Step Functions, SNS, and Athena.
2. Python knowledge for understanding the Glue PySpark scripts.
3. S3 buckets:
   - One for raw data.
   - One for transformed data.
4. Glue databases:
   - One for raw data.
   - One for transformed data.
5. SNS topic created and subscribed with a valid email for notifications.

---

## Setup and Installation

### Step 1: Set up S3 Buckets
- Create two S3 buckets:
  - `raw-data-bucket`: To store raw data.
  - `transformed-data-bucket`: To store transformed data.

### Step 2: Configure Glue
- Create two Glue databases:
  - `raw_data_db`: For cataloging raw data.
  - `transformed_data_db`: For cataloging transformed data.
- Create a Glue job with a PySpark script for data transformation.
- Add the necessary IAM roles and policies.

### Step 3: Create Glue Crawlers
- Set up two Glue Crawlers:
  - **Crawler 1**: To catalog raw data into `raw_data_db`.
  - **Crawler 2**: To catalog transformed data into `transformed_data_db`.

### Step 4: Define Step Functions Workflow
- Design the Step Functions workflow to automate the process:
  - Step 1: Trigger Glue ETL job.
  - Step 2: Start the Glue Crawlers.
  - Step 3: Notify completion with SNS.

### Step 5: Configure SNS
- Create an SNS topic and subscribe with your email address to receive notifications.

### Step 6: Query with Athena
- Configure Athena to query the data using the Glue Data Catalog.
- Set the default database to `transformed_data_db`.

---

## Usage

1. Place the raw data in the designated S3 bucket (`raw-data-bucket`).
2. Trigger the Step Functions workflow manually or via an event.
3. Monitor the workflow in the AWS Management Console.
4. Once completed, check your email for an SNS notification.
5. Use Athena to run queries on the transformed data.

---

