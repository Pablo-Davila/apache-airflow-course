[$\leftarrow$ Back to the main page](./apache-airflow.md)


# Chapter 5: Advanced concepts


## Pools

To execute a task it must take a slot from a pool. If the pool runs out of slots, tasks will have to wait until tere are free slots.

  - By default, all tasks take slots from the "default_pool".
  - If, for example, you have higher-priority tasks you may create a new pool (using the UI) and assign them to it.
  - You can choose the number of slots for each pool.
  - To specify the pool assigned to a task you can use the `pool` argument for operators.


## Branching

We can add conditional nodes to DAGs. This can be done using `PythonBranchOperator`.


### Example

```Python 3
def bifurcation(**context):
    ti = context["task_instance"]
    api_response = ti.xcom_pull(task_id="api_call")

    number = json.loads(api_response)[0]["random"]

    if number <= 5:
        return "le5"
    else:
        return "gt5"


with DAG(...):
    api_call = SimpleHttpOperator(
        task_id="api_call",
        http_conn_id="random_number",
        method="GET",
        data={"min": 0, "max": 10},
        xcom_push=True,
    )

    bifurcation_task = BranchPythonOperator(
        task_id="bifurcation_task",
        python_callable=bifurcation,
        provide_context=True,
    )

    le5 = DummyOperator(task_id="le5")
    gt5 = DummyOperator(task_id="gt5")

api_call >> bifurcation_task >> [le5, gt5]
```


## Create DAGs dynamically


### Example

```Python 3
def create_dag(dag_id, ...)
    dag = DAG(dag_id, ...)

    with dag:
        ...

    return dag

...

for ...:
    dag_id = ...
    globals()[dag_id] = create_dag(dag_id, ...)
```


## Execute a DAG from another DAG


### Example

Here, "example_dag" is a DAG defined in a diferent module.

```Python 3
with DAG(...):
    ...

    trigger = TriggerDagRunOperator(
        task_id="trigger",
        trigger_dag_id="example_dag",
    )

    ...
```


### Wait for external DAG completion

You can do this by adding the `wait_for_completion=True` parameter to `TriggerDagRunOperator`.


[$\leftarrow$ Back to the main page](./apache-airflow.md)
