from airflow import DAG
from datetime import datetime
from airflow.decorators import task

from scripts.pipeline import crear_tareas

with DAG(
    dag_id="airflow5",
    description="Prueba de paralelize en Python",
    start_date=datetime(2026, 6, 7),
    # schedule="0 10 15,30 * 2",

    # Schedule para todos los Martes a las 10:00
    schedule="0 10 * * 2",
    catchup=True    
) as dag:

    crear_tareas