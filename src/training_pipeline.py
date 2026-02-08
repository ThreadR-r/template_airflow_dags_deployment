import os
from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator
from dotenv import load_dotenv

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    'training_pipeline',
    default_args=default_args,
    description='Exemple de pipeline d\'entrainement',
    schedule='@daily',
    catchup=False
)

start = EmptyOperator(task_id='start', dag=dag)
hello_world = PythonOperator(
    task_id='hello_world',
    python_callable=lambda: print(f"Hello, world! This is the training_pipeline from the {ENVIRONMENT} environment."),
    dag=dag
)
end = EmptyOperator(task_id='end', dag=dag)

start >> hello_world >> end