import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.csic_climate.data_loader import load_climate_data, filter_by_region_and_years
from src.csic_climate.metrics import calculate_climate_summary, calculate_decadal_trend

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA Y TEMA STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="CSIC ClimateWatch - Monitor de Cambio Climático y Sequía",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Avanzados (Diseño Moderno, Neomorfismo y Modos Contrastados)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Banner Principal con Gradiente CSIC */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 45%, #047857 100%);
        padding: 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #FFFFFF, #93C5FD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #E2E8F0;
        margin-top: 8px;
        font-weight: 300;
    }
    
    .badge-csic {
        background-color: rgba(255, 255, 255, 0.15);
        color: #6EE7B7;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(110, 231, 183, 0.3);
        display: inline-block;
        margin-bottom: 12px;
    }
    
    /* Tarjetas de Métricas Personalizadas */
    .metric-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        border-color: #3B82F6;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #F8FAFC;
        margin: 8px 0;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 600;
    }
    
    .metric-delta-warning {
        color: #F87171;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .metric-delta-good {
        color: #34D399;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* Tarjeta de Información de Grupos */
    .group-box {
        background: #1E293B;
        border-left: 4px solid #3B82F6;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 12px;
        color: #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# --- CABECERA HERO ---
st.markdown("""
<div class="hero-container">
    <div class="badge-csic">Grupo de Trabajo del Curso<br>Python para la Ciencia Abierta: Introducción</div>
    <div class="hero-title">🌍 CSIC ClimateWatch</div>

    <div class="hero-subtitle">Monitor Interactivo de Cambio Climático, Sequía (SPEI) y Olas de Calor en España (1961 - 2024)</div>
</div>
""", unsafe_allow_html=True)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    return load_climate_data()

try:
    df_raw = load_data()
except Exception as e:
    st.error(f"❌ Error al cargar los datos climáticos: {e}")
    st.stop()

# --- BARRA LATERAL CON FILTROS ---
st.sidebar.markdown("### 🎛️ Filtros de Control")

# Obtener lista completa de Comunidades Autónomas ordenadas
regiones_disponibles = sorted(df_raw["comunidad_autonoma"].unique().tolist())
regiones_opciones = ["Todas"] + regiones_disponibles

region_sel = st.sidebar.selectbox(
    "📍 Selecciona Comunidad Autónoma:",
    regiones_opciones,
    index=0
)

# Slider de años
min_year = int(df_raw["anio"].min())
max_year = int(df_raw["anio"].max())

year_range = st.sidebar.slider(
    "📅 Rango Temporal (Años):",
    min_value=min_year,
    max_value=max_year,
    value=(1970, 2024),
    step=1
)

# Información en Barra Lateral
st.sidebar.markdown("---")
st.sidebar.markdown(f"**📊 Registros Filtrados:** {len(df_raw)} observaciones")
st.sidebar.markdown(f"**🏛️ Comunidades en Base:** {len(regiones_disponibles)}")
st.sidebar.caption("Fuente: ERA5 Reanalysis / IPE-CSIC (DOI: 10.20350/digitalCSIC/8997)")

# Filtrado de Datos
df_filtered = filter_by_region_and_years(
    df_raw, 
    region=region_sel, 
    start_year=year_range[0], 
    end_year=year_range[1]
)

# --- RESUMEN DE INDICADORES (TARJETAS KPI) ---
summary = calculate_climate_summary(df_filtered)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🌡️ Temp. Media</div>
        <div class="metric-value">{summary['temp_media']} °C</div>
        <div style="color: #94A3B8; font-size: 0.8rem;">Promedio Observado</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    delta_class = "metric-delta-warning" if summary['anomalia_media'] > 0 else "metric-delta-good"
    delta_icon = "🔥 +" if summary['anomalia_media'] > 0 else "❄️ "
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">☀️ Anomalía Térmica</div>
        <div class="metric-value" style="color: {'#F87171' if summary['anomalia_media'] > 0 else '#6EE7B7'};">{summary['anomalia_media']} °C</div>
        <div class="{delta_class}">{delta_icon}{summary['anomalia_media']} °C vs 1961-1990</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🌧️ Precipitación Total</div>
        <div class="metric-value" style="color: #60A5FA;">{summary['precipitacion_total']:,} <span style="font-size: 1rem;">mm</span></div>
        <div style="color: #94A3B8; font-size: 0.8rem;">Acumulado Periodo</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🏜️ Sequía Severa</div>
        <div class="metric-value" style="color: #F59E0B;">{summary['meses_sequia_severa']}</div>
        <div style="color: #94A3B8; font-size: 0.8rem;">Meses con SPEI < -1.5</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🔥 Días en Ola Calor</div>
        <div class="metric-value" style="color: #EF4444;">{summary['dias_totales_ola_calor']}</div>
        <div style="color: #94A3B8; font-size: 0.8rem;">Días T.Máx > 32°C</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- PESTAÑAS DE NAVEGACIÓN ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Series Temporales y Gráficos", 
    "🗺️ Comparativa Regional", 
    "🧮 Explorador Pandas", 
    "👥 Trabajo en Grupos (GitHub)"
])

# Estilo Oscuro Elegante para Matplotlib
plt.style.use('dark_background')

with tab1:
    st.subheader(f"📊 Evolución Climatológica - {region_sel} ({year_range[0]} - {year_range[1]})")
    
    # Agrupación Anual
    df_annual = df_filtered.groupby("anio").agg({
        "temperatura_media_c": "mean",
        "anomalia_termica_c": "mean",
        "precipitacion_mm": "sum",
        "indice_spei_sequia": "mean",
        "dias_ola_calor": "sum"
    }).reset_index()
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Gráfico 1: Anomalía de Temperatura
        fig1, ax1 = plt.subplots(figsize=(8, 4.5))
        fig1.patch.set_facecolor('#0F172A')
        ax1.set_facecolor('#1E293B')
        
        colors = ['#EF4444' if x > 0 else '#3B82F6' for x in df_annual["anomalia_termica_c"]]
        ax1.bar(df_annual["anio"], df_annual["anomalia_termica_c"], color=colors, alpha=0.9, width=0.8)
        ax1.axhline(0, color='#94A3B8', linestyle='--', linewidth=1)
        ax1.set_ylabel("Anomalía Térmica (°C)", color='#E2E8F0', fontsize=10)
        ax1.set_title("Anomalía Térmica Anual (°C vs Línea Base 1961-1990)", color='white', fontsize=12, fontweight='bold')
        ax1.grid(True, linestyle=":", alpha=0.3, color='#475569')
        ax1.tick_params(colors='#94A3B8')
        st.pyplot(fig1)

    with col_chart2:
        # Gráfico 2: Evolución de Sequía (SPEI)
        fig2, ax2 = plt.subplots(figsize=(8, 4.5))
        fig2.patch.set_facecolor('#0F172A')
        ax2.set_facecolor('#1E293B')
        
        ax2.plot(df_annual["anio"], df_annual["indice_spei_sequia"], color='#10B981', linewidth=2.2, label="Índice SPEI")
        ax2.axhline(-1.5, color='#EF4444', linestyle='--', linewidth=1.5, label="Umbral Sequía Severa (-1.5)")
        ax2.axhline(0, color='#94A3B8', linestyle=':', linewidth=0.8)
        ax2.fill_between(df_annual["anio"], df_annual["indice_spei_sequia"], -1.5, where=(df_annual["indice_spei_sequia"] <= -1.5), color='#EF4444', alpha=0.3)
        ax2.set_ylabel("Índice SPEI", color='#E2E8F0', fontsize=10)
        ax2.set_title("Índice Estandarizado de Sequía (SPEI - CSIC)", color='white', fontsize=12, fontweight='bold')
        ax2.legend(loc="lower left", facecolor='#1E293B', edgecolor='#334155')
        ax2.grid(True, linestyle=":", alpha=0.3, color='#475569')
        ax2.tick_params(colors='#94A3B8')
        st.pyplot(fig2)

    # Gráfico Decadal
    st.markdown("---")
    st.subheader("📅 Tendencia de Calentamiento por Décadas")
    df_decadal = calculate_decadal_trend(df_filtered)
    
    fig_dec, ax_dec = plt.subplots(figsize=(10, 3.5))
    fig_dec.patch.set_facecolor('#0F172A')
    ax_dec.set_facecolor('#1E293B')
    
    sns.barplot(
        data=df_decadal, 
        x="decada", 
        y="anomalia_termica_c", 
        hue="decada", 
        legend=False, 
        palette="Reds", 
        ax=ax_dec
    )
    ax_dec.set_xlabel("Década", color='#E2E8F0')
    ax_dec.set_ylabel("Anomalía Media (°C)", color='#E2E8F0')
    ax_dec.set_title("Incremento de Temperatura Promedio por Década (°C)", color='white', fontweight='bold')
    ax_dec.grid(True, linestyle=":", alpha=0.3, color='#475569')
    ax_dec.tick_params(colors='#94A3B8')
    st.pyplot(fig_dec)

with tab2:
    st.subheader("🗺️ Ranking y Comparativa entre Comunidades Autónomas")
    
    # Ranking Regional
    df_region_summary = df_raw[(df_raw["anio"] >= year_range[0]) & (df_raw["anio"] <= year_range[1])].groupby("comunidad_autonoma").agg({
        "anomalia_termica_c": "mean",
        "temperatura_media_c": "mean",
        "precipitacion_mm": "mean",
        "indice_spei_sequia": "mean",
        "dias_ola_calor": "sum"
    }).reset_index().round(2)
    
    col_rank1, col_rank2 = st.columns(2)
    
    with col_rank1:
        st.markdown("##### 🔥 Top 10 Comunidades con Mayor Anomalía Térmica (°C)")
        df_sorted_temp = df_region_summary.sort_values(by="anomalia_termica_c", ascending=False).head(10)
        
        fig_rank1, ax_r1 = plt.subplots(figsize=(7, 4.5))
        fig_rank1.patch.set_facecolor('#0F172A')
        ax_r1.set_facecolor('#1E293B')
        
        sns.barplot(data=df_sorted_temp, y="comunidad_autonoma", x="anomalia_termica_c", hue="comunidad_autonoma", legend=False, palette="YlOrRd_r", ax=ax_r1)
        ax_r1.set_xlabel("Anomalía Térmica (°C)")
        ax_r1.set_ylabel("")
        ax_r1.grid(True, linestyle=":", alpha=0.3, color='#475569')
        ax_r1.tick_params(colors='#94A3B8')
        st.pyplot(fig_rank1)

    with col_rank2:
        st.markdown("##### 🏜️ Top 10 Comunidades con Mayor Impacto de Olas de Calor (Días Acumulados)")
        df_sorted_heat = df_region_summary.sort_values(by="dias_ola_calor", ascending=False).head(10)
        
        fig_rank2, ax_r2 = plt.subplots(figsize=(7, 4.5))
        fig_rank2.patch.set_facecolor('#0F172A')
        ax_r2.set_facecolor('#1E293B')
        
        sns.barplot(data=df_sorted_heat, y="comunidad_autonoma", x="dias_ola_calor", hue="comunidad_autonoma", legend=False, palette="Oranges_r", ax=ax_r2)
        ax_r2.set_xlabel("Días Acumulados en Ola de Calor")
        ax_r2.set_ylabel("")
        ax_r2.grid(True, linestyle=":", alpha=0.3, color='#475569')
        ax_r2.tick_params(colors='#94A3B8')
        st.pyplot(fig_rank2)

with tab3:
    st.subheader("🧮 Explorador Interactivo del Dataset (Pandas)")
    st.dataframe(df_filtered, width="stretch")

    
    csv_bytes = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Dataset Filtrado en Formato CSV",
        data=csv_bytes,
        file_name=f"csic_climate_{region_sel}_{year_range[0]}_{year_range[1]}.csv",
        mime="text/csv"
    )

with tab4:
    st.subheader("👥 Organización del Trabajo en Grupos de GitHub")
    
    st.markdown("""
    <div class="group-box">
        <h4>🧮 GRUPO 1: Backend / Ciencia de Datos (<code>src/csic_climate/metrics.py</code>)</h4>
        <p><strong>Tarea:</strong> Implementar una nueva función analítica en Python (por ejemplo <code>calculate_warming_rate_per_decade(df)</code> o <code>detect_extreme_events(df)</code>).</p>
    </div>
    
    <div class="group-box" style="border-left-color: #10B981;">
        <h4>🎨 GRUPO 2: Frontend & Visualización (<code>app.py</code>)</h4>
        <p><strong>Tarea:</strong> Diseñar un nuevo widget interactivo y una tarjeta visual/gráfico en Streamlit que consuma la métrica creada por el Grupo 1.</p>
    </div>
    
    <div class="group-box" style="border-left-color: #F59E0B;">
        <h4>📖 GRUPO 3: Documentación & Ciencia Abierta (<code>README.md</code> y <code>CITATION.cff</code>)</h4>
        <p><strong>Tarea:</strong> Redactar la metodología científica, la descripción de las variables de la base del IPE-CSIC, la guía de instalación y las citas BibTeX.</p>
    </div>
    
    <div class="group-box" style="border-left-color: #EC4899;">
        <h4>🧪 GRUPO 4: Calidad de Software, Testing & CI/CD (<code>tests/</code> y <code>.github/workflows/ci.yml</code>)</h4>
        <p><strong>Tarea:</strong> Crear los tests unitarios con <code>pytest</code> para validar las nuevas funciones y asegurar que la automatización pase limpia en las Pull Requests.</p>
    </div>
    """, unsafe_allow_html=True)
