-Para la elección del modelo se eligió Linear Regression + Feature Importance + Balance, esto debido al criterio del DS, indicando que uno de los modelos con Feature Importance y Balance debia ser escogido. A partir de esto se elige Linear Regression, dado que ambos modelos obtuvieron similares resultados en el classification report, con leves diferencias en el recall. Siendo Linear Regression un modelo mas facil de interpretar, esto permitirá a futuro entender con mayor claridad el impacto de cada Feature en el resultado del entrenamiento del modelo. Considero de mas importancia la capacidad de entender el por qué de los resultados en este caso, con el objetivo de obtener mejores resultados en futuras iteraciones.

-En el Notebook entregado, se cambiaron los inputs de los plots, definiendo los valores de X e Y para poder visualizarlos. Se ejecutó el Notebook completo en el enviroment creado y se analizaron los resultados.

-En la transcripción del código a .py se corrigieron un par de detalles en los def() entregados. Ademas, en los tests realizados se arreglo el path al data.csv y al momento de instanciar el modelo se hizo un model.fit inicial con los datos para el test de predict.



