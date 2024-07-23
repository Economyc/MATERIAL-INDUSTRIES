import streamlit as st
from streamlit_option_menu import option_menu
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

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function): 
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Añadir imagen
        # Puedes usar st.image para mostrar una imagen si es necesario
        # Ejemplo: st.image("ruta/a/tu/imagen.png")

        with st.sidebar:
            st.markdown("""
                <style>
                /* Cambiar el tamaño y el estilo del botón de despliegue */
                .css-1d391kg {
                    font-size: 30px; /* Tamaño del icono */
                }
                .css-1d391kg svg {
                    width: 30px; /* Ajustar el ancho del ícono */
                    height: 30px; /* Ajustar la altura del ícono */
                }
                </style>
                """, unsafe_allow_html=True)

            app = option_menu(
                menu_title="MATERIAL INDUSTRIES",
                options=["Inicio", "POS", "Inventario", "Reportes"],
                icons=['house-fill', 'card-list', 'box-seam-fill', 'bar-chart-fill'],
                menu_icon='chat-text-fill',
                default_index=0,  # Establecer el índice por defecto a "Inicio"
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        # Ejecutar la función correspondiente al menú seleccionado
        for app_info in self.apps:
            if app == app_info["title"]:
                app_info["function"]()

# Crear y añadir aplicaciones al MultiApp
multi_app = MultiApp()
multi_app.add_app("Inicio", Inicio.app)
multi_app.add_app("POS", POS.app)
multi_app.add_app("Inventario", Inventario.app)
multi_app.add_app("Reportes", Reportes.app)

# Imprimir aplicaciones agregadas (solo para depuración)
print("Aplicaciones agregadas:", [app_info["title"] for app_info in multi_app.apps])

# Ejecutar el MultiApp
multi_app.run()
