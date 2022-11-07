# Databricks notebook source
print("I am the child notebook")

# COMMAND ----------

dbutils.notebook.exit(100)

# COMMAND ----------

dbutils.widgets.text("input","","Send the parameter value")

# COMMAND ----------

input_param = dbutils.widgets.get("input")

# COMMAND ----------

print(input_param)

# COMMAND ----------


