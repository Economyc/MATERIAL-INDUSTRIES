import streamlit as st
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
        # Mostrar el título en negrita en el área principal
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>MATERIAL INDUSTRIES</h1>", unsafe_allow_html=True)

        # Crear el menú lateral personalizado
        selected_option = st.sidebar.selectbox(
            label="Selecciona una opción",
            options=["Inicio", "POS", "Inventario", "Reportes"],
            format_func=lambda x: f"**{x}**"
        )

        # Ejecutar la función correspondiente al menú seleccionado
        for app_info in self.apps:
            if selected_option == app_info["title"]:
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
