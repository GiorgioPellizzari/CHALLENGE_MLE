-Para la elección del modelo se eligió Linear Regression + Feature Importance + Balance, esto debido al criterio del DS, indicando que uno de los modelos con Feature Importance y Balance debia ser escogido. A partir de esto se elige Linear Regression, dado que ambos modelos obtuvieron similares resultados en el classification report, con leves diferencias en el recall. Siendo Linear Regression un modelo mas facil de interpretar, esto permitirá a futuro entender con mayor claridad el impacto de cada Feature en el resultado del entrenamiento del modelo. Considero de mas importancia la capacidad de entender el por qué de los resultados en este caso, con el objetivo de obtener mejores resultados en futuras iteraciones.

-En el Notebook entregado, se cambiaron los inputs de los plots, definiendo los valores de X e Y para poder visualizarlos. Se ejecutó el Notebook completo en el enviroment creado y se analizaron los resultados.

-En la transcripción del código a .py se corrigieron un par de detalles en los def() entregados. Ademas, en los tests realizados se arreglo el path al data.csv y al momento de instanciar el modelo se hizo un model.fit inicial con los datos para el test de predict.

-Desarrollando la API, se modificaron nuevamente los requirements que estaban generando conflicto en el enviroment, se definio la API para esperar una predicción a la vez. Asi cumplir con los test, pero me genera la duda si este es el caso general que se espera. De no serlo bastaria iterar en los vuelos en vez de solo revisar el primero...

-Para el deployment se utilizó Google Cloud Run, se probaron varios metodos para el deploy. Finalmente se decidio por usar una imagen desde docker.io y tratar de hacer deploy con ella en Google.

-Se tiene el error: The user-provided container failed to start and listen on the port defined provided by the PORT=5200 environment variable. Logs for this revision might contain more information. 

-Se probo localmente el dockerfile y funcionó correctamente, asumo que alguna configuración habra faltado. Dado esto se deja link vacio a la api.