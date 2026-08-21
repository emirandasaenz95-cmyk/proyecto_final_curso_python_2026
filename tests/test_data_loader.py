import pytest
import pandas as pd
from csic_climate.data_loader import load_climate_data, filter_by_region_and_years

def test_load_climate_data():
    """Verifica que el cargador de datos lea correctamente el dataset y formatee la fecha."""
    df = load_climate_data()
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "fecha" in df.columns
    assert "year" in df.columns
    assert "comunidad_autonoma" in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df["fecha"])

def test_filter_by_region_and_years_single():
    """Verifica el filtrado por una Comunidad Autónoma específica y rango temporal."""
    df = load_climate_data()
    filtered = filter_by_region_and_years(df, region="Andalucía", start_year=2000, end_year=2010)
    
    assert not filtered.empty
    assert (filtered["comunidad_autonoma"] == "Andalucía").all()
    assert (filtered["year"] >= 2000).all()
    assert (filtered["year"] <= 2010).all()

def test_filter_by_region_and_years_all():
    """Verifica el comportamiento cuando region es 'Todas'."""
    df = load_climate_data()
    filtered = filter_by_region_and_years(df, region="Todas", start_year=2020, end_year=2024)
    
    assert not filtered.empty
    assert filtered["comunidad_autonoma"].nunique() == 17
    assert (filtered["year"] >= 2020).all()

def test_filter_by_region_empty_result():
    """Verifica que un rango sin registros devuelva un DataFrame vacío sin lanzar excepción."""
    df = load_climate_data()
    filtered = filter_by_region_and_years(df, region="Andalucía", start_year=1800, end_year=1850)
    
    assert isinstance(filtered, pd.DataFrame)
    assert filtered.empty
