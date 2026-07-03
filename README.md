# Formación Big Data - Airflow

Ejercicios Prácticos

# Ejercicio 1

Preguntas de reflexión
-   ¿Qué información permite detectar problemas rápidamente?

    Con las gráficas que muestra Airflow es muy sencillo detectar errores y ver el estado de las tareas y de los dags. Esintutivo ya que por instinto indetificamos el rojo como un fallo y así lo muestra Airflow.

-   ¿Qué diferencias observas entre DAG Runs y Task Instances?

    A simple vista veo que los Dags son los espacios de trabajo que albergan en su interior todas las tareas a realizar, por lo que las Task son las tareas que se realizan en un proyecto, en este caso, en un DAG.

# Ejercicio 2

Preguntas de reflexión
-   ¿Cómo afectan las dependencias al tiempo total de ejecución?

    Las depedencias por norma general incrementan el tiempo de ejecución de cualquier tarea o proyecto. Esto es debido a que importan librerías externas aumentando los recursos a consumir y por ende, aumentando el tiempo de ejecución.

-   ¿Qué tareas podrían paralelizarse?


# Ejercicio 3

Objetivo realizado en la ruta `dags/dag1.py`

Preguntas de reflexión
-   ¿Qué ocurre al cambiar el start_date?

    El parámetro start_date, como su nombre indica, es la fecha y hora en la que se ejecutarán las tareas del DAG, permitiendo modificar en el código cómodamente cuando iniciar las tareas e indicar cuáles son dependientes de otras.

-   ¿Cómo se refleja el DAG en la UI?

    A mi modo de ver, como aparece en la UI de Airflow, veo los DAGs represnetados como si fueran contenedores, es mi mejor relación. Son espacios en los que se ejecutan tareas y se pueden orquestar para que se ejecuten de forma asíncrona o simultáneamente.

# Ejercicio 4

Objetivo realizado en la ruta `dags/prueba.py`

Preguntas de reflexión
-   ¿Qué diferencia hay entre ejecución lógica y real?

    ...

-   ¿Cuándo es peligroso usar catchup?

    Usar catchup puede ser un problema cuando este configurado en True y se tenga definido un schedule_interval. Esto provocará una sobrecarga de los recursos ya que generará muchísimas tareas de manera simultánea.

# Ejercicio 5

Objetivo realizado en la ruta `dags/fichero.py`

Preguntas de reflexión
-   ¿Qué tipo de información es adecuada para XCom?

    Ligeros

-   ¿Por qué no es recomendable usar XCom para datos grandes?

    Recursos

# Ejercicio 6

Objetivo realizado en la ruta `dags/sensores.py`

Preguntas de reflexión
-   ¿Qué impacto tiene cada modo en los recursos?

    El modo poke, al ocupar un worker completo mientras espera a que le llegue la información al sensor, consume muchos recursos y hay que tener cuidado en el caso de diseñar muchos sensores de este tipo.

    Por otro lado el modo reschedule es mucho más ligero en cuanto a recursos, el sensor libera el worker y solo se vuelve a llamar pasado el tiempo de la comprobación. Esto lo hace muy eficiente y es altamente recomendado para esperas largas.

    Por norma general se recomienda usar reschedule mode por su ligereza y optimización, aunque en algunos casos puede ser más útil el poke mode.


-   ¿Cuándo evitarías el uso de sensores?

    ...