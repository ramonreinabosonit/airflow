from airflow import DAG
from datetime import datetime

from airflow.operators.bash import BashOperator

with DAG(
    dag_id="airflow1",
    description="Ejercicio extra Airflow 1",
    start_date=datetime(2026, 7, 6),
    schedule="*/10 * * * *",
    catchup=False
    
) as dag:
    
    t1 = BashOperator(
        task_id="tarea1",
        bash_command="""echo 'Probando tarea1' """
        
    )

    t2 = BashOperator(
        task_id="tarea2",
        bash_command="""echo 'Probando tarea1' """        
    )
    
    t1 >> t2