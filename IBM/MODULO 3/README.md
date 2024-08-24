<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" />
</p>

# Resumen de la lección

Herramientas como la función 'describir' de pandas pueden calcular rápidamente medidas estadísticas clave como la media, la desviación estándar y los cuartiles para todas las variables numéricas en su marco de datos. 

Utilice la función 'value_counts' para resumir datos en diferentes categorías para datos categóricos. 

Los diagramas de caja ofrecen una representación más visual de la distribución de datos numéricos, indicando características como la mediana, los cuartiles y los valores atípicos.

Los gráficos de dispersión son excelentes para explorar las relaciones entre variables continuas, como el tamaño y el precio del motor, en un conjunto de datos de automóviles.

Utilice el método 'groupby' de Pandas para explorar las relaciones entre variables categóricas.

Utilice tablas dinámicas y mapas de calor para mejores visualizaciones de datos.

La correlación entre variables es una medida estadística que indica cómo los cambios en una variable podrían estar asociados con cambios en otra variable.

Al explorar la correlación, utilice gráficos de dispersión combinados con una línea de regresión para visualizar las relaciones entre las variables.

Las funciones de visualización como regplot, de la biblioteca seaborn , son especialmente útiles para explorar la correlación.

La correlación de Pearson , un método clave para evaluar la correlación entre variables numéricas continuas, proporciona dos valores críticos: el coeficiente, que indica la fuerza y ​​la dirección de la correlación, y el valor P, que evalúa la certeza de la correlación.

Un coeficiente de correlación cercano a 1 o -1 indica una fuerte correlación positiva o negativa, respectivamente, mientras que uno cercano a cero sugiere que no hay correlación.

En el caso de los valores P, los valores inferiores a 0,001 indican una gran certeza en la correlación, mientras que los valores mayores indican una menor certeza. Tanto el coeficiente como el valor P son importantes para confirmar una fuerte correlación.

Los mapas de calor proporcionan un resumen visual completo de la fuerza y ​​la dirección de las correlaciones entre múltiples variables.

# Comandos y sintaxis
<table>
<tbody><tr>
<th width="20%">Package/Method </th><th width="30%">Description </th><th width="50%">Code Example</th>
</tr>
    <tr>
        <td>Complete dataframe correlation</td>
        <td>Correlation matrix created using all the attributes of the dataset. </td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">corr</span><span class="pun">()</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-0">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Specific Attribute correlation</td>
        <td>Correlation matrix created using specific attributes of the dataset.</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">[[</span><span class="str">'attribute1'</span><span class="pun">,</span><span class="str">'attribute2'</span><span class="pun">,...]].</span><span class="pln">corr</span><span class="pun">()</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-1">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Scatter Plot</td>
        <td>Create a scatter plot using the data points of the dependent variable along the x-axis and the independent variable along the y-axis.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="kwd">from</span><span class="pln"> matlplotlib </span><span class="kwd">import</span><span class="pln"> pyplot </span><span class="kwd">as</span><span class="pln"> </span></code></li><li class="L1"><code><span class="pln">plt plt</span><span class="pun">.</span><span class="pln">scatter</span><span class="pun">(</span><span class="pln">df</span><span class="pun">[[</span><span class="str">'attribute_1'</span><span class="pun">]],</span><span class="pln">df</span><span class="pun">[[</span><span class="str">'attribute_2'</span><span class="pun">]])</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-2">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Regression Plot</td>
        <td>Uses the dependent and independent variables in a Pandas data frame to create a scatter plot with a generated linear regression line for the data.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="kwd">import</span><span class="pln"> seaborn </span><span class="kwd">as</span><span class="pln"> sns </span></code></li><li class="L1"><code><span class="pln">sns</span><span class="pun">.</span><span class="pln">regplot</span><span class="pun">(</span><span class="pln">x</span><span class="pun">=</span><span class="str">'attribute_1'</span><span class="pun">,</span><span class="pln">y</span><span class="pun">=</span><span class="str">'attribute_2'</span><span class="pun">,</span><span class="pln"> data</span><span class="pun">=</span><span class="pln">df</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-3">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Box plot</td>
        <td>Create a box-and-whisker plot that uses the pandas dataframe, the dependent, and the independent variables. </td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="kwd">import</span><span class="pln"> seaborn </span><span class="kwd">as</span><span class="pln"> sns </span></code></li><li class="L1"><code><span class="pln">sns</span><span class="pun">.</span><span class="pln">boxplot</span><span class="pun">(</span><span class="pln">x</span><span class="pun">=</span><span class="str">'attribute_1'</span><span class="pun">,</span><span class="pln">y</span><span class="pun">=</span><span class="str">'attribute_2'</span><span class="pun">,</span><span class="pln"> data</span><span class="pun">=</span><span class="pln">df</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-4">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Grouping by attributes</td>
        <td>Create a group of different attributes of a dataset to create a subset of the data.</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df_group </span><span class="pun">=</span><span class="pln"> df</span><span class="pun">[[</span><span class="str">'attribute_1'</span><span class="pun">,</span><span class="str">'attribute_2'</span><span class="pun">,...]]</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-5">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>GroupBy statements</td>
        <td>a. Group the data by different categories of an attribute, displaying the average value of numerical attributes with the same category.<br>b. Group the data by different categories of multiple attributes, displaying the average value of numerical attributes with the same category.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">a</span><span class="pun">.</span></code></li><li class="L1"><code><span class="pln">df_group </span><span class="pun">=</span><span class="pln"> </span></code></li><li class="L2"><code><span class="pln">df_group</span><span class="pun">.</span><span class="pln">groupby</span><span class="pun">([</span><span class="str">'attribute_1'</span><span class="pun">],</span><span class="pln">as_index</span><span class="pun">=</span><span class="kwd">False</span><span class="pun">).</span><span class="pln">mean</span><span class="pun">()</span><span class="pln"> </span></code></li><li class="L3"><code><span class="pln">b</span><span class="pun">.</span><span class="pln"> </span></code></li><li class="L4"><code><span class="pln">df_group </span><span class="pun">=</span><span class="pln"> df_group</span><span class="pun">.</span><span class="pln">groupby</span><span class="pun">([</span><span class="str">'attribute_1'</span><span class="pun">,</span><span class="pln"> </span></code></li><li class="L5"><code><span class="str">'attribute_2'</span><span class="pun">],</span><span class="pln">as_index</span><span class="pun">=</span><span class="kwd">False</span><span class="pun">).</span><span class="pln">mean</span><span class="pun">()</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-6">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Pivot Tables</td>
        <td>Create Pivot tables for better representation of data based on parameters</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">grouped_pivot </span><span class="pun">=</span><span class="pln"> </span></code></li><li class="L1"><code><span class="pln">df_group</span><span class="pun">.</span><span class="pln">pivot</span><span class="pun">(</span><span class="pln">index</span><span class="pun">=</span><span class="str">'attribute_1'</span><span class="pun">,</span><span class="pln">columns</span><span class="pun">=</span><span class="str">'attribute_2'</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-7">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Pseudocolor plot</td>
        <td>Create a heatmap image using a PsuedoColor plot (or pcolor) using the pivot table as data.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="kwd">from</span><span class="pln"> matlplotlib </span><span class="kwd">import</span><span class="pln"> pyplot </span><span class="kwd">as</span><span class="pln"> plt </span></code></li><li class="L1"><code><span class="pln">plt</span><span class="pun">.</span><span class="pln">pcolor</span><span class="pun">(</span><span class="pln">grouped_pivot</span><span class="pun">,</span><span class="pln"> cmap</span><span class="pun">=</span><span class="str">'RdBu'</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-8">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Pearson Coefficient and p-value</td>
        <td>Calculate the Pearson Coefficient and p-value of a pair of attributes</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li><li>3</li></ol><ol class="linenums"><li class="L0"><code><span class="typ">From</span><span class="pln"> scipy </span><span class="kwd">import</span><span class="pln"> stats </span></code></li><li class="L1"><code><span class="pln">pearson_coef</span><span class="pun">,</span><span class="pln">p_value</span><span class="pun">=</span><span class="pln">stats</span><span class="pun">.</span><span class="pln">pearsonr</span><span class="pun">(</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_1'</span><span class="pun">],</span><span class="pln"> </span></code></li><li class="L2"><code><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_2'</span><span class="pun">])</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-9">Copied!</span></button></pre></td>
    </tr>
</tbody></table>