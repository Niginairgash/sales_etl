from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl_script import extract_data, transform_data, load_data_to_db

default_args = {
    'owner'     : 'airflow',
    'start_date': datetime(2024, 9, 24),
    'retries'   : 1
}

# DAG
with DAG(
    'sales_data_etl', 
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False) as dag:

    #task для извлечения данных
    def extract_task():
        return extract_data(r'path of file')
    
    extract = PythonOperator(
        task_id = 'extract_data',
        python_callable=extract_task
    )

    #task для трансформации данных
    def transform_task():
        data = extract_data(r'path of file')
        return transform_data(data)
    
    transform = PythonOperator(
        task_id = 'transform_data',
        python_callable=transform_task
    )

    #task для загрузки данных
    def load_task():
        data = transform_task()
        # загрузка данных в postgresql.
        load_data_to_db(data, 'postgresql://login:password@localhost:5432/sales_db')


    load = PythonOperator(
        task_id = 'load_data',
        python_callable=load_task
    )

    extract >> transform >> load