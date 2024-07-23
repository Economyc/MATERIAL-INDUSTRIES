import streamlit as st
import pandas as pd
import requests
import os

# URL del archivo CSV en Google Drive (reemplaza FILE_ID con el ID del archivo)
CSV_URL = 'https://drive.google.com/uc?id=1l8Bp3gHQan2a0X1lVTxoN92REYbN9Lxm'

def descargar_csv(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as f:
        f.write(response.content)
    st.write(f"Archivo descargado como {nombre_archivo}")

def obtener_clientes():
    # Descarga el archivo CSV
    descargar_csv(CSV_URL, 'Clientes.csv')
    # Carga el archivo CSV en un DataFrame de Pandas con el delimitador adecuado
    try:
        return pd.read_csv('Clientes.csv', encoding='utf-8', delimiter=';')  # Cambia el delimitador a punto y coma
    except UnicodeDecodeError:
        return pd.read_csv('Clientes.csv', encoding='ISO-8859-1', delimiter=';')  # Cambia el delimitador a punto y coma
    except pd.errors.ParserError:
        st.error("Error al analizar el archivo CSV. Verifica el formato del archivo.")
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

def agregar_cliente(nombre, cedula, celular, correo, direccion):
    # Carga los clientes existentes
    clientes_df = obtener_clientes()
    # Crea un nuevo DataFrame con el cliente nuevo
    nuevos_datos = pd.DataFrame([[nombre, cedula, celular, correo, direccion]], 
                                columns=["Nombre", "Cedula", "Celular", "Correo", "Dirección"])
    # Añade los nuevos datos al DataFrame existente
    clientes_df = pd.concat([clientes_df, nuevos_datos], ignore_index=True)
    # Guarda el DataFrame actualizado en el archivo CSV
    clientes_df.to_csv('Clientes.csv', index=False, sep=';')  # Guarda el archivo con el delimitador adecuado
    st.write("Datos guardados correctamente en 'Clientes.csv'")

def app_clientes():
    st.title("Formulario de Clientes")

    # Crear formulario
    with st.form(key='cliente_form'):
        nombre = st.text_input("Nombre")
        cedula = st.text_input("Cédula")
        celular = st.text_input("Celular")
        correo = st.text_input("Correo")
        direccion = st.text_input("Dirección")

        submit_button = st.form_submit_button(label="Agregar Cliente")
        
        if submit_button:
            agregar_cliente(nombre, cedula, celular, correo, direccion)
            st.success("Cliente agregado exitosamente!")
    
    # Mostrar la tabla de clientes
    st.subheader("Clientes Registrados")
    clientes_df = obtener_clientes()
    if not clientes_df.empty:
        st.dataframe(clientes_df)

# Asegúrate de que `app_clientes` sea accesible como `app`
app = app_clientes
