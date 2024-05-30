import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import requests


def test_calcular_factura():
    payload = {"price": 100.0, "people": 4, "tip": 10.0}
    response = requests.post("http://0.0.0.0:8080/calcular_factura/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"total": 110.0, "factura por persona": 27.5}


def test_calcular_factura_no_tip():
    payload = {"price": 100.0, "people": 4, "tip": 0.0}
    response = requests.post("http://0.0.0.0:8080/calcular_factura/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"total": 100.0, "factura por persona": 25.0}


def test_calcular_factura_one_person():
    payload = {"price": 50.0, "people": 1, "tip": 15.0}
    response = requests.post("http://0.0.0.0:8080/calcular_factura/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"total": 57.5, "factura por persona": 57.5}


@pytest.mark.asyncio
async def test_calcular_factura_negative_tip():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/calcular_factura/", json={"price": 100.0, "people": 4, "tip": -10.0}
        )
    assert (
        response.status_code == 422
    )  # HTTP 422 Unprocessable Entity for invalid input
