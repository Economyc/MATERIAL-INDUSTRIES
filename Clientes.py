import streamlit as st
import gdown
import pandas as pd

# Enlace del archivo CSV en Google Drive (reemplaza FILE_ID con el ID del archivo)
CSV_URL = 'https://drive.google.com/file/d/1rNdq54U7ru8TCG056CEvr-4OvjqlvQLk/view?usp=drive_link'

def obtener_clientes():
    # Descarga el archivo CSV
    gdown.download(CSV_URL, 'clientes.csv', quiet=False)
    # Carga el archivo CSV en un DataFrame de Pandas
    return pd.read_csv('clientes.csv')

def agregar_cliente(nombre, cedula, celular, correo, direccion):
    # Carga los clientes existentes
    clientes_df = obtener_clientes()
    # Crea un nuevo DataFrame con el cliente nuevo
    nuevos_datos = pd.DataFrame([[nombre, cedula, celular, correo, direccion]], 
                                columns=["Nombre", "Cedula", "Celular", "Correo", "Dirección"])
    # Añade los nuevos datos al DataFrame existente
    clientes_df = pd.concat([clientes_df, nuevos_datos], ignore_index=True)
    # Guarda el DataFrame actualizado en el archivo CSV
    clientes_df.to_csv('clientes.csv', index=False)

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
    st.dataframe(clientes_df)
