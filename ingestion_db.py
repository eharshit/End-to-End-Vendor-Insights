import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine

# Logging setup
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Create DB connection
engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''Ingests a DataFrame into the database'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    logging.info(f"Uploaded table: {table_name} | Shape: {df.shape}")

def load_raw_data():
    '''Loads all CSVs in the data folder and ingests them into the DB'''
    start = time.time()
    data_folder = 'data'

    if not os.path.exists(data_folder):
        logging.error(f"Data folder '{data_folder}' not found.")
        return

    for file in os.listdir(data_folder):
        if file.endswith('.csv'):
            try:
                file_path = os.path.join(data_folder, file)
                df = pd.read_csv(file_path)
                table_name = file[:-4]  # Remove '.csv'
                logging.info(f"Ingesting {file} to table '{table_name}'")
                ingest_db(df, table_name, engine)
            except Exception as e:
                logging.error(f"Failed to ingest {file}: {e}")

    end = time.time()
    total_time = (end - start) / 60
    logging.info("-------------Ingestion Complete-------------")
    logging.info(f"Total Time Taken: {total_time:.2f} minutes")

if __name__ == '__main__':
    load_raw_data()
