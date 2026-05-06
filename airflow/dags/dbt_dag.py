from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

DBT_PROJECT_DIR = "/home/maria/dbt_projects/my_data_warehouse"
DBT_EXE = "/home/maria/dbt_env/bin/dbt"

default_args = {
    'owner': 'student',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_data_warehouse_pipeline',
    default_args=default_args,
    description='Ежедневное обновление витрин dbt',
    schedule_interval='@daily',
    catchup=False,
    tags=['dbt'],
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command=f'cd {DBT_PROJECT_DIR} && {DBT_EXE} run',
    dag=dag,
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command=f'cd {DBT_PROJECT_DIR} && {DBT_EXE} test',
    dag=dag,
)

dbt_docs = BashOperator(
    task_id='dbt_docs_generate',
    bash_command=f'cd {DBT_PROJECT_DIR} && {DBT_EXE} docs generate',
    dag=dag,
)

dbt_run >> dbt_test >> dbt_docs