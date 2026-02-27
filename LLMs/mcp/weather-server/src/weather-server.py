import logging
from typing import Any 

import httpx
from mcp.server.fastmcp import FastMCP
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



## -----------------------------------------------------

# Inicializar el servidor MCP
mcp=FastMCP("weather-server")

# Constantes
NWS_API_BASE = "https://api.weather.gov" #  URL base de la API.
USER_AGENT = "weather-app/1.0" # ID application

# --------------------------------------------------------
# HELPER FUNCTIONS: funcion petition , funcion formato 

async def make_nws_request(url: str) -> dict[str, Any]|None:
    """
    Feat: Hacer la petición de NWS API con manejo de errores.
    """
    # definicmos acceso: user, formato json.
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            # logging.info(response.json())
            return response.json()
        except Exception:
            return None 


def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get("event", "Unknown")}
Area: {props.get("areaDesc", "Unknown")}
Severity: {props.get("severity", "Unknown")}
Description: {props.get("description", "No description available")}
Instructions: {props.get("instruction", "No specific instructions provided")}
"""

#---------------------------------------------------------
# HANDLERS: Funciones ejecutoras de tools y logicas.

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)  

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Obtener pronostico para una ubicación.
    Args:
        latitude: latitud de la ubicacion.
        longitude: longitud de la ubicacion.
    """
    # first: obtener pronostico apartir de puntos.
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "No se puede extraer pronostico de la ubicación"
    
    # Get el pronostico URL de los puntos.
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "No se puede extraer pronostico detallado"

    # Dandole formato 
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period["name"]}:
Temperature: {period["temperature"]}°{period["temperatureUnit"]}
Wind: {period["windSpeed"]} {period["windDirection"]}
Forecast: {period["detailedForecast"]}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)



def main():
    # Inicializar y ejecutar el server.
    mcp.run(transport="stdio") # transporte de datos.



if __name__ == "__main__":
    
    logging.info("Starting Weather Server MCP ... ")
    main()

    # async def _debug():
    #     logging.info("Starting weather Server MCP . . . ")
    #     # Ejemplo de coord NY.
    #     result = await get_forecast(40.7128, -74.0060)
    #     print(f"Resultado get_forecast:{result}")
    # asyncio.run(_debug())

