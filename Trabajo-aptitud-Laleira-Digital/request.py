import requests

# Define el payload JSON
payload = {"price": 999.99, "people": 4, "tip": 20.40}

# Envía la solicitud POST al servidor local
response = requests.post("http://0.0.0.0:8080/calcular_factura/", json=payload)

#
print(response.json())
