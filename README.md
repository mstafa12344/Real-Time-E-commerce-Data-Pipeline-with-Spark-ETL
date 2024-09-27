# Real-Time E-commerce Data Pipeline with Spark ETL

## Project Overview

This project focuses on designing and implementing an ETL (Extract, Transform, Load) pipeline for **ShopEase**, a hypothetical e-commerce platform. The pipeline is developed using **Apache Spark** and is designed to handle both batch and real-time data processing, enabling analytics and reporting for business insights.

## Scenario

**ShopEase** generates a vast amount of data daily, including:
- **User Activity Logs**: Website clickstream data.
- **Transaction Records**: Data on purchases, refunds, and returns.
- **Inventory Updates**: Stock levels, restocks, and product info changes.
- **Customer Feedback**: Reviews and ratings from users.

The goal is to process this data and support real-time analytics using Apache Spark, with both batch and streaming capabilities.

## Project Requirements

The pipeline includes the following tasks:

### 1. Data Ingestion

- **Batch Data**: 
  - Load historical data from CSV and JSON files stored locally.
  
- **Real-Time Data**: 
  - Simulate real-time ingestion of user activity logs from Kafka.

### 2. Data Processing and Transformation

- **Using RDDs**:
  - Filter corrupted or incomplete transaction records.
  - Anonymize user IDs for privacy compliance.
  
- **Using DataFrames**:
  - Clean and standardize inventory data.
  - Join user activity logs with transaction data to analyze user behavior leading to purchases.
  
- **Using Spark SQL**:
  - Create SQL views and execute queries to compute:
    - Top 10 most purchased products in the last month.
    - Monthly revenue trends.
    - Inventory turnover rates.

### 3. Real-Time Streaming Processing (Optional but Recommended)

Set up a **Spark Streaming** job to process live user activity logs from Kafka and compute real-time metrics like:
- Active users per minute.
- Real-time conversion rates.
- Detect unusual spikes in user activities.

### 4. Data Storage

- **Batch-Processed Data**: Store in **Parquet** format in a local data lake.
- **Real-Time Metrics**: Use **Redis** or **PostgreSQL** for in-memory storage of real-time data.

## Tools and Technologies

- **Apache Spark**: For batch and real-time ETL processing.
- **Kafka**: To simulate real-time data streams for user activity logs.
- **Hadoop HDFS / Local File System**: To store and process historical data.
- **Redis / PostgreSQL**: For real-time metrics storage.
- **PySpark/Scala**: Spark programming languages for data transformations.
- **Spark SQL**: To create views and execute analytical queries.
