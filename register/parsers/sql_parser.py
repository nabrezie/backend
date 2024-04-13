import pandas as pd
from pandasql import sqldf

data = pd.read_csv("data.csv")
data = data.set_index("id")

sql_query = "SELECT * FROM data WHERE "
