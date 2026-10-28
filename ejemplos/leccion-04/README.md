# Ejemplo 4 · Datos, código y resultados conectados

[← Lección 4](../../cursos/open-science-essentials/lecciones/04-componentes-ciencia-abierta.md) · [🏠 Inicio](../../README.md)

**Ejemplo educativo totalmente sintético.** No contiene observaciones reales ni datos personales.

## Sin programar: lee el recorrido

1. [Datos CSV](datos-sinteticos.csv): seis números inventados, dos sensores y tres fechas.
2. [Diccionario](#diccionario-de-datos): explica qué significa cada columna.
3. [Cuaderno con código y salidas](01-informe-reproducible.ipynb): muestra cómo se calcula.
4. [Informe breve](#informe-de-resultados): interpreta el resultado y sus límites.

GitHub puede mostrar el cuaderno y sus salidas guardadas; no las recalcula por abrirlo. Si su visor falla, el [programa en texto](analisis.py) y el informe siguen disponibles.

## Diccionario de datos

| Campo | Tipo y unidad | Significado |
|---|---|---|
| fecha | Fecha ISO, AAAA-MM-DD | Día ficticio del ejemplo; no fecha de una campaña real |
| sensor_id | Texto A o B | Identificador ficticio; no representa persona o instalación |
| temperatura_c | Número, grados Celsius | Valor inventado para practicar |

Datos de ejemplo versión **1.0**, creados para esta lección. No hay instrumento, calibración o ubicación reales. La versión exacta del paquete puede identificarse mediante el commit de GitHub; aquí no se ha registrado un DOI.

## Método

Media aritmética de los seis valores y media por identificador de sensor. No se pondera, interpola ni elimina observaciones.

El [programa](analisis.py) utiliza únicamente la biblioteca estándar de Python. Lleva la misma tabla incorporada que el CSV para poder ejecutarse sin red ni archivos auxiliares. Esa coincidencia se verifica durante la preparación de la lección.

## Informe de resultados

| Resultado | Valor esperado |
|---|---|
| Registros sintéticos | 6 |
| Media global | 21 °C |
| Media del sensor A | 22 °C |
| Media del sensor B | 20 °C |

**Interpretación:** el cálculo resume números inventados. No demuestra diferencia ambiental entre lugares, tendencia temporal, calibración ni rendimiento de un sistema real.

**Criterio de reproducción del ejemplo sin cambios:** mismo número de registros y mismos promedios para esta tabla concreta. No se deduce que cualquier estudio deba usar siempre igualdad exacta o esta misma prueba.

## Si quieres modificarlo

Abre el cuaderno en un entorno Jupyter compatible y ejecuta las celdas desde el inicio. Aquí no se crea ni se paga un entorno en la nube. Cambia una entrada, predice el efecto y explica por qué ya corresponde a otra ejecución.

No es necesario ejecutar código para completar la lectura de la lección.

## Licencias diferenciadas

- Programa `analisis.py` y código de las celdas: [MIT](LICENSE).
- Texto explicativo y datos sintéticos originales: [CC BY 4.0](../../LICENSE.md).

No se reutiliza código de RAPID ni datos de Zenodo. Es un ejemplo independiente.
