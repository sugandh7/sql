import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'C:\Users\NIKHIL\Desktop\upwork_proj1\part2\load_to_table.csv')   
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HC7ATDVO;'
                      'Database=master;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''truncate table  products''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO products (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )
conn.commit()

#for larger tables we can use 
#DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)