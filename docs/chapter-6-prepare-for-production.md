[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 6: Prepare for production

> It is never a good idea to use the `SequentialExecutor` on production


## Types of deployments

  - Single cloud server:
      - Local Executor
      - External metadata database
      - Performance will depend on available resources
  - Multiple cloud servers:
      - Machine 1: Web server and scheduler
      - Machine 2: Metadata database
      - Machines 2, ..., n: Celery executor -> Distributes load among multiple nodes
  - (Docker) containers:
      - A single machine
      - One container for each component
  - Kubernetes: Similar to the containers option, but with horizontal scalability
  - Airflow as a service:
      - These are usually based on Kubernetes, but this is managed by the cloud provider
      - Examples: Google Cloud Composer, Astronomer


## Set up configuration

The `airflow.cfg` file is always at the root of Airflow's home directory. The default file includes descriptions for most configuration options.

  - The `executor` value allows you to choose among `SequentialExecutor`, `LocalExecutor`, `CeleryExecutor`...
  - There are options to store logs using a cloud service
  - There are options to connect an external SMTP server. This allows Airflow to send emails.


## Documentation


### DAG docs

You may add docs to a DAG by updating the `doc_md` attribute.


### Example

```Python 3
from airflow import DAG

with DAG(...) as dag:
    dag.doc_md = "These are the dag's docs!"
```


### Task docs

You may add docs to a task by updating any of the following attributes:
  - `doc`: Plain text
  - `doc_md`: Makdown
  - `doc_json`: JSON
  - `doc_yaml`: YAML
  - `doc_rst`: ReStructuredText


[$\leftarrow$ Back to the main page](./apache-airflow.md)
