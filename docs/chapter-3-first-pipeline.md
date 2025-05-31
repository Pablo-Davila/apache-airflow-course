[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 3: First Airflow pipeline


## The DAG instance

DAGs are created as an instance of the `DAG` class.

  - Import: `from airflow.models import DAG`
  - Mandatory parameters:
      - `dag_id`
      - `default_args` (`dict[str, Any]`): explained below
      - `schedule_interval`: cron, Airflow parameter (i.e., "daily")...
  - Other parameters:
      - `dagrun_timeout`: timeout time
      - `tags` (`list[str]`): these make searching in the UI easier


## Default arguments (`default_args`)

These key-value pairs will be used for all the operators that accept them in this DAG.

  - "start_date": It is the date from which the DAG is allowed to run.
      - This is the only mandatory default argument.
  - "email" (`list[str]`)
  - "email_on_failure" (`bool`): Whether to send an email on failure.
  - "email_on_retr" (`bool`): Whether to send an email on retry.
  - "retries" (`int`): Number of retries.
  - "retry_delay" (`timedelta`): Amout of time to stop before retrying.


## Tasks

Tasks are instances of operator classes such as `DummyOperator`, `BashOperator`, `PythonOperator` or `SimpleHTTPOperator`.

  - The initializer usually has the `task_id` and `dag` parameters.
  - If you create the DAG with a context manager, you will not need to pass it as an argument to operators.


## Enforcing tasks sequences

In this example, `task_b` will be executed after `task_a`.

```Python 3
task_a >> task_b
```

You may specify a whole chain as a single expression:

```Python 3
sensor >> task_a >> task_b >> task_c
```


## Code sample

```Python 3
from airflow.models import DAG

args = {
    "start_date": ...,
}
```


## Connections

  - They allow your DAGs to interact with external systems (MySQL, Posgres, S3...)
  - They can be set up through the UI
  - Connections will be stored at the metadata database and encrypted with a fernet key


[$\leftarrow$ Back to the main page](./apache-airflow.md)
