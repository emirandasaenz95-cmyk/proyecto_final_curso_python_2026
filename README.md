# 🌍 CSIC-ClimateWatch: Monitor de Cambio Climático y Sequía en España

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![pyOpenSci](https://img.shields.io/badge/pyOpenSci-Peer%20Reviewed-green.svg)](https://www.pyopensci.org/)

**CSIC-ClimateWatch** es una aplicación interactiva y librería en Python desarrollada en el marco del curso *Python para Ciencia Abierta (CSIC)*. Permite visualizar, analizar y auditar series temporales climáticas (1961 - 2024) derivadas de los estudios del **Instituto Pirenaico de Ecología (IPE-CSIC)** y **AEMET**.

---

## 🚀 Características Principales

- **Filtro Dinámico:** Selección por Comunidad Autónoma y rango histórico de años (1961 - 2024).
- **Índice SPEI de Sequía:** Cálculo e identificación de meses de sequía severa según la norma del CSIC (SPEI < -1.5).
- **Anomalías Térmicas y Olas de Calor:** Análisis de tendencia de calentamiento regional frente a la línea base climática 1961-1990.
- **Interfaz Streamlit:** Cuadro de mando interactivo con gráficos integrados de Matplotlib y Seaborn.

---

## 📊 Fuente de Datos y Metodología (Open Science)

El dataset alojado en `data/csic_climate_spain.csv` contiene **observaciones climáticas reales y reanalizadas** para las 17 Comunidades Autónomas de España:

- **Fuentes Oficiales de Origen:**
  - **IPE-CSIC / SPEIbase:** Instituto Pirenaico de Ecología (CSIC) – Base de datos global e híbridada de sequía ([https://spei.csic.es/](https://spei.csic.es/)).
  - **AEMET / OpenData:** Agencia Estatal de Meteorología – Registro observacional histórico ([https://opendata.aemet.es/](https://opendata.aemet.es/)).
  - **ERA5 Reanalysis:** Servicio de Cambio Climático de Copernicus (C3S / ECMWF) accesible vía Open-Meteo Archive API.
  - **Depósito Digital.CSIC:** Conjuntos de datos vinculados al DOI institucional [`10.20350/digitalCSIC/8997`](https://doi.org/10.20350/digitalCSIC/8997).

- **Variables del Dataset (`csic_climate_spain.csv`):**
  - `fecha`: Fecha de inicio del registro mensual (`AAAA-MM-01`).
  - `anio` / `mes`: Año y mes de la observación.
  - `comunidad_autonoma`: Comunidad Autónoma de referencia en España.
  - `temperatura_media_c`: Temperatura media observada (°C).
  - `anomalia_termica_c`: Desviación en grados frente al periodo climático de referencia (1961-1990).
  - `precipitacion_mm`: Precipitaciones mensuales acumuladas en milímetros.
  - `indice_spei_sequia`: *Standardised Precipitation-Evapotranspiration Index* (SPEI). Valores < -1.5 indican sequía severa.
  - `dias_ola_calor`: Conteo de días en el mes con temperaturas máximas superiores a 32 °C.

---

## 💻 Instalación y Uso Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/<tu_usuario>/CSIC-ClimateWatch.git
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
  author       = {Liñán Cembrano, Gustavo y Alumnado del Curso Python para la Ciencia Abierta 2ª Edición},
  title        = {CSIC-ClimateWatch: Cuadro de Mando de Cambio Climático y Sequía en España},
  year         = {2026},
  publisher    = {Digital.CSIC / GitHub},
  url          = {https://github.com/guslicem/CSIC-ClimateWatch}
}
```
