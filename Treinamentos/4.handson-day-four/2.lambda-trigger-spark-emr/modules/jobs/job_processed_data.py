from pyspark.sql.functions import isnan, when, count, col, from_unixtime, to_timestamp, to_date, udf
from pyspark.sql.types import DateType
from datetime import datetime
from os.path import join

def convert_timestamp_to_datetime(timestamp):
    return str(datetime.fromtimestamp(int(timestamp)))

def process(spark, input_path, output_path, save_mode='append'):
    
    path_movies = join(input_path, 'data', 'movies.csv')
    path_ratings = join(input_path, 'data', 'ratings.csv')
    path_outputs = join(output_path, 'outputs')
    
    df_movies = spark.read.format("csv").option("header", "true").load(path_movies)
    df_ratings = spark.read.format("csv").option("header", "true").load(path_ratings)
            
    df_final = df_movies.join(df_ratings, df_movies.movieId == df_ratings.movieId).select(df_movies.movieId, 'title', 'genres', 'userId', 'rating', 'timestamp')

    udf_convert_timestamp_to_datetime = udf(convert_timestamp_to_datetime)
    
    df_final = df_final.withColumn('date', udf_convert_timestamp_to_datetime(col('timestamp')))

    df_final = df_final.drop('timestamp')

    df_final.write.mode(save_mode).parquet(path_outputs)


