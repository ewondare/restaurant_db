import streamlit as st
import pandas as pd
import pypyodbc as odbc
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt


Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = 'DESKTOP-2V8SO2H\SQLEXPRESS'

Parinaz_DB = 'db_project'
Nazanin_DB = 'proj'
Dorsa_DB = 'GroupAssignment1'
Taha_DB = 'database_withdata'

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Parinaz_SERVER_NAME
DATABASE_NAME = Parinaz_DB

connection_string = f"DRIVER={{SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trust_Connection=yes;"

# establish connection
conn = odbc.connect(connectString=connection_string)

def fetch_data(operation_name):
    count = 0
    combined_df = None
    for table_name in table_names:
        count += 1
        query = """
                SELECT log_id , [timestamp]
                FROM [{}]
                WHERE operation LIKE '%{}%';""".format(table_name , operation_name)
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            new_df = pd.DataFrame(cursor.fetchall(), columns=columns)
            new_df['Log_table'] = table_name
            if count == 0:
                combined_df = new_df.copy()
            elif count > 0:
                combined_df = pd.concat([combined_df, new_df], ignore_index=True)

        
    return combined_df
        
    
Log_Tables_query = """SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%Log%';"""
cursor = conn.cursor()
cursor.execute(Log_Tables_query)
table_names = list(row[0] for row in cursor.fetchall() )



options = ('INSERT' , 'UPDATE' , 'DELETE')
with st.container():
    st.empty()
    selected_option = st.selectbox("What Kind of Log Data do you want to observe?", options)

    start_date = datetime(2024, 1, 1, 0, 0, 0)
    end_date = datetime.combine(date.today() + timedelta(days=1), datetime.min.time())
    
    selected_date = st.slider(
        "Select a date range",
        min_value=start_date,
        max_value=end_date,
        value=(start_date, end_date),
        step=timedelta(days=1),
    )
    

    df = fetch_data(selected_option[0])
    start_date, end_date = selected_date
    df = df[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)]
    st.write(selected_date)
    st.dataframe(df)

        
    grouped_df = df.groupby(pd.Grouper(key='timestamp', freq='D')).size().reset_index(name='count')
    
    st.bar_chart(grouped_df, x='timestamp', y='count')
    st.write(f"Number of {selected_option} operations within the selected date range")
