from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
from airflow.hooks.base import BaseHook
from airflow.sensors.filesystem import FileSensor
from airflow.models import Variable

with DAG(
    dag_id="dag_definitivo",
    description="",
    start_date=datetime(2026, 7, 3),
    catchup=False
    
) as dag:
    
    valor = Variable.get("dorsal")
    
    @task(retries=3 ,retry_delay=timedelta(seconds=10))
    def prueba_retry_connection():
        try:
            BaseHook.get_connection("prueba_retry")
            print("Conexión establecida")
        except:
            raise Exception("Ha habido un error en la conexión.")
        
    # 
    sensor_fichero = FileSensor(
        task_id="leer_variable",
        filepath="valor",
        fs_conn_id="connection_var",
        poke_interval=5,
        timeout=30,
        mode="reschedule"
    )
    
    @task()
    def enviar_ruta_modificada(valor):
        ruta_final = valor+"/fichero2.txt"
        return ruta_final
    
    @task()
    def recibir_ruta(ruta_final):
        print(f"La ruta final es {ruta_final}")
    
    t1 = enviar_ruta_modificada(valor)
    t2 = recibir_ruta(t1)
    
    
    prueba_retry_connection() >> t1 >> t2