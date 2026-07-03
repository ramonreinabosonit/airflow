from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
from airflow.models.connection import Connection
from airflow.sensors.filesystem import FileSensor
from airflow.hooks.base import BaseHook

# # Esto deberia de coger VE para no exponer los datos
# c = Connection(
#     conn_id="connection_var",
#     conn_type="fs",
#     login="root",
#     password="root"
# )
# def leer_variable():
#     valor = Variable.get("dorsal")
#     print(f"El dorsal del jugador es el {valor}")
#     return valor

with DAG(
    dag_id="conecctions",
    description="Prueba conexiones y variables",
    start_date=datetime(2026, 7, 3),
    catchup=False
) as dag:
    
    valor = Variable.get("dorsal")
    
    sensor_fichero = FileSensor(
        task_id="leer_variable",
        filepath=valor,
        fs_conn_id="connection_var",
        poke_interval=5,
        timeout=30,
        mode="reschedule"
    )
    
    @task()
    def leer_conexion():
        c = BaseHook.get_connection("connection_var")
        print(f"Tipo: {c.conn_type}")
        print(f"Usuario: {c.login}")
        
    
    sensor_fichero >> leer_conexion()
    
    