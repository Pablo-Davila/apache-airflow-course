[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 4: Improve your DAGs


## Hooks

They are interfaces to connect to external services (DBs, AWS...).

  - They have functions such as "get_pandas_df" (from a DB), "run_query", etc.
  - They can be used from an operator or to create your own operators

> **Important**: To use Amazon's hooks (for example) you will need to install their specific dependencies with `pip install apache-airflow[amazon]`


## Python tasks

Python tasks can be defined either through a `PythonOperator` instance or by using the `task` decorator (preferred).

```Python 3
from airflow import DAG
from airflow.decorators import task

with DAG(...):
    @task
    def count_to_5():
        for i in range(1, 6):
            print(i)
    
    task_a = count_to_5()
```

```Python 3
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

with DAG(...):
    task_a = PythonOperator(
        task_id="task2",
        python_callable=lambda: logging.error("Hello, Airflow!"),
    )
```


## Create DAGs with the `@dag` decorator

[TODO]


## Variables

They are values stored in a key-value fashion.


### Create variables

  - Through the UI.
  - Through the CLI:
      - `airflow variables -s email test@test.com`
      - `airflow variables -i variables.json`
  - Through environment variables (i.e. `AIRFLOW_VAR_EMAIL=test@test.com`)

> The guy in the course says that Airflow makes a query to the DB for each variable, so it is more efficient to store many of them as a single JSON-formatted variable
> I am not sure whether to believe that


### Use a variable

```Python 3
from airflow.models import Variable

email = Variable.get("email")
multivar = Variable.get("multivar", deserialize_json=True)
```


## Cross-communication (XCom)

This allows to share information between tasks.

  - This information should not be too big, as it will be inserted in the metadata database.


### Save data to XCom

  - `do_xcom_push=True`: This argument for operators allows you to automatically save the task's return value. For a `PythonOperator` task, it is the function's return value, for a `BashOperator` task it will be the command's stdout.

    ```Python 3
    task_x = PythonOperator(
        task_id=...,
        python_callable=...,
        do_xcom_push=True,
    )
    ```

  - `provide_context=True`: In `PythonOperator` instances this sends the Jinja context information to the callable.
  
    ```Python 3
    def mycallable(**context):
        ti = context["task_instance"]
        ti.xcom_push(
            key="test_key",
            value="test_value",
        )
    
    ...

    task_x = PythonOperator(
        task_id=...,
        python_callable=mycallable,
        provide_context=True,
    )
    ```


### Load data form XCom

```Python 3
def mycallable(**context):
    ti = context["task_instance"]
    return_value = ti.xcom_pull(task_ids="previous_task_id")
    print(value)

    key_value = ti.xcom_pull(task_ids="previous_task_id", key="my_key")
    print(value)

...

task_x = PythonOperator(
    task_id=...,
    python_callable=mycallable,
    provide_context=True,
)
```

## Templates and macros

These can be used in Bash commands and will be replaced with a computed value.

  - You will need to check the operator's documentation to see if it allows using templates. The template_fields attribute should not be empty.


### Example: Timestamp

```Python 3
bash_test = BashOperator(
    task_id="task_id",
    bash_command="echo {{ ts }}",
)
```


### Example: Variable (basic)

Here we take the "email" variable and insert it in the Bash command.

```Python 3
bash_test = BashOperator(
    task_id="task_id",
    bash_command="echo {{ var.value.email }}",
)
```


### Example: Variable (json)

Here we take the "multivar" JSON-formatted variable and insert it in the Bash command.

```Python 3
bash_test = BashOperator(
    task_id="task_id",
    bash_command="echo {{ var.json.multivar }}",
)
```


### Example: XCom value

```Python 3
bash_test = BashOperator(
    task_id="task_id",
    bash_command="echo {{ ti.xcom_pull(task_ids=\"previous_task_id\")  }}",
)
```


[$\leftarrow$ Back to the main page](./apache-airflow.md)
