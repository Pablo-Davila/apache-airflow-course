[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 2: Basic concepts


## Directed Acylic Graphs (DAGs)

It is a way to represent a collection of tasks and the relationships and dependencies among them.


## Operators

They are tasks inside a workflow.

  - They can be represented as nodes in a DAG.
  - They must be idempotent (have the same result when run multiple times).
  - In Python 3, operators are classes that inherit from `BaseOperator`.


### Types of operators

  - Actions: Postgres, MySQL, Sagemaker Training..
  - Data transfer: S3ToRedshift, BigQueryToGCS, MySqlToS3...
  - Sensors: S3Sensor, SQL Sensor...


[$\leftarrow$ Back to the main page](./apache-airflow.md)
