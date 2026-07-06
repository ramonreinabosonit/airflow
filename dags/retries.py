from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.hooks.base import BaseHook

with DAG(
    dag_id="retries_dag",
    description="Ejercicio 8 retries",
    start_date=datetime(2026, 7, 3),
    catchup=False
    
) as dag:
    
    @task(retries=3, retry_delay=timedelta(seconds=5))
    def connection_error():
        BaseHook.get_connection("connection_v")
        print("Conexión establecida")
        
    connection_error()