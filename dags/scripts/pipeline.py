from airflow.decorators import task

def crear_tareas():
    
    @task()
    def tarea1():
        print("Ejecutando la tarea 1")
    
    @task()
    def tarea2():
        print("Ejecutando la tarea 2")
        
    @task()
    def tarea3():
        print("Ejecutando la tarea 3")
        
    t1 = tarea1()
    t2 = tarea2()
    t3 = tarea3()
    
    [t1, t2] >> t3