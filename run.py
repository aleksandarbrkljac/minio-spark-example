
from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .appName("Minio S3")
         .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.0")
         .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
         .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
         .config("spark.hadoop.fs.s3a.access.key", "minio-root-user")
         .config("spark.hadoop.fs.s3a.secret.key", "minio-root-password")
         .config("spark.hadoop.fs.s3a.path.style.access", "true")
         .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
         .getOrCreate()
         )

spark.read.text('s3a://testing/test.json').show()
