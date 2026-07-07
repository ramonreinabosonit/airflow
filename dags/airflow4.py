from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

argumentos_dag = {
    "retries": 3,
    "retry_delay": timedelta(minutes=15)
}

with DAG(
    dag_id="airflow4",
    description="Prueba paralelize Airflow",
    start_date=datetime(2026, 7, 7),
    schedule="0 8 * * 1,3,5",
    catchup=False
    ) as dag:
    
    # al fin y al cabo, los operators son tareas
    t1 = BashOperator(
        task_id="tarea1",
        bash_command="echo Imprimiendo Tarea 1"
    )

    t2 = BashOperator(
        task_id="tarea2",
        bash_command="echo Imprimiendo Tarea 2"
    )
    
    t3 = BashOperator(
        task_id="tarea3",
        bash_command="echo 'Imprimiendo Tarea 3'"
    )
    
    [t1, t2] >> t3