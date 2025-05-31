import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="first_dag",
    start_date=datetime.now() - timedelta(days=1),
    schedule="@daily",
):
    task1 = EmptyOperator(task_id="task1")
    task2 = PythonOperator(
        task_id="task2",
        python_callable=lambda: logging.error("Hello, Airflow!"),
    )
    task3 = BashOperator(
        task_id="task3",
        bash_command="echo \"This is a Bash task!\"",
    )

    task1 >> task2 >> task3
