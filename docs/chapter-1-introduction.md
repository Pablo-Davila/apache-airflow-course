[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 1: Introduction


## Airflow components

  - DAG processor: parses DAG files and serializes them in the metadata database.
  - Scheduler: triggers scheduled workflows and submits tasks to the executor.
  - Executor: defines how to execute tasks.
      - Sequential executor (Por defecto)
      - Local executor: tareas paralelas en local
      - Docker executor
      - Celery executor
      - Custom made executors
  - Web server: provides a user interface (UI) to inspect, trigger and debug the behaviour of dags and tasks.
  - Metadata database: stores information about DAGs connections, variables, users...
      - It may be any DB compatible with SQLAlchemy.


## Key concepts

  - DAG: Directed Acyclic Graph. It is a way to represent workflows through tasks and their relationships.
  - Operator: a template for an Airflow task
  - Task: It is an individual piece of work. In code, it is an instance of an operator or an `@task` decorated function.
  - Task instances: an execution of a task (with a timestamp)
  - Workflow: a combination of al the previous ones


## Why Airflow

  - Scalability with Kubernetes
  - Configuration as code
  - Pipelines can be created dynamically
  - Everything is run and written in Python
  - Extensible
  - Strong and nice UI (workflow monitoring)
  - Integration witll all major cloud services and databases (AWS, Google Cloud, Azure, DBs, Datadog, Docker, Kubernetes...)
      - Google Cloud offers Airflow as a service with Google Cloud Orchestrator
      - AWS has operatos for many of their products (Sagemaker...)
  - Used by many huge tech companies
  - Active community


### Alternatives

  - Matillion: more expensive, less flexibility
  - Talend: more expensive, less flexibility
  - Pentaho: more expensive, less flexibility
  - Luigi: no scheduler
  - Prefect: less community
  - Cronjobs: no monitorization, no UI...


## Installation and config


### Directly

 1. Install Airflow: `pip install apache-airflow`.
 2. The `AIRFLOW_HOME` environment variable determines the path to the directory where Airflow will save its files. The default value is `$HOME`.
 3. Initialize the metadata database: `airflow initdb`.
 4. Start webserver: `airflow webserver`
      - By default it is attached to the current terminal
      - You may use the `-D` option to run it in detached mode
 5. Start scheduler: `airflow scheduler`
      - By default it is attached to the current terminal
      - You may use the `-D` option to run it in detached mode


### Using docker

Just use the official "docker-compose.yaml" file [provided by Airflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).


[$\leftarrow$ Back to the main page](./apache-airflow.md)
