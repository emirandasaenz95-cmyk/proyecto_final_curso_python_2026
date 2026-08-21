# 🌍 CSIC-ClimateWatch: Monitor de Cambio Climático y Sequía en España

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![pyOpenSci](https://img.shields.io/badge/pyOpenSci-Peer%20Reviewed-green.svg)](https://www.pyopensci.org/)

**CSIC-ClimateWatch** es una aplicación interactiva y librería en Python desarrollada en el marco del curso *Python para Ciencia Abierta (CSIC)*. Permite visualizar y analizar series temporales de cambio climático y sequía (1961 - 2024) para las 17 Comunidades Autónomas de España.

---

## 🚀 Características Principales

- **Filtro Dinámico:** Selección por Comunidad Autónoma y rango histórico de años (1961 - 2024).
- **Índice SPEI de Sequía:** Cálculo e identificación de meses de sequía severa según la metodología desarrollada por el **Instituto Pirenaico de Ecología (IPE-CSIC)** (SPEI < -1.5).
- **Anomalías Térmicas y Olas de Calor:** Análisis de tendencia de calentamiento regional frente al periodo climático de referencia (1961 - 1990).
- **Interfaz Streamlit:** Cuadro de mando interactivo en Modo Oscuro con gráficos de Matplotlib y Seaborn.

---

## 📊 Fuente de Datos y Metodología (Transparencia Open Science)

El dataset alojado en `data/csic_climate_spain.csv` combina series meteorológicas observadas/reanalizadas con la metodología científica del CSIC:

- **Origen de los Datos Meteorológicos:**
  - **ERA5 Reanalysis (Copernicus / ECMWF):** Las series temporales de temperatura y precipitación mensual (1961 - 2024) se obtuvieron a partir del modelo de reanálisis ERA5 del Servicio de Cambio Climático de Copernicus / ECMWF (vía API REST de Open-Meteo).
- **Metodología de Sequía:**
  - **Algoritmo SPEI (IPE-CSIC):** El *Standardised Precipitation-Evapotranspiration Index* (SPEI) se calcula aplicando la formulación del Instituto Pirenaico de Ecología (IPE-CSIC) (Vicente-Serrano et al., [Digital.CSIC Handle: 10261/22405](https://digital.csic.es/handle/10261/XXXXXXXXX)).



- **Variables del Dataset (`csic_climate_spain.csv`):**
  A completar por el equipo doc.

---

## 💻 Instalación y Uso Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/guslicem/XUUXYXYX.git
cd CSIC-ClimateWatch

# 2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar las dependencias
pip install -r requirements.txt
pip install -e .

# 4. Lanzar la aplicación interactiva de Streamlit
streamlit run app.py
```

---

## 👥 Estructura del Proyecto y Colaboración en GitHub

El proyecto está diseñado para el trabajo colaborativo en 4 grupos de investigación:

- **`src/csic_climate/metrics.py`**: Funciones analíticas backend (**Grupo 1**).
- **`app.py`**: Interfaz de usuario Streamlit (**Grupo 2**).
- **`README.md` & `CITATION.cff`**: Documentación FAIR y Ciencia Abierta (**Grupo 3**).
- **`tests/` & `.github/workflows/ci.yml`**: Arnés de pruebas unitarias `pytest` y CI/CD (**Grupo 4**).

---

## 📜 Licencia y Citación

Este proyecto está bajo la Licencia MIT. Para citar el uso de los datos o el paquete:

```bibtex
@software{csic_climatewatch_2026,
  author       = {XXXXXXXXX},
  title        = {CSIC-ClimateWatch: Dashboard de Cambio Climático y Sequía en España},
  year         = {YYYYY},
  publisher    = {Digital.CSIC / GitHub},
  url          = {https://github.com/guslicem/XUXUXYXYXYXYX}
}
```
