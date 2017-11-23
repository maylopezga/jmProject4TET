# jmProject4TET

## Autores
  *Jose David Sánchez Castrillón*              _jsanch81@eafit.edu.co_

  *Mayerli Andrea López Galeano*               _mlopez12@eafit.edu.co_

## Créditos

  En este proyecto se implementó el HashingTF y el IDF el cual podemos encontrar en el siguiente link [github](https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/tf_idf_example.py), además de eso se utilizó el Kmeans que ya estaba implementado en una bilioteca.

## Instalaciones


## Ejecución
  Para la ejecución de este proyecto se tiene dos posibilidades, pero necesariamente se debe de correr en un cluster que cuente con el framework de spark, para poder tener acceso a los datasets del cluster de hadoop. la primera posibilidad de ejecución es correrlo localmente con el siguiente comando.
  ````
  spark-submmit name-archivo.py
  ````
  con este comando el proceso se correrá localmente, pero de igual forma los datos quedaran guardados en el cluster de hadoop, aunque no quedara registro de este en hadoop.
  La otra manera es ejecutar este en el cluster de hadoop, para poder realizar esto es necesario correr el programa con yarn, el comando para esta ejecución es la siguiente.

  ````
  spark-submit --master yarn --deploy-mode cluster --executor-memory 2G --num-executors 4 name-archivo.py
  ````
  con este comando se correrá en el cluster de hadoop, y su registro quedara allí, aunque en este lugar es necesario esperar en ocasiones mucho, ya que en primera parte el programa se pondrá en cola, y luego se ejecutara apenas terminen los que estén corriendo, y los que estén por delante de mí.
## Funcionalidad del código
