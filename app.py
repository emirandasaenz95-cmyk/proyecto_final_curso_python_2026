import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.csic_climate.data_loader import load_climate_data, filter_by_region_and_years
from src.csic_climate.metrics import calculate_climate_summary, calculate_decadal_trend

# Configuración de la página de Streamlit
st.set_page_config(
    page_title="CSIC ClimateWatch - Monitor de Sequía y Cambio Climático",
    page_icon="🌍",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-title {
        font-size: 2.3rem;
        color: #1E3A8A;
        font-weight: 700;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Título y Cabecera Institucional
st.markdown('<p class="main-title">🌍 CSIC ClimateWatch: Monitor de Cambio Climático y Sequía</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Análisis de Series Temporales (1961 - 2025) derivado del IPE-CSIC y AEMET</p>', unsafe_allow_html=True)

# Cargar Datos Climáticos
@st.cache_data
def get_data():
    return load_climate_data()

try:
    df_raw = get_data()
except Exception as e:
    st.error(f"Error al cargar el dataset climático: {e}")
    st.stop()

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.header("🔍 Filtros de Selección")

# Lista de Comunidades Autónomas
regiones = ["Todas"] + sorted(df_raw["comunidad_autonoma"].unique().tolist())
region_sel = st.sidebar.selectbox("Selecciona Comunidad Autónoma:", regiones)

# Rango de Años
min_year = int(df_raw["anio"].min())
max_year = int(df_raw["anio"].max())

year_range = st.sidebar.slider(
    "Selecciona Rango de Años:",
    min_value=min_year,
    max_value=max_year,
    value=(1980, 2025)
)

# Filtrar Datos
df_filtered = filter_by_region_and_years(
    df_raw, 
    region=region_sel, 
    start_year=year_range[0], 
    end_year=year_range[1]
)

# --- TARJETAS DE MÉTRICAS PRINCIPALES ---
summary = calculate_climate_summary(df_filtered)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Temp. Media", f"{summary['temp_media']} °C")
col2.metric("Anomalía Térmica", f"{summary['anomalia_media']} °C", delta=f"{summary['anomalia_media']} °C", delta_color="inverse")
col3.metric("Precipitación Total", f"{summary['precipitacion_total']} mm")
col4.metric("Meses Sequía Severa", f"{summary['meses_sequia_severa']} meses")
col5.metric("Días en Ola de Calor", f"{summary['dias_totales_ola_calor']} días")

st.markdown("---")

# --- PESTAÑAS DE CONTENIDO ---
tab1, tab2, tab3 = st.tabs(["📊 Visualización y Gráficos", "🧮 Tabla de Datos", "👥 Información y Grupos"])

with tab1:
    st.subheader("Evolución de la Anomalía Térmica y Sequía")
    
    # Agrupar por año para los gráficos de tendencia
    df_annual = df_filtered.groupby("anio").agg({
        "temperatura_media_c": "mean",
        "anomalia_termica_c": "mean",
        "precipitacion_mm": "sum",
        "indice_spei_sequia": "mean",
        "dias_ola_calor": "sum"
    }).reset_index()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    
    # Gráfico 1: Anomalía de Temperatura
    colors = ['#EF4444' if x > 0 else '#3B82F6' for x in df_annual["anomalia_termica_c"]]
    ax1.bar(df_annual["anio"], df_annual["anomalia_termica_c"], color=colors, alpha=0.85)
    ax1.axhline(0, color='black', linestyle='--', linewidth=0.8)
    ax1.set_ylabel("Anomalía Térmica (°C)")
    ax1.set_title(f"Anomalía Anual de Temperatura - {region_sel}")
    ax1.grid(True, linestyle=":", alpha=0.6)
    
    # Gráfico 2: Índice SPEI de Sequía
    ax2.plot(df_annual["anio"], df_annual["indice_spei_sequia"], color='#059669', linewidth=1.8, label="Índice SPEI")
    ax2.axhline(-1.5, color='#DC2626', linestyle='--', linewidth=1.2, label="Umbral Sequía Severa (-1.5)")
    ax2.axhline(0, color='gray', linestyle=':', linewidth=0.8)
    ax2.set_xlabel("Año")
    ax2.set_ylabel("Índice SPEI")
    ax2.set_title("Evolución del Índice de Sequía SPEI (CSIC)")
    ax2.legend(loc="lower left")
    ax2.grid(True, linestyle=":", alpha=0.6)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Gráfico de Tendencia Decadal
    st.subheader("Tendencia por Décadas")
    df_decadal = calculate_decadal_trend(df_filtered)
    
    fig_dec, ax_dec = plt.subplots(figsize=(8, 3.5))
    sns.barplot(data=df_decadal, x="decada", y="anomalia_termica_c", palette="Reds", ax=ax_dec)
    ax_dec.set_xlabel("Década")
    ax_dec.set_ylabel("Anomalía Media (°C)")
    ax_dec.set_title("Anomalía Térmica Promedio por Década")
    st.pyplot(fig_dec)

with tab2:
    st.subheader("Explorador de Datos Históricos (Pandas)")
    st.dataframe(df_filtered, use_container_width=True)
    
    # Botón para descargar CSV filtrado
    csv_bytes = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Datos Filtrados en CSV",
        data=csv_bytes,
        file_name=f"csic_climate_{region_sel}_{year_range[0]}_{year_range[1]}.csv",
        mime="text/csv"
    )

with tab3:
    st.subheader("👥 Organización del Trabajo en Grupos de GitHub")
    st.markdown("""
    Este repositorio base está preparado para ser extendido en equipo mediante **GitHub Pull Requests**:
    
    - **Grupo 1 (Backend / Ciencia de Datos):** Implementar nuevas métricas en `src/csic_climate/metrics.py`.
    - **Grupo 2 (Frontend / Streamlit):** Integrar los nuevos gráficos e indicadores visuales en `app.py`.
    - **Grupo 3 (Documentación & FAIR):** Completar el `README.md`, licencias y citación `CITATION.cff`.
    - **Grupo 4 (Testing & CI/CD):** Crear tests unitarios en `tests/` y automatizar GitHub Actions (`.github/workflows/ci.yml`).
    """)
