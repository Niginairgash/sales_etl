import pandas as pd
from sqlalchemy import create_engine

def extract_data(file_path):
    sales_data = pd.read_csv(file_path)
    return sales_data

#Transform 
def transform_data(data):
    data['total_price'] = data['quantity']*data['price']
    data = data.dropna()

    return data

#Load
def load_data_to_db(data, db_connection_string):
    engine =  create_engine(db_connection_string)

    data.to_sql('sales_data', engine, index=False, if_exists='append')