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
    acasi = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/11*.txt")
    name = acasi.keys().collect()
    documents_values = acasi.values().map(lambda line: line.split(" "))

    hashingTF = HashingTF()
    tf = hashingTF.transform(documents_values)

    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)

    clusters_model = KMeans.train(tfidf, k, maxIterations=10)
    clusters = clusters_model.predict(tfidf).collect()
    for i in range(k):
        group.insert(i,[])
        cont = 0
    for i in clusters:
        group[i].append(name[cont][name[cont].rfind('/')+1:])
        cont += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(name)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("++++++++++++++++++++++++++++++")
    print(group)
    print("++++++++++++++++++++++++++++++")
    print("clusters:")
    print(clusters)
    s = sc.parallelize(group)
    s.saveAsTextFile("hdfs:///user/mlopez12/prueba2")
    sc.stop()
    
