import pandas as pd
import numpy as np
from typing import Dict, Any

def calculate_climate_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calcula los indicadores climáticos principales a partir de un DataFrame filtrado.
    
    Args:
        df: DataFrame filtrado con datos climáticos.
        
    Returns:
        Dict[str, Any]: Diccionario con las métricas calculadas.
    """
    if df.empty:
        return {
            "temp_media": 0.0,
            "anomalia_media": 0.0,
            "precipitacion_total": 0.0,
            "meses_sequia_severa": 0,
            "dias_totales_ola_calor": 0
        }
        
    temp_media = round(df["temperatura_media_c"].mean(), 2)
    anomalia_media = round(df["anomalia_termica_c"].mean(), 2)
    precipitacion_total = round(df["precipitacion_mm"].sum(), 1)
    
    # Se considera sequía severa cuando el índice SPEI es menor a -1.5 (Norma IPE-CSIC)
    meses_sequia = int((df["indice_spei_sequia"] < -1.5).sum())
    tot_olas_calor = int(df["dias_ola_calor"].sum())
    
    return {
        "temp_media": temp_media,
        "anomalia_media": anomalia_media,
        "precipitacion_total": precipitacion_total,
        "meses_sequia_severa": meses_sequia,
        "dias_totales_ola_calor": tot_olas_calor
    }

def calculate_decadal_trend(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por década y calcula el promedio de anomalía térmica y sequía.
    """
    df_copy = df.copy()
    df_copy["decada"] = (df_copy["anio"] // 10) * 10
    
    summary = df_copy.groupby("decada").agg({
        "temperatura_media_c": "mean",
        "anomalia_termica_c": "mean",
        "precipitacion_mm": "mean",
        "indice_spei_sequia": "mean",
        "dias_ola_calor": "sum"
    }).reset_index()
    
    summary = summary.round(2)
    return summary

# ==============================================================================
# ESPACIO DE TRABAJO PARA EL GRUPO 1 (BACKEND / CIENCIA DE DATOS)
# ==============================================================================
# El Grupo 1 añadirá aquí sus nuevas funciones analíticas avanzadas, por ejemplo:
# - calculate_warming_rate_per_decade(df)
# - detect_extreme_climate_events(df)
# ==============================================================================
