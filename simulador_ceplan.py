
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Simulación Consistencia → Seguimiento", layout="wide")
st.title("Simulador Funcional del Aplicativo CEPLAN")
st.subheader("Etapas: Consistencia → Seguimiento del POI")

# Sección 1: Estado de la etapa de Consistencia
st.markdown("### 1. Cierre de Consistencia")
with st.expander("Estado de POI Consistenciado"):
    aprobado = st.checkbox("Consistencia validada por todas las UE")
    if aprobado:
        st.success("✅ Consistencia lista para transición")
        if st.button("Cerrar Consistencia y Crear Base de Seguimiento"):
            st.session_state['seguimiento_iniciado'] = True
            st.success("Base para Seguimiento creada exitosamente")
    else:
        st.warning("Esperando validación de todas las UE")

# Sección 2: Seguimiento
st.markdown("### 2. Registro de Avance del POI")
if st.session_state.get('seguimiento_iniciado'):
    st.markdown("#### Actividades Prioritarias")
    data = {
        'Actividad': ['Capacitación técnica', 'Mantenimiento de red', 'Supervisión territorial'],
        'Meta Fisica Programada': [100, 80, 50],
        'Meta Fisica Ejecutada': [st.slider('Avance Capacitación (%)', 0, 100, 50),
                                   st.slider('Avance Mantenimiento (%)', 0, 100, 60),
                                   st.slider('Avance Supervisión (%)', 0, 100, 30)],
        'Evidencia': ['', '', '']
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.markdown("#### Cargar Evidencias")
    for i, row in df.iterrows():
        file = st.file_uploader(f"Evidencia para {row['Actividad']}", type=['pdf', 'jpg', 'png'], key=f"file_{i}")
        if file:
            df.at[i, 'Evidencia'] = file.name

    if st.button("Guardar Seguimiento"):
        st.success("Datos guardados y bitácora actualizada")

# Sección 3: Reporte
st.markdown("### 3. Reportes y Alertas")
if st.session_state.get('seguimiento_iniciado'):
    if st.button("Generar Reporte Consolidado"):
        st.download_button("Descargar Reporte (CSV)", df.to_csv(index=False), file_name="reporte_seguimiento.csv")
        st.info("Incluye % avance y evidencias registradas")

# Pie
st.markdown("---")
st.caption("Simulación diseñada por Dncp IA para el CEPLAN - Mayo 2025")
