import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import importlib.util
import sys
import os
import requests

Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = None

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Nazanin_SERVER_NAME
DATABASE_NAME = 'proj'

# SQLAlchemy
connection_string = f"mssql+pyodbc://{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME.replace(' ', '+')}"

# create SQLAlchemy engine
engine = create_engine(connection_string)

# query to select all data from a table
def query_select(table_name):
    query = f"SELECT * FROM [{table_name}]"
    return query

# fetch data from the database and return a dataframe
def get_data(query):
    return pd.read_sql(query, engine)

options = ("Appetizer_item", "Entree_item", "Desert_item", "Table", "Booking", 
           "Transaction", "Counter", "Makes_order", "Employee", "Customer", 
           "Manager", "Cashier", "Chef", "Waiter", "Receive_order", "Menu")

# table selection UI
selected_option = st.selectbox("Please select the table you want to see the data in.", options)

# fetch and display data from the selected table
if selected_option:
    query = query_select(selected_option)
    data = get_data(query)
    with st.container():
        st.write(f"Data from {selected_option}")
        st.dataframe(data)

# load a module from a given URL
def load_module_from_github(url, module_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{module_name}.py", 'w') as f:
            f.write(response.text)
        spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        os.remove(f"{module_name}.py")
        return module
    else:
        st.error(f"Failed to load module {module_name} from {url}")
        return None

# URLs to the GitHub raw files
delete_url = "https://raw.githubusercontent.com/ewondare/restaurant_db/main/main/pages/delete.py"
update_url = "https://raw.githubusercontent.com/ewondare/restaurant_db/main/main/pages/update.py"
insert_url = "https://raw.githubusercontent.com/ewondare/restaurant_db/main/main/pages/insert.py"

# load the modules
delete = load_module_from_github(delete_url, "delete")
update = load_module_from_github(update_url, "update")
insert = load_module_from_github(insert_url, "insert")

st.write("Perform other operations:")

operation = st.selectbox("Select an operation:", ("Insert", "Update", "Delete"))

if operation == "Insert":
    st.write("Insert operation selected")
    if insert:
        insert.selected_option = st.selectbox("Choose an insert option:", insert.options)
        exec(open("insert.py").read())

elif operation == "Update":
    st.write("Update operation selected")
    if update:
        update.selected_option = st.selectbox("Choose an update option:", update.options)
        exec(open("update.py").read())

elif operation == "Delete":
    st.write("Delete operation selected")
    if delete:
        delete.selected_option = st.selectbox("Choose a delete option:", delete.options)
        exec(open("delete.py").read())
