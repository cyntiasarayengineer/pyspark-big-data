# Importar o Spark
from pyspark.sql import SparkSession

# Criar da sessão do Spark
spark = SparkSession.builder.getOrCreate()

# Carregar o arquivo CSV como um DataFrame
df = spark.read.csv('imdb-reviews-pt-br.csv', header=True, quote="\"", escape="\"", encoding="UTF-8")

# Função map para extrair o valor da coluna sentiment e converter a primeira coluna para inteiro
def map(x):
    return (x[3], int(x[0]))

# Função reduceByKey para somar os IDs
def reduceByKey(x, y):
    return x + y

# Aplicar o map/reduce no DataFrame Spark conforme tutoria
resultado_ru3745222 = df.rdd.map(map).reduceByKey(reduceByKey).collect()

# Exibir o resultado
print("A soma total dos IDs com a coluna 'sentiment' igual a 'neg':", resultado_ru3745222[0][1])
