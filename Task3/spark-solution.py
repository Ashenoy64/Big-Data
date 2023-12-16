#!/usr/bin/env python3
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, asc,desc

spark = SparkSession.builder.appName("cases").getOrCreate()

input_paths =  sys.argv[1:-1]
output_path = sys.argv[-1]




#Reading the csv file
df_2012 = spark.read.csv(input_paths[0],header=True,inferSchema= True).select('ddl_case_id','year','state_code')
df_2013 = spark.read.csv(input_paths[1],header=True,inferSchema= True).select('ddl_case_id','year','state_code')
df_2014 = spark.read.csv(input_paths[2],header=True,inferSchema= True).select('ddl_case_id','year','state_code')
df_state_key = spark.read.csv(input_paths[3],header=True,inferSchema= True)

cases_union = df_2012.union(df_2013)
cases_union = cases_union.union(df_2014)

task_1_1_data = cases_union.join(df_state_key,[df_state_key.state_code == cases_union.state_code,df_state_key.year == cases_union.year]).select('state_name').groupBy(['state_name']).count().orderBy(col('count').desc()).take(10)

top_10 = [i[0] for i in task_1_1_data]






#Task 1.2

df_judges_clean = spark.read.csv(input_paths[4],header=True,inferSchema= True)
df_case_merge_key =spark.read.csv(input_paths[5],header=True,inferSchema= True)
df_acts_section = spark.read.csv(input_paths[6],header=True,inferSchema= True)

cases_ids = df_acts_section.join(cases_union,[cases_union.ddl_case_id==df_acts_section.ddl_case_id,df_acts_section.criminal==1]).select(df_acts_section.ddl_case_id)

judges=cases_ids.join(df_case_merge_key,[cases_ids.ddl_case_id==df_case_merge_key.ddl_case_id,df_case_merge_key.ddl_decision_judge_id.isNotNull()]).select(df_case_merge_key.ddl_decision_judge_id).groupBy(['ddl_decision_judge_id']).count().orderBy(col('count').desc()).take(1)

top_judge = int(judges[0][0])


task_1_ans = (top_10,top_judge)
file  = open(output_path,'w+')

file.write(str(task_1_ans))

file.close()

