from airflow import DAG
from datetime import datetime
from airflow.decorators import task

from scripts.pipeline import crear_tareas

with DAG(
    dag_id="airflow5",
    description="Prueba de paralelize en Python",
    start_date=datetime(2026, 6, 7),
    # schedule="0 10 15,30 * 2",
    schedule="0 10 * * 2",
    catchup=True    
) as dag:

    crear_tareas

    # @task()
    # def tarea1():
    #     print("Ejecutando la tarea 1")
    
    # @task()
    # def tarea2():
    #     print("Ejecutando la tarea 2")
        
    # @task()
    # def tarea3():
    #     print("Ejecutando la tarea 3")
        
    # t1 = tarea1()
    # t2 = tarea2()
    # t3 = tarea3()
    
    # [t1, t2] >> t3