<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" />
</p>

# Desarrollo de Modelos de prediccion

La regresión lineal se refiere al uso de una variable independiente para hacer una predicción.

Puede utilizar la regresión lineal múltiple para explicar la relación entre una variable objetivo continua y y dos o más variables predictoras x.

La regresión lineal simple, o SLR, es un método utilizado para comprender la relación entre dos variables, la variable independiente predictora x y la variable dependiente objetivo y.

Utilice las funciones regplot y residplot de la biblioteca Seaborn para crear gráficos de regresión y residuales, que le ayudarán a identificar la fuerza, dirección y linealidad de la relación entre sus variables independiente y dependiente.

Cuando utilice gráficos de residuos para la evaluación del modelo, lo ideal es que los residuos tengan media cero, aparezcan distribuidos uniformemente alrededor del eje x y tengan una varianza consistente. Si no se cumplen estas condiciones, considere la posibilidad de ajustar su modelo.

Utilice gráficos de distribución para modelos con múltiples características: Aprenda a construir gráficos de distribución para comparar los valores previstos y los reales, sobre todo cuando su modelo incluya más de una variable independiente. Sepa que esto puede ofrecerle una visión más profunda de la precisión de su modelo en diferentes rangos de valores.

El orden de los polinomios afecta al ajuste del modelo a sus datos. Aplique la función polyfit de Python para desarrollar modelos de regresión polinómica que se adapten a su conjunto de datos específico.

Para preparar sus datos para un modelado más preciso, utilice técnicas de transformación de características, en particular utilizando la biblioteca de preprocesamiento en scikit-learn, transforme sus datos utilizando características polinómicas y utilice los módulos como StandardScaler para normalizar los datos.

Las canalizaciones le permiten simplificar la forma de realizar transformaciones y predicciones secuencialmente, y puede utilizar canalizaciones en scikit-learn para agilizar su proceso de modelado.

Puede construir y entrenar una canalización para automatizar tareas como la normalización, la transformación polinómica y la realización de predicciones.

Para determinar el ajuste de su modelo, puede realizar evaluaciones de muestras mediante el error cuadrático medio (MSE), utilizando la función mean_squared_error de Python de scikit-learn, y utilizando el método de puntuación para obtener el valor R-cuadrado.

Un modelo con un alto valor R-cuadrado cercano a 1 y un MSE bajo suele ser un buen ajuste, mientras que un modelo con un R-cuadrado bajo y un MSE alto puede no ser útil.

Esté alerta ante situaciones en las que su valor R-cuadrado pueda ser negativo, lo que puede indicar un ajuste excesivo.

Al evaluar los modelos, utilice medidas de visualización y numéricas y compare diferentes modelos.

El error cuadrático medio es quizá la medida numérica más intuitiva para determinar si un modelo es bueno.

Un gráfico de distribución es un método adecuado para la regresión lineal múltiple.

Un valor r-cuadrado aceptable depende de lo que esté estudiando y de su caso de uso.

Para evaluar el ajuste de su modelo, aplique la visualización, métodos como los gráficos de regresión y residuales, y medidas numéricas como los coeficientes del modelo para la sensibilidad:

Utilice el error cuadrático medio (ECM) para medir la media de los cuadrados de los errores entre los valores reales y los predichos y examine la R al cuadrado para comprender la proporción de la varianza en la variable dependiente que es predecible a partir de las variables independientes.

Al analizar los trazados residuales, los residuos deben distribuirse aleatoriamente en torno a cero para un buen modelo. Por el contrario, una curva de parcela residual o imprecisiones en ciertos rangos sugieren un comportamiento no lineal o la necesidad de más datos.