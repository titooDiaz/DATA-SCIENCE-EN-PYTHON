<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" />
</p>

# RESUMEN DE LA CARPETA

ya lo sabemos:

Cada línea de un conjunto de datos es una fila, y las comas separan los valores.

Para comprender los datos, debe analizar los atributos de cada columna de datos.

Las bibliotecas de Python son colecciones de funciones y métodos que facilitan diversas funcionalidades sin necesidad de escribir código desde cero y se clasifican en Computación científica, Visualización de datos y Algoritmos de aprendizaje automático.

Muchas bibliotecas de ciencia de datos están interconectadas; por ejemplo, Scikit-learn está construida sobre NumPy, SciPy y Matplotlib.

El formato de los datos y la ruta del archivo son dos factores clave para la lectura de datos con Pandas.

El método read_CSV en Pandas puede leer archivos en formato CSV en un Pandas DataFrame.

Pandas tiene tipos de datos únicos como object, float, Int, y datetime.

Utilice el método dtype para comprobar el tipo de datos de cada columna; los tipos de datos mal clasificados pueden necesitar una corrección manual.

Conocer los tipos de datos correctos ayuda a aplicar las funciones Python adecuadas a columnas específicas.

El uso de resumen estadístico con describe( ) proporciona los rangos de recuento, media, desviación estándar, mínimo, máximo y cuartil para columnas numéricas.

También puede utilizar include='all' como argumento para obtener resúmenes para columnas de tipo objeto.

El resumen estadístico ayuda a identificar posibles problemas, como valores atípicos, que requieren mayor atención.

Utilizando el método info( ) se obtiene un resumen de las 30 filas superiores e inferiores del DataFrame, útil para una rápida inspección visual.

Algunas métricas estadísticas pueden devolver "NaN", lo que indica que faltan valores, y el programa no puede calcular estadísticas para ese tipo de datos específico.

Python puede conectarse a bases de datos mediante código especializado, a menudo escrito en cuadernos Jupyter.

Las interfaces de programación de aplicaciones (API) SQL y las API DB de Python (las más utilizadas) facilitan la interacción entre Python y el SGBD.

Las API SQL se conectan al SGBD con una o varias llamadas API, construyen sentencias SQL como una cadena de texto y utilizan llamadas API para enviar sentencias SQL al SGBD y recuperar resultados y estados.

DB-API, El estándar de Python para interactuar con bases de datos relacionales, utiliza objetos de conexión para establecer y gestionar conexiones a bases de datos y objetos cursor para ejecutar consultas y desplazarse por los resultados.

Los métodos de los objetos de conexión incluyen los comandos cursor(), commit(), rollback() y close().

Puede importar el módulo de base de datos, utilizar la API de conexión para abrir una conexión y, a continuación, crear un objeto cursor para ejecutar consultas y obtener resultados.

Recuerde cerrar la conexión a la base de datos para liberar recursos.