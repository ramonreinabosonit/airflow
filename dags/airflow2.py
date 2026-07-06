from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

argumentos_dag = {
    "retries":3, 
    "retry_delay":timedelta(minutes=2)
}

with DAG(
    dag_id="airflow2",
    description="Ejercicios Extra Airflow 2",
    start_date=datetime(2026, 7, 6),
    schedule="*/5 * * * *",
    catchup=False,
    default_args=argumentos_dag
) as dag:
    
    @task()
    def tarea1():
        print("Tarea 1")
        
    @task()
    def tarea2():
        print("Tarea 2")
        
    t1 = tarea1()
    t2 = tarea2()
    
    t1 >> t2