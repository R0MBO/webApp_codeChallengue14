import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

#COnfiguración básica de la web
st.set_page_config(page_title="CODE FOR EARTH",layout="centered")

# Título principal de la aplicación
st.title("CODE FOR EARTH APP")

# Creo las dos pestañas 
tab1, tab2 = st.tabs(["Primera Pestaña", "Segunda Pestaña"])

#boton de reseteo de opciones
if st.sidebar.button("Resetear mapa y valores"):
    
    #Borrar toda la memoria de lo seleccionado
    st.session_state.clear()
    
    #Recargar el servidor
    st.rerun()

# Primera pestaña
with tab1:
    st.header("PESTAÑA 1")
    st.write("Contenido")

    #ejemplo de dataframe
    datos_zonas = pd.DataFrame({
        'País': ['Spain', 'France', 'Italy', 'Germany', 'Portugal'],
        'Variable 1': [85, 70, 90, 105, 60],
        'Variable 2': [25,10,30,50,20]
    })

    #selector de variable para colorear mapa
    variables = ['Variable 1', 'Variable 2']
    variable_elegida = st.selectbox("¿Qué variable quieres visualizar en el mapa?", variables,key='menu variables', index=None, placeholder='Select variable to visualize: ')

    

    
    #mapa geografico
    if variable_elegida:
        colores_variables= {'Variable 1':'Viridis','Variable 2':'Reds'}
        color_elegido = colores_variables[variable_elegida]
        figura_mapa = px.choropleth(
            datos_zonas,
            locations='País',              # La columna con los nombres de las zonas
            locationmode='country names',  # Le decimos que busque por nombres de países en inglés
            color=variable_elegida,            # La columna que dictará el color
            color_continuous_scale=color_elegido, # El estilo de los colores 
            title='Puntuaciones por País en Europa'
        )
        
        #mostrar en la app el mapa
        st.plotly_chart(figura_mapa,use_container_width=True)
    else:
        st.image("upna_logo.jpg")

    
    # Boton interactivo
    if st.button("Haz clic aquí"):
        st.success("¡FUNCIONA!")

# Segunda pestaña
with tab2:
    st.header("PESTAÑA 2")
    st.write("Contenido 2")
    
    # Entrada de texto con inputs
    input = st.text_input("input")
    if input:
        st.info(f"Has puesto:{input}")
