from datetime import datetime

from airflow import DAG
from airflow.decorators import task

# Si uso XCom, no uso xcom_push ni pull pero si que lo utilizo
# ya que la comunicacion es correcta, es XCom moderno de Airflow
with DAG(
    dag_id="fichero_dag",
    description="Probando XCom",
    schedule="0 0 * * *",
    start_date=datetime(2026, 6, 2),
    catchup=False
) as dag:
    
    @task()
    def enviar():
        path = "/home/ramonreina/airflow/dags/fichero.py"
        print("Ruta enviada")
        return path
    
    @task()
    def recibir(path):    
        print(f"La ruta recibida es {path}")
    
    t1 = enviar()
    t2 = recibir(t1)
    
    t1 >> t2