import pandas as pd
import sqlite3

record = pd.read_csv('C:/Users/mewtw/project03_2/record.csv', encoding='utf-8')
# sqlite 연결 
con = sqlite3.connect("record.db")
query = con.execute("SELECT * FROM record")
cols = [column[0] for column in query.description]
record_df = pd.DataFrame.from_records(data = query.fetchall(), columns=cols)
record_df.to_csv('record_df.csv', index=False)
# record.to_sql("record", con, if_exists='append', index=False)

#record_df = pd.read_sql_query("SELECT * FROM record", con)
print(record_df)
con.commit()