import streamlit as st
from PIL import Image
import Inicio
import POS
import Inventario
import Reportes

# Configuración de la página
st.set_page_config(
    page_title="MATERIAL INDUSTRIES",
    page_icon="MI.ico"
)

# Mostrar el título en negrita dentro del contenido de la aplicación
st.markdown("<h1 style='text-align: center; font-weight: bold;'>MATERIAL INDUSTRIES</h1>", unsafe_allow_html=True)

# Definir las opciones del menú
menu_options = ["Inicio", "POS", "Inventario", "Reportes"]
menu_icons = ['house-fill', 'card-list', 'box-seam-fill', 'bar-chart-fill']

# Crear un menú personalizado
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("")  # Espacio vacío para centrar el menú

with col2:
    selected_option = st.selectbox(
        label="",
        options=menu_options,
        format_func=lambda x: f"**{x}**",
        index=0
    )

with col3:
    st.write("")  # Espacio vacío para centrar el menú

# Mostrar el icono asociado al menú seleccionado
st.write(f"**Icono:** {menu_icons[menu_options.index(selected_option)]}")

# Ejecutar la función correspondiente al menú seleccionado
if selected_option == "Inicio":
    Inicio.app()
elif selected_option == "POS":
    POS.app()
elif selected_option == "Inventario":
    Inventario.app()
elif selected_option == "Reportes":
    Reportes.app()
