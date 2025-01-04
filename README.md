# 📂 Descrição do Projeto
O dataset IMDB é super popular e amplamente utilizado para criar modelos de processamento de linguagem natural e para clusterização (ou seja, agrupar textos) em análises de sentimentos, como identificar se um texto tem uma opinião positiva ou negativa. 
Neste projeto, trabalhei com a versão traduzida para o português desse conjunto de dados (PT-BR). 🇧🇷📚
Vale destacar que não foi realizado processamento de linguagem natural neste trabalho. O objetivo aqui é apenas utilizar o dataset IMDB como exemplo, fazendo coletas simples de informações sobre ele. 

# 📊 Descrição do Conjunto de Dados
O conjunto de dados IMDB PT-BR é uma versão traduzida para o português do famoso dataset IMDB, muito usado para criar classificadores automáticos que determinam se textos são positivos ou negativos. 
Essa tradução está disponível na plataforma Kaggle (https://www.kaggle.com/luisfredgs/imdb-ptbr) de forma livre e gratuita. Esses dados são frequentemente usados em pesquisas científicas nas áreas de Ciência de Dados e Big Data. 

# 🎯 Objetivo do Projeto
Este projeto tem como objetivo responder duas perguntas principais, utilizando ferramentas como Spark ou PySpark para processamento de grandes volumes de dados.

## 🔢 Somatório de IDs

Objetivo: Encontrar a soma de todos os campos "id" dos filmes classificados como negativos no conjunto de dados “imdb-reviews-pt-br.csv”.
Para essa tarefa, utilizei a máquina virtual com PySpark para processar os dados e calcular o valor total da soma dos IDs dos filmes negativos. O processo envolve a filtragem do dataset para identificar as avaliações negativas e, em seguida, somar os valores dos campos "id" relacionados a essas avaliações. 

Abaixo está o código que foi utilizado para realizar essa tarefa e o resultado. 👇


![image](https://github.com/user-attachments/assets/7f93231d-a3f8-4bed-b529-4278ae490fc6)





## 🔤 Diferença do número de palavras

Objetivo: Contar o número de palavras dos textos negativos em português e inglês e calcular a diferença de quantidade entre os dois idiomas.
Nessa etapa, o desafio foi contar todas as palavras presentes nas avaliações negativas (tanto em português quanto em inglês) e determinar quantas palavras a mais existem nos textos em português em comparação com os textos em inglês. Para isso, desenvolvi um script em Python , que foi executado na minha máquina virtual com Spark/PySpark, seguindo o mesmo processo da prática anterior. A filtragem adequada das avaliações negativas é essencial para garantir a precisão dos resultados.

Abaixo está o código que foi utilizado para realizar essa tarefa e o resultado. 👇


![image](https://github.com/user-attachments/assets/8862b805-5808-4ad7-8a76-89748232e2b3)
