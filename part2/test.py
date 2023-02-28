import pandas as pd
import pyodbc
import logging


logging.basicConfig(filename='output_logs',
                filemode='w',
                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                datefmt='%H:%M:%S',
                level=logging.INFO)

try:


    # Import CSV
    #print('loading data into dataframe from a file')
    logging.info('loading data into dataframe from a file')

    data = pd.read_csv (r'C:\Users\NIKHIL\Desktop\upwork_proj1\part2\load_to_table.csv')   
    df = pd.DataFrame(data)
    logging.info('dataframe created')

    # Connect to SQL Server
    logging.info('creating connection to SQL SERVER')
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-HC7ATDVO;'
                          'Database=master;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    logging.info('connection  created to SQL SERVER')

    # Create Table
    logging.info('truncating target table')

    cursor.execute('''truncate table  products''')
    logging.info('truncated target table')
    i=1
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
        logging.info('%s row inserted'.format(i))
        i=i+1
    logging.info('table loaded successfully')


    conn.commit()

except Exception as inst:

    logging.info(inst)

#for larger tables we can use 
#DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)
