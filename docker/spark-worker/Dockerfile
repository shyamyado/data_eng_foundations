FROM apache/spark:3.5.3-scala2.12-java17-python3-ubuntu

ENV SPARK_WORKER_WEBUI_PORT=8081

EXPOSE 8081

CMD ["/opt/spark/bin/spark-class", "org.apache.spark.deploy.worker.Worker", "spark://spark-master:7077"]