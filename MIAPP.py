import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import Inicio
import POS
import Inventario
import Reportes
import Clientes

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

        with st.sidebar:
            app = option_menu(
                menu_title="MATERIAL INDUSTRIES",
                options=["Inicio", "POS", "Inventario", "Reportes", "Clientes"],
                icons=['house-fill', 'card-list', 'box-seam-fill', 'bar-chart-fill', "person-fill"],
                menu_icon='chat-text-fill',
                default_index=0,  # Establecer el índice por defecto a "Home"
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
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
multi_app.add_app("Clientes", Clientes.app)
multi_app.add_app("Reportes", Reportes.app)



def new_func(multi_app):
    print("Aplicaciones agregadas:", [app_info["title"] for app_info in multi_app.apps])

    multi_app.run()

new_func(multi_app)
