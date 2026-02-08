import os
from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from dotenv import load_dotenv

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    f"inference_pipeline_{ENVIRONMENT}",
    default_args=default_args,
    description='Exemple de pipeline d\'inférence',
    schedule='@hourly',
    catchup=False
)

start = EmptyOperator(task_id='start', dag=dag)
end = EmptyOperator(task_id='end', dag=dag)

start >> end
