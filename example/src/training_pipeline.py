from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime

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
end = EmptyOperator(task_id='end', dag=dag)

start >> end
