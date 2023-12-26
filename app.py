import streamlit as st
import pickle
import numpy as np

# Cargar el modelo una sola vez al inicio de la aplicación
with open("modelo/modelo.pkl", "rb") as file:
    model = pickle.load(file)
    
# Leer el contenido del archivo de estilo
with open("theme/template.css", "r") as file:
    theme = file.read()

# Aplicar el tema
st.markdown(f"<style>{theme}</style>", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def check_button_state(valores_numericos):
    return all(valor == 0 for valor in valores_numericos)

def render_input(data):
    return st.number_input(data)

def render_input_entero(data, step=1.0, format="%f"):
    return st.number_input(data, step=step, format=format)

def render_checkbox(data):
    return st.checkbox(data)

def main():
    st.title('Predicción de precio de Viviendas en Lima')

    baños = render_input_entero('Número de Baños')
    cocheras = render_input_entero('Número de cocheras')
    dormitorios = render_input_entero('Número de dormitorios')
    area_total = render_input('Área total (m2)')

    chimenea = render_checkbox('Chimenea')
    jacuzzi = render_checkbox('Jacuzzi')
    aire_acondicionado = render_checkbox('Aire Acondicionado')
    hall_ingreso = render_checkbox('Hall Ingreso')
    piscina = render_checkbox('Piscina')
    sauna = render_checkbox('Sauna')
    
    
   

    # Mapear valores booleanos a 0 o 1
    valores_checkbox = {
        'chimenea': chimenea, 'jacuzzi': jacuzzi,
        'aire_acondicionado': aire_acondicionado,
        'hall_ingreso': hall_ingreso,
        'piscina': piscina, 'sauna': sauna
    }

    valores_numericos = [baños, cocheras, dormitorios, area_total]
    valores_numericos.extend([1 if valor else 0 for valor in valores_checkbox.values()])
    
    
    print('valores_numericos',valores_numericos)

    
    # Verificar el estado del botón dinámicamente
    enable_button = check_button_state(valores_numericos)        
        
    if st.button('Resultado' , key="boton_resultado", disabled=enable_button):
        
        prediction = np.NaN
    
        if not enable_button:
            
            prediction = np.round(model.predict([valores_numericos]), 2)[0] 
            
            # Formatear el resultado con formato de miles y símbolo de moneda
            formatted_prediction = "S/.{:,.2f}".format(float(prediction))

            # Imprimir el resultado formateado
            st.success(formatted_prediction)


if __name__ == '__main__':
    main()
#streamlit run app.py