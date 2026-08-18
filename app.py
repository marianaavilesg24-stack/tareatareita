import streamlit as st

st.set_page_config(page_title="Calculadora de Huella de Carbono", page_icon="🌱")

st.title("🌱 Calculadora de Huella de Carbono")
st.write("Ingresa tus datos de consumo mensual para estimar tu huella de carbono en kg de CO₂.")

# --- Entradas del usuario ---
km_auto = st.number_input("Kilómetros recorridos en auto por semana", min_value=0.0, value=0.0)
consumo_luz = st.number_input("Consumo eléctrico mensual (kWh)", min_value=0.0, value=0.0)
vuelos = st.number_input("Vuelos tomados en el último año", min_value=0, value=0, step=1)
carne_semana = st.number_input("Porciones de carne roja por semana", min_value=0, value=0, step=1)

# --- Factores de emisión aproximados ---
FACTOR_AUTO = 0.21      # kg CO2 por km
FACTOR_LUZ = 0.45       # kg CO2 por kWh
FACTOR_VUELO = 250      # kg CO2 por vuelo promedio
FACTOR_CARNE = 3.3      # kg CO2 por porción

if st.button("Calcular huella"):
    huella_auto = km_auto * 4.33 * FACTOR_AUTO   # semanas a mes
    huella_luz = consumo_luz * FACTOR_LUZ
    huella_vuelos = (vuelos / 12) * FACTOR_VUELO
    huella_carne = carne_semana * 4.33 * FACTOR_CARNE

    total = huella_auto + huella_luz + huella_vuelos + huella_carne

    st.subheader("Resultado")
    st.metric("Huella de carbono mensual estimada", f"{total:,.1f} kg CO₂")

    st.write("**Desglose:**")
    st.write(f"- Transporte: {huella_auto:,.1f} kg CO₂")
    st.write(f"- Electricidad: {huella_luz:,.1f} kg CO₂")
    st.write(f"- Vuelos: {huella_vuelos:,.1f} kg CO₂")
    st.write(f"- Consumo de carne: {huella_carne:,.1f} kg CO₂")

    if total > 500:
        st.warning("Tu huella está por encima del promedio recomendado. Considera reducir el uso del auto o el consumo de carne.")
    else:
        st.success("¡Tu huella está en un rango razonable!")