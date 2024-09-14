import os
import psycopg2
import streamlit as st
from psycopg2 import sql
from contract import Sales
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Postgre database configuration
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Function to save validated data in Postgre
def load_into_postgre(dados: Sales):
    """"
    Function to save in Postgre    
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        # Inserting data into the sales table
        insert_query = sql.SQL(
            "INSERT INTO sales (email, date_time, product_value, product_quantity, product_type) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.date_time,
            dados.product_value,
            dados.product_quantity,
            dados.product_type
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Data successfully saved in Postgre")
    except Exception as e:
        st.error(f"Error saving data in Postgre: {e}")