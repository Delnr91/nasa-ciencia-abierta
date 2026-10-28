"""Ejemplo educativo: datos completamente sintéticos, sin validez observacional.
Código original bajo MIT: consulta LICENSE en esta carpeta.
No escribe archivos, no instala paquetes y no consulta servicios externos.
"""
import csv
import io
import math
from datetime import date
from statistics import mean

CSV_SINTETICO = "fecha,sensor_id,temperatura_c\n2026-01-01,A,20\n2026-01-01,B,18\n2026-01-02,A,22\n2026-01-02,B,20\n2026-01-03,A,24\n2026-01-03,B,22\n"

def analizar(texto):
    lector = csv.DictReader(io.StringIO(texto))
    if lector.fieldnames != ["fecha", "sensor_id", "temperatura_c"]:
        raise ValueError("Columnas inesperadas")
    grupos = {}
    valores = []
    for fila in lector:
        if None in fila or any(v is None for v in fila.values()):
            raise ValueError("Fila incompleta o con columnas adicionales")
        date.fromisoformat(fila["fecha"])
        sensor = fila["sensor_id"].strip()
        if not sensor:
            raise ValueError("Sensor sin identificador")
        valor = float(fila["temperatura_c"])
        if not math.isfinite(valor):
            raise ValueError("Temperatura no finita")
        valores.append(valor)
        grupos.setdefault(sensor, []).append(valor)
    if not valores:
        raise ValueError("No hay datos")
    return {
        "observaciones_sinteticas": len(valores),
        "media_global_c": mean(valores),
        "medias_por_sensor_c": {k: mean(v) for k, v in sorted(grupos.items())},
    }

if __name__ == "__main__":
    import json
    print(json.dumps(analizar(CSV_SINTETICO), ensure_ascii=False, indent=2))
