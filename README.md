# proyecto-claude-code

Herramienta de análisis de control de calidad para muestras de laboratorio, escrita en Python.

## Sobre este proyecto

Este proyecto es un ejercicio de control de calidad de laboratorio con manejo de errores en Python, pensado como parte de un portafolio de ingeniería química aplicada a IA. Simula la evaluación de pureza de muestras de reactivos, mostrando un flujo básico pero robusto: datos de ejemplo, lógica de aprobación/rechazo, validación de datos inválidos o fuera de rango, y un reporte final en formato de tabla.

## Contenido

- `control_calidad.py`: evalúa una lista de muestras (id, reactivo y pureza) y genera un reporte indicando si cada una está **APROBADA**, **RECHAZADA** o presenta **ERROR** (dato de pureza inválido o fuera del rango 0-100). Al final muestra un resumen con los totales.
- `saludo.py`: script de ejemplo que imprime un mensaje de saludo.

## Uso

```bash
python control_calidad.py
```

## Convenciones

- El código debe estar comentado en español.
