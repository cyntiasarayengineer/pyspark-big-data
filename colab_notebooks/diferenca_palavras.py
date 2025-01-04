# Importar o Spark
from pyspark.sql import SparkSession

# Criar a sessão do Spark
spark = SparkSession.builder.getOrCreate()

# Carregar o arquivo CSV como um DataFrame
df = spark.read.csv('imdb-reviews-pt-br.csv', header=True, quote="\"", escape="\"", encoding="UTF-8")

# Função map para contar as palavras em cada texto
def map_contador_palavras(row):
    sentiment = row[3]
    palavras_en = len(row[1].split())  # Contar o número de palavras em text_en
    palavras_pt = len(row[2].split())  # Contar o número de palavras em text_pt
    return (sentiment, (palavras_en, palavras_pt))

# Função reduceByKey para somar o total de palavras em cada idioma
def reduce_soma_palavras(a, b):
    return (a[0] + b[0], a[1] + b[1])

# Aplicar o map/reduce para contar as palavras
contador_palavras = df.rdd.map(map_contador_palavras).reduceByKey(reduce_soma_palavras).collect()

# Calcular a diferença entre o total de palavras em cada idioma
total_palavras_en = contador_palavras [0][1][0]  # Total de palavras em text_en
total_palavras_pt = contador_palavras [0][1][1]  # Total de palavras em text_pt
# Diferença de palavras com abs para retorna o valor absoluto de um número (não negativo)
dif_palavras_ru3745222 = abs(total_palavras_en - total_palavras_pt)

# Exibir o resultado
print("A soma total de palavras nos textos negativos em Inglês (text_en):", total_palavras_en)
print("A soma total de palavras nos textos negativos em Português (text_pt):", total_palavras_pt)
print("A diferença entre as palavras (text_en - text_pt):", dif_palavras_ru3745222)
