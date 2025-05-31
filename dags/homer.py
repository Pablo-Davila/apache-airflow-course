import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="first_dag",
    schedule="@daily",
    default_args={
        "owner": "homer",
        "start_date": datetime.now() - timedelta(days=1),
    },
):
    task1 = PythonOperator(
        task_id="task1",
        python_callable=lambda: logging.info(
            "El uso de Airflow en la universidad de Springfield"
        ),
    )
    task2 = PythonOperator(
        task_id="task2",
        python_callable=lambda: logging.info(
            "El otro día mi hija me dijo que Airflow no se utilizaba "
            "en la universidad de Springfield, y yo le dije: qué no "
            "Lisa? qué no?"
        ),
    )
    task3 = PythonOperator(
        task_id="task3",
        python_callable=lambda: logging.info(150 * "Púdrete Flanders"),
    )

    task1 >> task2 >> task3
