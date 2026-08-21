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
  > 📌 *[TAREA EQUIPO 3 (DOCUMENTACIÓN)]: Verificar y actualizar el enlace permanente de Digital.CSIC sustituyendo `XXXXXXXXX` por lo que corresponda.*

- **Variables del Dataset (`csic_climate_spain.csv`):**

  > 📌 *[TAREA EQUIPO 3 (DOCUMENTACIÓN)]: Completar la siguiente tabla describiendo el significado científico y las unidades de cada una de las 9 columnas.*

  | Columna | Tipo de Dato | Descripción Científica / Unidades |
  | :--- | :--- | :--- |
  | `fecha` | Date (`AAAA-MM-01`) | Fecha del primer día del mes observado |
  | `year` | Int | Año de la observación (1961 - 2024) |
  | `mes` | Int | Mes del año (1 - 12) |
  | `comunidad_autonoma` | String | Nombre oficial de la CC.AA. en España |
  | `temperatura_media_c` | Float | *[A completar por Equipo 3]* |
  | `anomalia_termica_c` | Float | *[A completar por Equipo 3]* |
  | `precipitacion_mm` | Float | *[A completar por Equipo 3]* |
  | `indice_spei_sequia` | Float | *[A completar por Equipo 3]* |
  | `dias_ola_calor` | Int | *[A completar por Equipo 3]* |

---

## 💻 Instalación y Uso Local

```bash
# 1. Clonar el repositorio del proyecto
git clone https://github.com/guslicem/XUUXYXYX.git
# 📌 [TAREA EQUIPO 3]: Reemplazar XUUXYXYX.git por el nombre real del repositorio (proyecto_final_curso_python_2026.git)

cd proyecto_final_curso_python_2026

# 2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar las dependencias en modo editable
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
- **`README.md`**, **`CITATION.cff`** y **`CHANGELOG.md`**: Documentación FAIR y Ciencia Abierta (**Grupo 3**).
- **`tests/` & `.github/workflows/ci.yml`**: Pruebas unitarias `pytest` y CI/CD (**Grupo 4**).

---

## 📜 Licencia y Citación

Este proyecto está bajo la Licencia MIT. Para citar el uso de los datos o el paquete:

> 📌 *[TAREA EQUIPO 3 (DOCUMENTACIÓN)]: Completar los autores, el año de publicación y la URL del repositorio tanto en el bloque BibTeX inferior como en el archivo `CITATION.cff`.*

```bibtex
@software{csic_climatewatch_2026,
  author       = {XXXXXXXXX},
  title        = {CSIC-ClimateWatch: Dashboard de Cambio Climático y Sequía en España},
  year         = {YYYYY},
  publisher    = {Digital.CSIC / GitHub},
  url          = {https://github.com/guslicem/XUXUXYXYXYXYX}
}
```

---

## 📝 Historial de Cambios (`CHANGELOG.md`)

> 📌 *[TAREA EQUIPO 3 (DOCUMENTACIÓN)]: Actualizar el archivo `CHANGELOG.md` al recibir las Pull Requests de los Equipos 1 (Backend), 2 (Frontend) y 4 (Testing).*
