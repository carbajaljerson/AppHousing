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
    area_constr = render_input('Número de area_constr')
    area_total = render_input('Número de area_total')

    chimenea = render_checkbox('Chimenea')
    jacuzzi = render_checkbox('Jacuzzi')
    aire_acondicionado = render_checkbox('Aire Acondicionado')
    area_deportiva = render_checkbox('Area Deportiva')
    hall_ingreso = render_checkbox('Hall Ingreso')
    areas_verdes = render_checkbox('Áreas Verdes')
    desague = render_checkbox('Desague')
    piscina = render_checkbox('Piscina')
    sauna = render_checkbox('Sauna')
    area_bbq = render_checkbox('Área Bbq')

    # Mapear valores booleanos a 0 o 1
    valores_checkbox = {
        'chimenea': chimenea, 'jacuzzi': jacuzzi,
        'aire_acondicionado': aire_acondicionado,
        'area_deportiva': area_deportiva, 'hall_ingreso': hall_ingreso,
        'areas_verdes': areas_verdes, 'desague': desague,
        'piscina': piscina, 'sauna': sauna, 'area_bbq': area_bbq
    }

    valores_numericos = [baños, cocheras, dormitorios, area_constr, area_total]
    valores_numericos.extend([1 if valor else 0 for valor in valores_checkbox.values()])
    
    
    print('valores_numericos',valores_numericos)

    prediction = ''
        
    if st.button('Resultado'):
        prediction = np.round(model.predict([valores_numericos]), 2)[0] 

    # Comprobar si prediction es un valor válido
    if prediction is not None:
        try:
            # Formatear el resultado con formato de miles y símbolo de moneda
            formatted_prediction = "${:,.2f}".format(float(prediction))

            # Imprimir el resultado formateado
            st.success(formatted_prediction)
        except ValueError:
            st.error("")
    else:
        st.error("El valor de predicción es None o inválido.")

       

if __name__ == '__main__':
    main()
#streamlit run app.py