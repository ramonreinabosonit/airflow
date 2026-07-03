from datetime import datetime, timedelta

# Operators, necesario para operar
# from airflow.operators import BashOperator

# Objeto DAG, necesario para crear una instancia DAG
from airflow import DAG

from airflow.decorators import task

# crear un DAG simple
with DAG(
    dag_id="prueba1",
    description="Probando los DAGs",
    start_date=datetime(2026,6,1),
    schedule="0 * * * *",
    catchup=False
) as dag:
    
    @task()
    def tarea1():
        print("Ejecutando tarea 1")
    
    @task()
    def tarea2():
        print("Ejecutando tarea 2")
    
    @task()
    def tarea3():
        print("Ejecutando tarea 3")

    #Ordern de ejecucion
    t1 = tarea1()
    t2 = tarea2()
    t3 = tarea3()
    
    t1 >> t2 >> t3
