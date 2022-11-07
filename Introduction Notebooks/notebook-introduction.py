# Databricks notebook source
# MAGIC %scala
# MAGIC val msg = "hello"

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT "Hello" 

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks-datasets/COVID/USAFacts/

# COMMAND ----------

# MAGIC %fs head dbfs:/databricks-datasets/COVID/USAFacts/covid_confirmed_usafacts.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC ps

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

for folder_name in dbutils.fs.ls('/'):
    print(folder_name)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.notebook.run("./child_notebook",10, {"input":"Called from main notebook"})

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------


