<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" />
</p>

# Introducción a la Regresión Ridge  
Para modelos con múltiples características independientes y aquellos con extrapolación de características polinomiales, es común tener combinaciones colineales de características. Si no se controla, esta multicolinealidad de características puede llevar al modelo a sobreajustar los datos de entrenamiento. Para controlar esto, los conjuntos de características suelen regularizarse utilizando hiperparámetros.

La regresión Ridge es el proceso de regularización del conjunto de características utilizando el hiperparámetro alpha. El video que sigue muestra cómo la regresión Ridge puede ser utilizada para regularizar y reducir los errores estándar, evitando el sobreajuste al utilizar un modelo de regresión.

# Resumen:
Enhorabuena Ha completado esta lección. En este punto del curso, ya sabe

Cómo dividir sus datos utilizando el método train_test_split() en conjuntos de entrenamiento y de prueba. Cómo utilizar el conjunto de entrenamiento para entrenar un modelo, descubrir posibles relaciones predictivas y, a continuación, utilizar el conjunto de prueba para probar su modelo y evaluar su rendimiento.

Cómo utilizar el error de generalización para medir lo bien que lo hacen sus datos a la hora de predecir datos no vistos previamente.

Cómo utilizar la validación cruzada dividiendo los datos en pliegues en los que utiliza algunos de los pliegues como conjunto de entrenamiento, que utilizamos para entrenar el modelo, y las partes restantes se utilizan como conjunto de prueba, que utilizamos para probar el modelo. Se itera a través de los pliegues hasta que se utiliza cada partición para el entrenamiento y la prueba. Al final, promedia los resultados como estimación del error fuera de muestra.

Cómo elegir el mejor orden polinómico y problemas que surgen al seleccionar el orden polinómico incorrecto analizando los modelos que se ajustan por defecto y por exceso a sus datos.

Seleccione el mejor orden de un polinomio para ajustar sus datos minimizando el error de prueba mediante un gráfico que compare el error cuadrático medio con el orden de los polinomios ajustados.

Debe utilizar la regresión ridge cuando exista una fuerte relación entre las variables independientes.

La regresión ridge evita el sobreajuste.

La regresión ridge controla la magnitud de los coeficientes polinómicos introduciendo un hiperparámetro, alfa.

Para determinar alfa, se dividen los datos en datos de entrenamiento y datos de validación. Empezando con un valor pequeño para alfa, entrena el modelo, hace una predicción utilizando los datos de validación, luego calcula el R-cuadrado y guarda los valores. Repite el proceso para un valor mayor de alfa. Repite el proceso para diferentes valores de alfa, entrena el modelo y realiza una predicción. Usted selecciona el valor de alfa que maximiza R-cuadrado.

Esa búsqueda de cuadrícula le permite explorar múltiples hiperparámetros utilizando la biblioteca Scikit-learn, que itera sobre estos parámetros utilizando la validación cruzada. Basándose en los resultados del método de búsqueda en cuadrícula, selecciona los valores óptimos de los hiperparámetros.

El método GridSearchCV() toma como argumento un diccionario en el que la clave es el nombre del hiperparámetro y los valores son los valores de hiperparámetro sobre los que desea iterar.

