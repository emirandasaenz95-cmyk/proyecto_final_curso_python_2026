import os
import pandas as pd
from typing import Optional, List

# Ruta por defecto al dataset local dentro de data/
DEFAULT_DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "csic_climate_spain.csv")
)

def load_climate_data(filepath: Optional[str] = None) -> pd.DataFrame:
    """
    Carga el dataset climático histórico del CSIC (1961 - 2025).
    
    Args:
        filepath: Ruta al archivo CSV. Si es None, utiliza la ruta por defecto.
        
    Returns:
        pd.DataFrame: DataFrame procesado con la columna 'fecha' en formato datetime.
    """
    path = filepath if filepath else DEFAULT_DATA_PATH
    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo de datos climáticos en: '{path}'")
        
    df = pd.read_csv(path)
    df["fecha"] = pd.to_datetime(df["fecha"])
    return df

def filter_by_region_and_years(
    df: pd.DataFrame, 
    region: Optional[str] = None, 
    start_year: int = 1961, 
    end_year: int = 2025
) -> pd.DataFrame:
    """
    Filtra los datos climáticos por Comunidad Autónoma y rango de años.
    """
    filtered = df[(df["year"] >= start_year) & (df["year"] <= end_year)].copy()

    if region and region != "Todas":
        filtered = filtered[filtered["comunidad_autonoma"] == region]
    return filtered
