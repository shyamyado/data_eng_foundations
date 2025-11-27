FROM apache/spark:3.5.3-scala2.12-java17-python3-ubuntu

ENV SPARK_MASTER_HOST=spark-master
ENV SPARK_MASTER_PORT=7077
ENV SPARK_MASTER_WEBUI_PORT=8080
ENV PATH="/opt/spark/bin:${PATH}"   

EXPOSE 8080 7077

CMD ["/opt/spark/bin/spark-class", "org.apache.spark.deploy.master.Master"]
