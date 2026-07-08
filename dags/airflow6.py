from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="airflow6-spark",
    description="Prueba de job spark",
    start_date=datetime(2026, 7, 8),
    schedule="30 * * * *",
    catchup=False
    
) as dag:
    
    t1 = BashOperator(
        task_id="tarea1",
        # bash_command="java -jar /opt/airflow/dags/scripts/Pruebaa.jar"
        # bash_command="spark-submit /opt/airflow/dags/spark/spark.py"
        bash_command="spark-submit --master local[*] /opt/airflow/dags/spark/spark.py"
    )
    
    t1