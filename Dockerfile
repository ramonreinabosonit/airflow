FROM apache/airflow:2.7.3

USER root

# Instalar Java y wget
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Descargar Spark
RUN wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.1-bin-hadoop3.tgz -C /opt && \
    mv /opt/spark-3.5.1-bin-hadoop3 /opt/spark && \
    rm spark-3.5.1-bin-hadoop3.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH="${PATH}:${SPARK_HOME}/bin"

USER airflow

# Instalar provider de Spark
# RUN pip install apache-airflow-providers-apache-spark
RUN pip install \
    --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt \
    apache-airflow-providers-apache-spark