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

# Comandos:
<table>
    <tbody><tr>
        <td><b>Package/Method</b></td>
        <td><b>Description</b></td>
        <td><b>Code Example</b></td>
    </tr>
    <tr>
        <td>Read CSV data set</td>
        <td>Read the CSV file containing a data set to a pandas data frame</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df </span><span class="pun">=</span><span class="pln"> pd</span><span class="pun">.</span><span class="pln">read_csv</span><span class="pun">(&lt;</span><span class="pln">CSV_path</span><span class="pun">&gt;,</span><span class="pln"> header </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">)</span><span class="pln"> </span><br><span class="com"># load without header </span><br><span class="pln">df </span><span class="pun">=</span><span class="pln"> pd</span><span class="pun">.</span><span class="pln">read_csv</span><span class="pun">(&lt;</span><span class="pln">CSV_path</span><span class="pun">&gt;,</span><span class="pln"> header </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><br><span class="com"># load using first row as header</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-0">Copied!</span></button></pre> Note: The labs in this course run in JupyterLite environment. In JupyterLite environment, you'll need to download the required file to the local environment and then use the local path to the file as the CSV_path. However, in case you are using JupyterLabs, or any other Python compiler on your local machine, you can use the URL of the required file directly as the CSV_path.  </td>
    </tr>
    <tr>
        <td>Print first few entries</td>
        <td>Print the first few entries (default 5) of the pandas data frame</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">head</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="com">#n=number of entries; default 5</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-1">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Print last few entries</td>
        <td>Print the last few entries (default 5) of the pandas data frame</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">tail</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="com">#n=number of entries; default 5</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-2">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Assign header names</td>
        <td>Assign appropriate header names to the data frame</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">columns </span><span class="pun">=</span><span class="pln"> headers</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-3">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Replace "?" with NaN</td>
        <td>Replace the entries "?" with NaN entry from Numpy library</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df </span><span class="pun">=</span><span class="pln"> df</span><span class="pun">.</span><span class="pln">replace</span><span class="pun">(</span><span class="str">"?"</span><span class="pun">,</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">nan</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-4">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Retrieve data types</td>
        <td>Retrieve the data types of the data frame columns</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">dtypes</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-5">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Retrieve statistical description</td>
        <td>Retrieve the statistical description of the data set. Defaults use is for only numerical data types. Use include="all" to create summary for all variables</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">describe</span><span class="pun">()</span><span class="pln"> </span><span class="com">#default use df.describe(include="all")</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-6">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Retrieve data set summary</td>
        <td>Retrieve the summary of the data set being used, from the data frame</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">info</span><span class="pun">()</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-7">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Save data frame to CSV</td>
        <td>Save the processed data frame to a CSV file with a specified path</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">to_csv</span><span class="pun">(&lt;</span><span class="pln">output CSV path</span><span class="pun">&gt;)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-8">Copied!</span></button></pre></td>
    </tr>
</tbody></table>