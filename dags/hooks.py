import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
from airflow.providers.standard.operators.python import PythonOperator


def check_db():
    red_shift_hook = RedshiftSQLHook("la_virgen_cuantos_datos")
    logging.info("Checking database connection...")

    red_shift_hook.get_conn()
    logging.info("Database connection successful!")


def extract_experiment_data():
    red_shift_hook = RedshiftSQLHook("la_virgen_cuantos_datos")
    logging.info("Extracting experiment data...")

    sql_query = "SELECT * FROM experiments.experimentos_100tifikos"
    df = red_shift_hook.get_pandas_df(sql_query)

    if df.empty:
        logging.warning(
            "No data found in experiments.experimentos_100tifikos table."
        )
    else:
        logging.info(
            f"Extracted {len(df)} rows from experiments.experimentos_100tifikos table.")

    df.to_csv("/tmp/experiment_data.csv", index=False)
    logging.info("Experiment data saved to /tmp/experiment_data.csv")


def copy_shift_data():
    red_shift_hook = RedshiftSQLHook("la_virgen_cuantos_datos")
    logging.info("Copying shift data...")

    sql_query = (
        "SELECT coordenadas "
        "FROM trajectories.precision_desplazamiento "
        "WHERE coordenadas = -0.06843"
    )
    result = red_shift_hook.get_first(sql_query)
    if result is None:
        logging.warning("No data found for the specified coordinates.")
        return

    red_shift_hook.insert_rows("trajectories.comprobar_trayectorias", result)
    logging.info("Data copied to trajectories.comprobar_trayectorias table.")


with DAG(
    dag_id="first_dag",
    start_date=datetime.now() - timedelta(days=1),
    schedule="@daily",
):
    task1 = PythonOperator(
        task_id="task1",
        python_callable=check_db,
    )
    task2 = PythonOperator(
        task_id="task2",
        python_callable=extract_experiment_data,
    )
    task3 = PythonOperator(
        task_id="task3",
        python_callable=copy_shift_data,
    )

    task1 >> task2 >> task3
