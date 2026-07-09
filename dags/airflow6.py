from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.decorators import task

with DAG(
    dag_id="airflow6-spark",
    description="Prueba de job spark",
    start_date=datetime(2026, 7, 8),
    schedule="30 * * * *",
    catchup=False
    
) as dag:
    
    @task()
    def tarea1():
        print("Ejecutando tarea 1")
        
    @task()
    def tarea2():
        print("Ejecutando tarea 2")
    
    t1 = tarea1()
    t2 = tarea2()
    
    t3 = BashOperator(
        task_id="tarea3",
        # bash_command="java -jar /opt/airflow/dags/scripts/Pruebaa.jar"
        # bash_command="spark-submit /opt/airflow/dags/spark/spark.py"
        bash_command="spark-submit --master local[*] /opt/airflow/dags/spark/spark.py"
    )
    
    [t1, t2] >> t3