import requests
import pandas as pd
from io import StringIO

# URL de la API pública con la consulta para obtener los primeros 1000 elementos
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+ra,dec,sy_name,hostname,sy_snum,sy_pnum,sy_mnum,st_mass+from+stellarhosts+LIMIT+1000"

try:
    # Hacer una solicitud GET a la API
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Imprimir el contenido para verificar la respuesta
        print("Contenido de la respuesta:")
        print(response.text[:500])  # Muestra solo los primeros 500 caracteres

        # Cargar el contenido CSV en un DataFrame
        df = pd.read_csv(StringIO(response.text), sep=',')  # Asegúrate de que el separador sea correcto

        # Imprimir el DataFrame
        print("\nDataFrame con los primeros 1000 elementos:")
        print(df)
    else:
        print(f"Error al conectar a la API: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")




