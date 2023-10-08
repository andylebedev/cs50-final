from project import get_city, get_coordinates, get_weather
import pytest

def test_get_city():
    with pytest.raises(TypeError):
        get_city("ACB")

def test_get_coordinates():
    latitude, longitude = get_coordinates('Kyiv')
    assert latitude == '50.4020'
    assert longitude == '30.6148'

def test_get_weather():
    with pytest.raises(TypeError):
        get_city(50,30)
