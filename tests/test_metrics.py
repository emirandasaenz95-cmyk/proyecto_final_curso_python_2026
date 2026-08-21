import pytest
import pandas as pd
from csic_climate.metrics import calculate_climate_summary, calculate_decadal_trend

@pytest.fixture
def sample_climate_data():
    """Fixture que proporciona un DataFrame sintético para las pruebas unitarias."""
    data = {
        "fecha": ["1990-01-01", "1990-06-01", "2020-01-01", "2020-06-01"],
        "year": [1990, 1990, 2020, 2020],

        "mes": [1, 6, 1, 6],
        "comunidad_autonoma": ["Andalucía", "Andalucía", "Andalucía", "Andalucía"],
        "temperatura_media_c": [12.0, 26.0, 14.0, 28.0],
        "anomalia_termica_c": [0.2, 0.5, 1.2, 1.8],
        "precipitacion_mm": [50.0, 10.0, 30.0, 5.0],
        "indice_spei_sequia": [0.1, -1.8, -0.5, -2.1],
        "dias_ola_calor": [0, 2, 0, 5]
    }
    return pd.DataFrame(data)

def test_calculate_climate_summary(sample_climate_data):
    summary = calculate_climate_summary(sample_climate_data)
    
    assert summary["temp_media"] == 20.0
    assert summary["anomalia_media"] == 0.92
    assert summary["precipitacion_total"] == 95.0
    assert summary["meses_sequia_severa"] == 2  # -1.8 y -2.1 son < -1.5
    assert summary["dias_totales_ola_calor"] == 7

def test_calculate_climate_summary_empty():
    empty_df = pd.DataFrame(columns=["temperatura_media_c", "anomalia_termica_c", "precipitacion_mm", "indice_spei_sequia", "dias_ola_calor"])
    summary = calculate_climate_summary(empty_df)
    assert summary["temp_media"] == 0.0
    assert summary["meses_sequia_severa"] == 0

def test_calculate_decadal_trend(sample_climate_data):
    trend = calculate_decadal_trend(sample_climate_data)
    assert len(trend) == 2
    assert 1990 in trend["decada"].values
    assert 2020 in trend["decada"].values
