# Streaming Finance Data with AWS Lambda

- Author: Carmen Ruan
- Date Created: 05/18/2021
- Class: CIS 9760

## Project Objective - 

Provisioning a Lambda function to generate near real time finance data records for interactive querying and analysis. This project is made to collect one full day's worth of stock HIGH and LOW prices for the 10 stocks which includes: Facebook (FB) Shopify (SHOP) Beyond Meat (BYND) Netflix (NFLX) Pinterest (PINS) Square (SQ) The Trade Desk (TTD) Okta (OKTA) Snap (SNAP) Datadog (DDOG). The time set is to be May 11th, 2021 at 5 minute intervals. 

## Basic Project Infrastructure Flow -  

yfinance package layered into --> Lambda Function (triggered every 5 minutes via the usage of Cloudwatch Events) --> Kinesis Delivery Stream --> Kinesis Firehose --> S3 Bucket --> AWS Athena



## AWS Kinesis Configuration Page - 

![kinesis_config](C:\Users\cabul\OneDrive\Desktop\Academics\Spring Semester\CIS 9760\project03\assets\kinesis_config.png)