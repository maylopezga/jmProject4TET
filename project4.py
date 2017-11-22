from __future__ import print_function
# tf-idf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.mllib.feature import HashingTF, IDF
# KMeans
from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans, KMeansModel

if __name__ == "__main__":
    k = 3
    group = []
    sc = SparkContext(appName="May_Jose") # SparkContext
    '''
    Se encarga de traer en un diccionario todos los documentos con sus respectivos textos.
    '''
    acasi = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/*.txt")

    '''
    Sacamos los nombres de los documentos para mostrarlos en el momento que se realizao la
    agrupacion.
    '''
    name = acasi.keys().collect()

    '''
    se realiza la divicion de cada texto de cada documento por un espacio, para obtener las palabras de todos los documentos, y
    saber su frecuencia en cada documento.
    '''
    documents_values = acasi.values().map(lambda line: line.split(" "))

    '''
    En esta parte se esta realizando la comparacion de cada documento, para obtener las distancias
    Entre el uno y el otro, al final estos metodos me generan una matriz, la cual sera analizada por KMeans
    para asignar a cada documento en un cluster diferente.
    '''
    hashingTF = HashingTF()
    tf = hashingTF.transform(documents_values)
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)

    '''
    En esta area se le pasa la matriz obtenida por los metodos de agrupamiento, los cuales se encargan de asignar a
    cada documento en su respectivo cluster, dependiendo de la cercania de un documento con el otro.
    '''
    clusters_model = KMeans.train(tfidf, k, maxIterations=10)
    clusters = clusters_model.predict(tfidf).collect()
    for i in range(k):
        group.insert(i,[])
        cont = 0
    for i in clusters:
        group[i].append(name[cont][name[cont].rfind('/')+1:])
        cont += 1
    s = sc.parallelize(group)
    s.saveAsTextFile("hdfs:///user/mlopez12/prueba2")
    sc.stop()
