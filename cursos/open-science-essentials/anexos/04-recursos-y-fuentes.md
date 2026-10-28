# Anexo 4A · Recursos y fuentes de los componentes

[← Lección 4](../lecciones/04-componentes-ciencia-abierta.md) · [🧪 Ejemplo práctico](../../../ejemplos/leccion-04/README.md) · [🏠 Inicio](../../../README.md)

**Revisión:** 28-10-2026. Los enlaces amplían el estudio; no son requisitos adicionales de Canvas. Se diferencia consulta de páginas, revisión de metadatos y ejecución de software.

## Empieza en español y compara idiomas

| Recurso | Idioma y formato | Qué aporta |
|---|---|---|
| [Open Data Handbook](https://opendatahandbook.org/guide/es/what-is-open-data/) | Español · texto web | Definición y criterios de datos abiertos |
| [La misma guía en inglés](https://opendatahandbook.org/guide/en/what-is-open-data/) | Inglés · texto web | Comparar terminología |
| [La misma guía en chino simplificado](https://opendatahandbook.org/guide/zh_CN/what-is-open-data/) | Chino · texto web | Ampliación multilingüe, no traducción de Canvas |
| [MetaDocencia](https://metadocencia.github.io/herramientas-de-ciencia-abierta-junio-2026/) | Español · lecciones | Refuerzo de ciencia abierta; recurso previamente comprobado |
| [Anexo de licencias](02-aspectos-legales-codigo-abierto.md) | Español · texto, imagen y ejercicios | Distinguir permisos de precio y visibilidad |

## Datos y software del ejemplo científico real

- [Registro de datos 3688691](https://zenodo.org/records/3688691): se revisaron por API título, tipo Dataset, DOI específico y DOI conceptual.
- [API pública del registro](https://zenodo.org/api/records/3688691): metadatos legibles por máquina; la página web no fue accesible mediante la herramienta de lectura, pero la API sí respondió.
- [FAQ de versiones de Zenodo](https://zenodo.org/help/versioning): diferencia entre DOI de versión y conceptual.
- [Artículo](https://doi.org/10.1175/JHM-D-19-0084.1): relación bibliográfica identificada; el sitio editorial devolvió 403.
- [RAPID](https://github.com/c-h-david/rapid): README revisado; no instalado ni ejecutado.

**Qué no demuestra la comprobación:** que se hayan validado las conclusiones del artículo o reproducido el modelo. El [paquete sintético propio](../../../ejemplos/leccion-04/README.md) es otro ejercicio.

## Metadatos y formatos

| Fuente primaria | Idioma / formato | Uso |
|---|---|---|
| [CF Conventions](https://cfconventions.org/) | Inglés · especificación y web | Variables y propiedades espacio-temporales |
| [WMO WIS2](https://community.wmo.int/en/activity-areas/wis/wis2-implementation) | Inglés · web | Intercambio meteorológico; apertura agotó el tiempo |
| [NASA OSDR](https://science.nasa.gov/biological-physical/data/osdr/) | Inglés · web | Repositorio y contexto de ciencias biológicas y físicas |
| [CSV, RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) | Inglés · documento | Formato tabular de texto y sus convenciones |
| [HDF5](https://www.hdfgroup.org/solutions/hdf5/) | Inglés · web técnica | Organización de conjuntos de datos |
| [netCDF](https://docs.unidata.ucar.edu/netcdf-c/current/) | Inglés · documentación | Datos multidimensionales |
| [FITS](https://fits.gsfc.nasa.gov/fits_standard.html) | Inglés · estándar | Datos astronómicos |

No se probaron conversiones entre estos formatos. La tabla completa nombres que faltaban en el fragmento recibido; no afirma recuperar una diapositiva original.

## Resultados y acceso abierto

| Recurso | Idioma / formato | Uso |
|---|---|---|
| [OSI: definición de código abierto](https://opensource.org/osd) | Inglés · definición | Derechos de redistribución, modificación y otros criterios |
| [The Open Source Way](https://opensource.com/open-source-way) | Inglés · texto | Transparencia, colaboración, iteración, perspectivas y comunidad |
| [The Turing Way: acceso abierto](https://book.the-turing-way.org/reproducible-research/open/open-access/) | Inglés · libro web | Rutas y contexto de publicación |
| [cOAlition S: diamante](https://www.coalition-s.org/diamond-open-access/) | Inglés · web | Publicación sin cobro a lectores ni autores |
| [Jupyter](https://jupyter.org/) | Inglés · documentación | Cuadernos con narración, código y salidas |
| [Jupyter Book](https://jupyterbook.org/) | Inglés · documentación | Narrativas y publicaciones computacionales |
| [R Markdown](https://rmarkdown.rstudio.com/) | Inglés · documentación | Documentos basados en narración y código |
| [Quarto](https://quarto.org/) | Inglés · documentación | Publicación computacional en varios formatos |
| [FORRT](https://forrt.org/) | Inglés · recursos de formación | Investigación abierta y reproducible |

Las páginas de herramientas se consultaron; no se instalaron ni se probaron sus flujos completos. El sitio de Project Binder no se pudo abrir en esta revisión; no se publica un botón que prometa una sesión preparada de este repositorio.

## Casos y referencias del curso

| Referencia | Qué se comprobó |
|---|---|
| [Copernicus EMS](https://mapping.emergency.copernicus.eu/about/) | Descripción del componente cartográfico con datos satelitales y otras fuentes |
| [NOAA: propagación de tsunamis](https://www.noaa.gov/jetstream/tsunamis/tsunami-propagation) | Velocidad dependiente de profundidad; corrige el error de unidades |
| [NASA: desastres y ciencia abierta](https://science.nasa.gov/open-science/artificial-intelligence-hurricane-response/) | Página localizada y consultada |
| [Hemphill et al., 2022](https://doi.org/10.1002/asi.24646) | Referencia aportada por el estudiante; texto íntegro no contrastado |
| [Guillemin et al., 2025](https://doi.org/10.1007/s11160-024-09906-7) | Referencia aportada; no se verifica un cambio normativo causado por el estudio |
| [Chan et al., 2019](https://doi.org/10.20381/ruor-24088) | Referencia aportada; caso de Beirut pendiente de contraste completo |
| [Maxmen, 2019](https://doi.org/10.1038/d41586-019-02258-4) | Título y contexto visible de República Democrática del Congo; texto completo restringido. No valida por sí solo la narración de África Occidental del fragmento |
| [El-Gebali, 2021](https://doi.org/10.5281/zenodo.4562630) | Referencia de taller aportada; materiales íntegros no revisados |
| [Publicaciones USGS](https://pubs.usgs.gov/) | Portal de referencia; no se selecciona ni valida aquí un informe concreto |

## Aprende con varios formatos

- **Ver:** diagramas de [componentes](../../../assets/leccion-04-componentes.svg), [metadatos](../../../assets/leccion-04-metadatos.svg) y [acceso abierto](../../../assets/leccion-04-acceso-abierto.svg).
- **Leer:** lección en español y fuentes por idioma.
- **Examinar:** CSV, diccionario, programa y resultados del ejemplo sintético.
- **Experimentar:** cuaderno Jupyter con salidas guardadas, ejecutable en un entorno compatible; GitHub muestra el contenido, pero no ejecuta celdas.
- **Escuchar:** guion textual de la lección para una función de voz del dispositivo, sin MP3 propio.
- **Recordar:** preguntas desplegables originales.

Las imágenes son originales del repositorio y no copias de ilustraciones NASA, Unsplash, Scriberia o Google Earth.

[← Lección 4](../lecciones/04-componentes-ciencia-abierta.md)
