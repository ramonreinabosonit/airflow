from airflow import DAG
from datetime import datetime
from scripts.pipeline import crear_tareas

with DAG(
    dag_id="airflow5-days",
    description="DAG 2 para días",
    start_date=datetime(2026, 6, 1),
    
    # Schedule para los días 15 y 30 a las 10:30
    schedule="30 10 15,30 * *",
    catchup=True
) as dag:
    
    crear_tareas