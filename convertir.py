# Conversor USD -> CLP (Versión 3: con tipo de cambio en tiempo real)

import requests

# 1. Le pedimos a la API el dolar de hoy
print("Consultando el tipo de cambio actual...")
url = "https://mindicador.cl/api/dolar"
respuesta = requests.get(url)
datos = respuesta.json()

# 2. Extraemos el valor del dolar de la respuesta
tipo_de_cambio = datos["serie"][0]["valor"]
fecha = datos["serie"][0]["fecha"][:10]  # solo los primeros 10 caracteres (YYYY-MM-DD)

print(f"Tipo de cambio del {fecha}: 1 USD = {tipo_de_cambio} CLP")
print()

# 3. Le preguntamos al usuario cuanto gano
texto_ingresado = input("¿Cuántos USD ganaste? ")
usd = float(texto_ingresado)

# 4. Calculamos
clp = usd * tipo_de_cambio

# 5. Mostramos el resultado con formato bonito
print()
print(f"Tienes {usd:,.2f} USD")
print(f"Equivalen a ${clp:,.0f} CLP")