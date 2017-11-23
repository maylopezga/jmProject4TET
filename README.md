# jmProject4TET

## Autores
  *Jose David Sánchez Castrillón*              _jsanch81@eafit.edu.co_

  *Mayerli Andrea López Galeano*               _mlopez12@eafit.edu.co_

## Créditos

  En este proyecto se implementó el HashingTF y el IDF el cual podemos encontrar en el siguiente link [github](https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/tf_idf_example.py), además de eso se utilizó el Kmeans que ya estaba implementado en una bilioteca.

## Instalaciones

Para este proyecto no se realizaron instalaciones debido a que el entorno en que estábamos trabajando ya contaba con todo instalado. Sin embargo, para ejecutar el proyecto es necesario contar con el Framework de spark.

En el siguiente link se puede encontrar los pasos a seguir para la instalación de spark. [install](https://gist.github.com/darcyliu/d47edccb923b0f03280a4cf8b66227c1)



## Ejecución
  Para la ejecución de este proyecto se tiene dos posibilidades, pero necesariamente se debe de correr en un cluster que cuente con el framework de spark, para poder tener acceso a los datasets del cluster de hadoop. la primera posibilidad de ejecución es correrlo localmente con el siguiente comando.
  ````
  spark-submit name-archivo.py
  ````
  con este comando el proceso se correrá localmente, pero de igual forma los datos quedaran guardados en el cluster de hadoop, aunque no quedara registro de este en hadoop.
  La otra manera es ejecutar este en el cluster de hadoop, para poder realizar esto es necesario correr el programa con yarn, el comando para esta ejecución es la siguiente.

  ````
  spark-submit --master yarn --deploy-mode cluster --executor-memory 2G --num-executors 4 name-archivo.py
  ````
  con este comando se correrá en el cluster de hadoop, y su registro quedara allí, aunque en este lugar es necesario esperar en ocasiones mucho, ya que en primera parte el programa se pondrá en cola, y luego se ejecutara apenas terminen los que estén corriendo, y los que estén por delante de mí.


## Funcionalidad del código

La principal funcionalidad de este código consiste en minería de textos, lo cual es relacionar un documento con otros que sean parecidos, o hablen del mismo tema, esto se está haciendo con una métrica de similaridad, para la cual fue necesaria la implementación de algoritmos como HashingTF e IDF los cuales me devuelven una matriz donde se encuentran las distancias que hay entre los documentos. Dichos algoritmos trabajan de la siguiente manera:

![IDF](/idf.png)

![TF](/tfidf.png)

Donde t con las palabras que contienen los documentos y d con los documentos.

Después de obtener la matriz se necesita un algoritmo de agrupamiento para lo cual se utiliza el kmeans que proviene de una biblioteca de Python, este algoritmo nos devolverá un objeto de tipo KMeansModel. A este objeto es necesario aplicarle un método llamado predict, el cual nos devolverá un arreglo donde se encuentran divididos los clúster, con los cuales ya se podrían hacer recomendaciones de documentos que tiendan a hablar del mismo tema.
