import streamlit as st

# Título de la aplicación en la web
st.title("🌡️ Conversor de Temperatura de Marvin")
st.write("Convierte grados Celsius y Fahrenheit al instante.")

# Creamos el input numérico en la web (reemplaza al input tradicional)
temperatura = st.number_input("Ingresa la temperatura:", value=0.0)

# Selector de tipo (reemplaza a la pregunta de texto)
tipo = st.selectbox("¿Qué unidad estás ingresando?", ["Celsius (C)", "Fahrenheit (F)"])

# Si el tipo seleccionado empieza con "C" (Celsius)
if tipo.startswith("Celsius"):
    farenheit = (temperatura * 9 / 5) + 32
    # st.metric hace que el número se vea grande y profesional
    st.metric(label="Resultado:", value=f"{farenheit:.2f} °F")
    
    # Tu lógica de estados del agua
    if farenheit <= 32:
        st.info("❄️ AGUA CONGELADA")
    elif farenheit >= 212:
        st.error("🔥 AGUA HIRVIENDO!!")

# Si el tipo seleccionado empieza con "F" (Fahrenheit)
else:
    celsius = (temperatura - 32) * 5 / 9
    st.metric(label="Resultado:", value=f"{celsius:.2f} °C")
    
    # Tu lógica de estados del agua
    if celsius <= 0:
        st.info("❄️ AGUA CONGELADA")
    elif celsius >= 100:
        st.error("🔥 AGUA HIRVIENDO!!")