# from datetime import datetime

# from airflow import DAG

# # modos: poke y reschedule
# # poke: consume mas ya que mantiene el worker en ejecucion
# # reschedule: libera el worker, espera el tiempo y se vuelve
# # a ejecutar pasado el tiempo
# with DAG(
#     dag_id="sensores",
#     description="Prueba de DAG para tarea sensores",
#     start_date=datetime(2026, 7, 2),
#     # schedule=
#     catchup=False
    
# ) as dag:
    
#     # FileSensor(task_id="")
 
#     @task()
#     def 
    
#     # @task()
#     # def prueba():
#     #     estado = True
#     #     if(estado == False):
#     #         print("Condición correcta")
#     #     else:
#     #         print("Error en la condición")    

from datetime import datetime

from airflow import DAG
# from airflow.sensors.bash import BashSensor   
from airflow.sensors.filesystem import FileSensor

with DAG(
    dag_id="sensor_bash",
    description="Ejemplo de BashSensor",
    start_date=datetime(2026, 7, 2),
    catchup=False,
) as dag:

    esperar_fichero = FileSensor(
        task_id="esperar_fichero",
        filepath="/opt/airflow/files/fichero.txt",
        poke_interval=5,
        timeout=30,
        mode="reschedule",
        fs_conn_id="fs_default"
    )