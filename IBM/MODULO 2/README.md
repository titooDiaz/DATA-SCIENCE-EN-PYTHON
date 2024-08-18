<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" />
</p>

# Aprendemos:

El formateo de datos es fundamental para que los datos procedentes de diversas fuentes sean coherentes y comparables.

Dominar las técnicas en Python para convertir unidades de medida, como transformar "millas urbanas por galón" a "litros urbanos por cada 100 kilómetros" para facilitar la comparación y el análisis.

Adquiera habilidades para identificar y corregir los tipos de datos en Python, asegurándose de que los datos se representan con precisión para los análisis estadísticos posteriores.

La normalización de datos ayuda a que las variables sean comparables y a eliminar los sesgos inherentes a los modelos estadísticos.

Puede aplicar Feature Scaling, Min-Max y Z-Score para normalizar los datos y aplicar cada técnica en Python utilizando los métodos de pandas.

El binning es un método de preprocesamiento de datos para mejorar la precisión del modelo y la visualización de los datos.

Ejecute técnicas de binning en Python utilizando los métodos "linspace" de numpy y "cut" de pandas, en particular para variables numéricas como "price"

Utilice los histogramas para visualizar la distribución de los datos bindeados y obtener información sobre las distribuciones de las características.

Los modelos estadísticos suelen requerir entradas numéricas, por lo que es necesario convertir variables categóricas como "tipo de combustible" en formatos numéricos.

Puede implementar la técnica de codificación one-hot en Python utilizando el método get_dummies de pandas para transformar las variables categóricas en un formato adecuado para los modelos de aprendizaje automático.

# Comandos:

<table width="100%">
<tbody><tr>
<th width="20%">Package/Method </th><th width="50%">Description </th><th width="30%">Code Example</th>
</tr>
    <tr>
        <td>Replace missing data with frequency</td>
        <td>Replace the missing values of the data set attribute with the mode common occurring entry in the column. </td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="typ">MostFrequentEntry</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">].</span><span class="pln">value_counts</span><span class="pun">().</span><span class="pln">idxmax</span><span class="pun">()</span><span class="pln"> </span></code></li><li class="L1"><code><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">].</span><span class="pln">replace</span><span class="pun">(</span><span class="pln">np</span><span class="pun">.</span><span class="pln">nan</span><span class="pun">,</span><span class="typ">MostFrequentEntry</span><span class="pun">,&gt;</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">].</span><span class="pln">replace</span><span class="pun">(</span><span class="pln">np</span><span class="pun">.</span><span class="pln">nan</span><span class="pun">,</span><span class="typ">MostFrequentEntry</span><span class="pun">,</span><span class="pln"> inplace</span><span class="pun">=</span><span class="kwd">True</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-0">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Replace missing data with mean</td>
        <td>Replace the missing values of the data set attribute with the mean of all the entries in the column. </td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="typ">AverageValue</span><span class="pun">=</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">].</span><span class="pln">astype</span><span class="pun">(&lt;</span><span class="pln">data_type</span><span class="pun">&gt;).</span><span class="pln">mean</span><span class="pun">(</span><span class="pln">axis</span><span class="pun">=</span><span class="lit">0</span><span class="pun">)</span></code></li><li class="L1"><code><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">].</span><span class="pln">replace</span><span class="pun">(</span><span class="pln">np</span><span class="pun">.</span><span class="pln">nan</span><span class="pun">,</span><span class="pln"> </span><span class="typ">AverageValue</span><span class="pun">,</span><span class="pln"> inplace</span><span class="pun">=</span><span class="kwd">True</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-1">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Fix the data types</td>
        <td>Fix the data types of the columns in the dataframe.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li><li>3</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">[[</span><span class="str">'attribute1_name'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'attribute2_name'</span><span class="pun">,</span><span class="pln"> </span><span class="pun">...]]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span></code></li><li class="L1"><code><span class="pln">df</span><span class="pun">[[</span><span class="str">'attribute1_name'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'attribute2_name'</span><span class="pun">,</span><span class="pln"> </span><span class="pun">...]].</span><span class="pln">astype</span><span class="pun">(</span><span class="str">'data_type'</span><span class="pun">)</span></code></li><li class="L2"><code><span class="com">#data_type is int, float, char, etc. </span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-2">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Data Normalization</td>
        <td>Normalize the data in a column such that the values are restricted between 0 and 1.</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><br><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">]/</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">].</span><span class="pln">max</span><span class="pun">()</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-3">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Binning</td>
        <td>Create bins of data for better analysis and visualization.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">bins </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">linspace</span><span class="pun">(</span><span class="pln">min</span><span class="pun">(</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">]),</span><span class="pln"> </span></code></li><li class="L1"><code><span class="pln">max</span><span class="pun">(</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">],</span><span class="pln">n</span><span class="pun">)</span></code></li><li class="L2"><code><span class="com"># n is the number of bins needed </span></code></li><li class="L3"><code><span class="typ">GroupNames</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'Group1'</span><span class="pun">,</span><span class="str">'Group2'</span><span class="pun">,</span><span class="str">'Group3,...]</span></code></li><li class="L4"><code><span class="str">df['</span><span class="pln">binned_attribute_name</span><span class="str">'] = </span></code></li><li class="L5"><code><span class="str">pd.cut(df['</span><span class="pln">attribute_name</span><span class="str">'], bins, labels=GroupNames, include_lowest=True)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-4">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Change column name</td>
        <td>Change the label name of a dataframe column.</td>
        <td><pre class="prettyprint linenums prettyprinted" style="padding-right: 42px;"><ol class="formatted-line-numbers"><li>1</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">df</span><span class="pun">.</span><span class="pln">rename</span><span class="pun">(</span><span class="pln">columns</span><span class="pun">={</span><span class="str">'old_name'</span><span class="pun">:</span><span class="pln">\'new_name</span><span class="str">'}, inplace=True)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block one-line"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-5">Copied!</span></button></pre></td>
    </tr>
    <tr>
        <td>Indicator Variables</td>
        <td>Create indicator variables for categorical data.</td>
        <td><pre class="prettyprint linenums prettyprinted" style=""><ol class="formatted-line-numbers"><li>1</li><li>2</li></ol><ol class="linenums"><li class="L0"><code><span class="pln">dummy_variable </span><span class="pun">=</span><span class="pln"> pd</span><span class="pun">.</span><span class="pln">get_dummies</span><span class="pun">(</span><span class="pln">df</span><span class="pun">[</span><span class="str">'attribute_name'</span><span class="pun">])</span></code></li><li class="L1"><code><span class="pln">df </span><span class="pun">=</span><span class="pln"> pd</span><span class="pun">.</span><span class="pln">concat</span><span class="pun">([</span><span class="pln">df</span><span class="pun">,</span><span class="pln"> dummy_variable</span><span class="pun">],</span><span class="pln">axis </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">)</span></code></li></ol><button title="Copy" class="action-code-block copy-code-block multiple-lines"><i class="fa fa-copy" aria-hidden="true"></i><span class="popuptext" id="md-code-block-copy-6">Copied!</span></button></pre></td>
    </tr>
</tbody></table>