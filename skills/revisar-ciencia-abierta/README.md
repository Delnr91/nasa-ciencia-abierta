# Revisar ciencia abierta · Guía de uso

[🏠 Proyecto](../../README.md) · [Instrucciones de la skill](SKILL.md) · [Fuentes](references/fuentes.md) · [Revisión del proyecto](REVISION.md)

Una skill es una carpeta de instrucciones que ayuda a un asistente a realizar una tarea. Esta guía orienta una **revisión de prácticas de ciencia abierta en software científico**: qué evidencia existe, qué falta y qué se puede mejorar.

**Estado:** primera versión educativa. El contenido se ha revisado estructuralmente; aún no existe una prueba de funcionamiento completa en cada asistente. El asistente puede equivocarse: revisa los hallazgos y sus fuentes.

## Qué revisa

| Tema | Pregunta |
|---|---|
| Datos y resultados | ¿Se conocen su origen, significado y versión? |
| Software | ¿Hay instrucciones, dependencias y evidencia para repetir el cálculo? |
| Licencias | ¿Están claros los permisos para código, datos y materiales ajenos? |
| FAIR | ¿Se pueden encontrar, acceder según corresponda, interpretar y reutilizar los datos? |
| Colaboración | ¿Se reconocen contribuciones y se explican límites de mantenimiento? |
| IA, cuando corresponda | ¿Se documentan finalidad, datos, evaluación, incertidumbre y responsables? |

Una revisión no certifica cumplimiento, seguridad o reproducibilidad. Los datos sensibles pueden requerir acceso restringido. No envíes archivos privados a un servicio externo sin autorización.

## Antes de instalar

1. En [la carpeta de la skill](https://github.com/Delnr91/nasa-ciencia-abierta/tree/main/skills/revisar-ciencia-abierta), revisa `SKILL.md` y `references/fuentes.md`.
2. Descarga o copia **toda la carpeta**, conservando la subcarpeta `references`. Desde GitHub puedes usar **Code → Download ZIP** y extraer el archivo.
3. Coloca la carpeta en la ubicación de tu herramienta. No reemplaces otra carpeta del mismo nombre sin revisar su contenido.
4. Abre o recarga tu asistente y comprueba si la detecta. Las rutas de abajo se refieren a las versiones de línea de comandos o agentes indicados; no se ha probado la instalación en este proyecto.

## Codex

Copia `revisar-ciencia-abierta/` a `~/.codex/skills/`. Inicia una sesión nueva y pide:

> Usa $revisar-ciencia-abierta para revisar este proyecto en modo de solo lectura. Indica evidencias, hallazgos y lo que no puedas verificar.

[Documentación de skills de OpenAI](https://developers.openai.com/plugins/concepts/skills). La ubicación personal se basa en las instrucciones de Codex usadas para preparar esta guía; verifica la configuración de tu instalación.

## Claude Code

Para tu cuenta, copia la carpeta a `~/.claude/skills/`; para un proyecto, a `.claude/skills/` dentro de ese proyecto. Solicita `/revisar-ciencia-abierta` y describe el alcance.

[Documentación oficial de Claude Code](https://code.claude.com/docs/en/skills). Claude Code es una herramienta distinta de la aplicación web Claude.

## Gemini CLI

Copia la carpeta a `.agents/skills/` en el proyecto y usa `/skills list` para comprobar si se detectó; `/skills reload` actualiza la lista. Luego solicita una revisión de ciencia abierta por nombre.

[Guía oficial de Gemini CLI](https://geminicli.com/docs/cli/skills/) y [tutorial de Google](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli?hl=en). Gemini CLI y la aplicación web Gemini pueden ofrecer capacidades distintas.

## GitHub Copilot

Para un repositorio, copia la carpeta a `.github/skills/`; para uso personal, la documentación también contempla `~/.copilot/skills/`. Pide al agente que use la skill y revisa el informe.

[Documentación oficial de GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills). La disponibilidad depende del producto y su configuración.

## Otros asistentes y uso manual

Si tu asistente admite carpetas con `SKILL.md`, consulta su documentación para localizar la carpeta correcta; no asumimos compatibilidad ni instalación automática. Si solo admite instrucciones, puedes leer los dos archivos y facilitar el texto pertinente, respetando privacidad y permisos. Comprueba cómo procesa referencias y archivos adjuntos.

## Ejemplo de resultado esperado

> **Observado:** el README del ejemplo sintético incluye un diccionario y resultados esperados.  
> **Pendiente de comprobar:** ejecutar el cálculo en un entorno independiente.  
> **Propuesta:** registrar versión, entorno y resultado de esa comprobación.

Este ejemplo describe el tipo de informe; no demuestra que una prueba se haya ejecutado.

## Licencia y atribución

Las instrucciones y documentación originales de la skill se comparten bajo [CC BY 4.0](../../LICENSE.md). El código del ejemplo de la lección 4 tiene su propia [licencia MIT](../../ejemplos/leccion-04/LICENSE). Los documentos y figuras de terceros conservan sus condiciones; consulta [procedencia](../../assets/docs/README.md).

Para reutilizar la skill, atribuye a Delnr91 y colaboradores, enlaza este repositorio y la licencia, e indica cambios. No sugieras respaldo de NASA, MIT u otra institución. El proyecto es educativo e independiente.

## Contribuir

Puedes proponer una corrección con un caso reproducible, explicar su impacto y enlazar la fuente. Consulta [cómo contribuir](../../CONTRIBUTING.md). No incluyas credenciales ni datos privados en una incidencia pública.
