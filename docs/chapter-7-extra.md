[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 7: Extra


## Use manual execution arguments

The UI allows you to add manual inputs to a DAG execution. You can use this value in the code through the context or a template.


### Example using context

Input: `{"test_variable": 3}`

```Python 3
def test(**kwargs):
    config = kwargs["dag_run"].conf
    if "test_variable" in config:
        print(config["test_variable"])
    else:
        print("31415")


with DAG(...):
    task_x = PythonOperator(
        task_id=...,
        python_callable=test,
        provide_context=True,
    )
```


### Example using templates

Input: `{"test_variable": 3}`

```Python 3
with DAG(...):
    task_x = BashOperator(
        task_id=...,
        bash_command="echo {{ dag_run.conf['test_variable'] or 31415 }}",
    )
```


## Task groups

Group tasks as a single task. This replaces the old "SubDag" functionality.


### Example

```Python 3
with DAG(...):
    task_a = ...

    task_b = TaskGroup(group_id=...)
    with task_b:
        task_b1 = ...
        task_b2 = ...

        task_b1 >> task_b2

    task_c = ...
```


## Others

  - Variables that have "password", "passwd", "secret", "authorization", "api_key", "apikey" or "access_token" as part of the key will have their value hidden in the UI. This list can be edited in the config file.


[$\leftarrow$ Back to the main page](./apache-airflow.md)
