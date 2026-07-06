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

    Se pueden paralelizar las tareas que no son dependientes entre ellas y que se pueden ejecutar de forma independiente. Un ejemplo sería un par de tareas que trabajan con distintos datos y no comparten resultados, pues este par de tareas se podrían paralelizar, reduciendo el tiempo de ejecución considerablemente y sacando más partido a los recursos.    

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

    La ejecución lógica es la fecha y hora que procesa un DAG, mientras que la ejecución real es el momento en el que airflow ejecuta ese DAG. Un ejemplo para verlo más claro sería un DAG programado a las 10:00 (ejecución lógica) pero puede ejecutarse minutos más tarde (ejecución real).

-   ¿Cuándo es peligroso usar catchup?

    Usar catchup puede ser un problema cuando este configurado en True y se tenga definido un schedule_interval. Esto provocará una sobrecarga de los recursos ya que generará muchísimas tareas de manera simultánea.

# Ejercicio 5

Objetivo realizado en la ruta `dags/fichero.py`

Preguntas de reflexión
-   ¿Qué tipo de información es adecuada para XCom?

    La información más adecuada son las pequeñas tareas y ligeras, como rutas de archivos, ids, parámetros o resultados simples. Esta información debe de ser ligera para poder enviarse entre tareas con facilidad y no provocar retrasos y problemas.

-   ¿Por qué no es recomendable usar XCom para datos grandes?

    No es nada recomendable el uso de información pesada para XCom, provoca problemas de rendimiento ya que consume más recursos la transferencia de datos pesados. Además, la información es almacenada en la base de datos y por ello, al almacenar datos grandes ocupa más espacio en la BD y provoca tardanza en las consultas, impactando directamente en el rendimiento de las mismas.

# Ejercicio 6

Objetivo realizado en la ruta `dags/sensores.py`

Preguntas de reflexión
-   ¿Qué impacto tiene cada modo en los recursos?

    El modo poke, al ocupar un worker completo mientras espera a que le llegue la información al sensor, consume muchos recursos y hay que tener cuidado en el caso de diseñar muchos sensores de este tipo.

    Por otro lado el modo reschedule es mucho más ligero en cuanto a recursos, el sensor libera el worker y solo se vuelve a llamar pasado el tiempo de la comprobación. Esto lo hace muy eficiente y es altamente recomendado para esperas largas.

    Por norma general se recomienda usar reschedule mode por su ligereza y optimización, aunque en algunos casos puede ser más útil el poke mode.


-   ¿Cuándo evitarías el uso de sensores?

    Los sensores habría que evitarlos cuando se desconoce el tiempo de respuesto o puede ser largo, los sensores se evitarían en estos casos ya que pueden consumir un exceso de recursos e innecesario.

# Ejercicio 7

Objetivo realizado en la ruta `dags/varconnections.py`

Preguntas de reflexión
-   ¿Qué ventajas aporta este enfoque?

    El uso de variables es una práctica bastante cómoda ya que en caso de querer modificar una variable no hace falta modificar el código y subirlo de nuevo, tan solo hay que acceder al panel de airflow y modificar dicha variable. Otra ventaja es que evita exponer información sensible del propio código fuente.

-   ¿Qué riesgos existen si se abusa de Variables?

    Si se usan demasiadas variables, es difícil gestionar y mantener la configuración ya que puede ser tedioso modificar las variables además de la complejidad de comprensión del código, ya que estas variables no están presentes en el código, si no en airflow. Además de lo que supone la seguridad, ya que almacenar variables con datos sensibles no es una buena práctica y puede provocar problemas de seguridad.

# Ejercicio 8

Objetivo realizado en la ruta `dags/retries.py`

Preguntas de reflexión
-   ¿Cuándo es adecuado usar retries?

    Los retries son ideales para casos en los que se puede perder la comunicación en un breve momento, permite como almacenar en una cola las tareas para volver a ejecutarlas pasado x tiempo. Un buen caso sería para caídas de red o de un servicio para intentar ejecutarlo de nuevo. Hay que evitar de usarlo cuando es un error que no se va a arreglar, por ejemplo, el envío de parámetros incorrectos, por mucho retries que haga siempre va a dar error y se perderá ese tiempo reintentando.

-   ¿Qué información debe aparecer en los logs?

    En los logs debe de aparecer el error que ha saltado junto con una respuesta simplificada en el que se informa brevemente la causa del error, como la falta de un parámetro, valores incorrectos, etc... Es importante añadir en el log la fecha y hora en el que ha ocurrido dicha acción, esto ayuda muchísimo al mantenimiento.

# Ejercicio 9

Objetivo realizado en la ruta `dags/`

Preguntas de reflexión
-   ¿Cómo priorizarías la resolución?

    Para solucionar una incidencia, lo primero que se debe de hacer es buscar la causa por la que el servicio o el proceso ha terminado o ha fallado. Posteriormente, en caso de saber el origen del fallo, sería plantear un cambio que no provoque otro tipo de problemas y corrija nuestro problema inicial. Cuando esté el cambio implementado, habría que ejecutar y hacer distintas pruebas, sobre todo, probar el proceso que provocó el fallo.

-   ¿Qué métricas serían útiles para anticipar el problema?

    Podemos aplicar y utilizar distintas métricas que nos pueden ayudar para preveer un problema. Por ejemplo, el número de reintentos, el monitoreo de recursos utilizados, los tiempos de respuesta de las APIs o de la propia base de datos.


# Ejercicio 10

Objetivo realizado en la ruta `dags/ejercicio10.py`

Preguntas de reflexión
-   ¿Qué cambios aumentarían la mantenibilidad?

    Para seguir con una buena mantenibilidad, habría que preparar el proceso para que se mantenga de forma autónoma lo máximo posible. Para ello, es recomendable programar reinicios automáticos periodicamente para limpiar caché y liberar espacio. La parte de retries es importante para reintentar en caso de errores y no perder datos o funciones del proceso. Tener disponibles un apartado de logs mejora mucho el mantenimiento ya que se puede supervisar todo lo que hace el usuario y se ejecuta en el proceso. 

-   ¿Qué decisiones podrían causar problemas en producción?

    No tener un buen control de errores provoca problemas en producción ya que si se da algún tipo de error puede que el proceso se cierre o termine por si solo, además de perder tiempo buscando el error que es. Si hacemos un buen uso de try/catch o en este caso try/except todo estará más controlado y más legible.
