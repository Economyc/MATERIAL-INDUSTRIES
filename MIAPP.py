import streamlit as st
from streamlit_option_menu import option_menu
import Inicio
import POS
import Inventario
import Reportes

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
                .sidebar .sidebar-content {
                    font-size: 18px; /* Ajustar tamaño del texto */
                }
                .sidebar .css-1l7p5m3 {
                    font-size: 30px; /* Ajustar tamaño del icono */
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
                    "icon": {"color": "white", "font-size": "30px"},  # Aumentar tamaño del ícono
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        for app_info in self.apps:
            if app == app_info["title"]:
                app_info["function"]()

multi_app = MultiApp()
multi_app.add_app("Inicio", Inicio.app)
multi_app.add_app("POS", POS.app)
multi_app.add_app("Inventario", Inventario.app)
multi_app.add_app("Reportes", Reportes.app)

print("Aplicaciones agregadas:", [app_info["title"] for app_info in multi_app.apps])

multi_app.run()

