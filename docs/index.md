# Documentación Oficial de CSIC-ClimateWatch

Bienvenido a la documentación oficial del proyecto **CSIC-ClimateWatch**, la librería y cuadro de mando interactivo para el estudio del Cambio Climático y la Sequía en España.

```{toctree}
:maxdepth: 2
:caption: Contenidos:

README <self>
autoapi/index
```

## 🚀 Inicio Rápido

```python
from csic_climate.data_loader import load_climate_data, filter_by_region_and_years
from csic_climate.metrics import calculate_climate_summary

# Cargar dataset climático histórico (1961 - 2024)
df = load_climate_data()

# Filtrar por región y calcular métricas
df_madrid = filter_by_region_and_years(df, region="Comunidad de Madrid", start_year=2000, end_year=2024)
summary = calculate_climate_summary(df_madrid)
print(summary)
```

## 📜 Principios FAIR y Ciencia Abierta

El proyecto se distribuye bajo la Licencia MIT e incluye metadatos de citación en formato `CITATION.cff` e inyección de Handle de Digital.CSIC (`10261/XXXIXXIXIXI`).
