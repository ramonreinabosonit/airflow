from airflow import DAG 
from datetime import datetime
# from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="airflow3",
    description="Probando rutinas Java airflow",
    start_date=datetime(2026, 7, 7),
    schedule="*/15 * * * 1",
    catchup=False
    
) as dag:
    
    t1 = BashOperator(
        task_id="tarea1",
        # bash_command="java -jar /home/ramonreina/airflow/dags/scripts/Pruebaa.jar"
        # bash_command="java -jar /mnt/c/users/ramon.reina/desktop/Pruebaa.jar"
        bash_command="java -jar /opt/airflow/dags/scripts/Pruebaa.jar"
    )
    
    # Es importante tener exactamente la ruta del fichero .jar
    t2 = BashOperator(
        task_id="tarea2",
        # bash_command="java -jar /home/ramonreina/airflow/dags/scripts/Prueba2.jar"
        bash_command="java -jar /opt/airflow/dags/scripts/Pruebaa.jar"

    )

    t1 >> t2