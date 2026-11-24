# CFDI Resumen

Herramienta de línea de comandos que lee archivos **CFDI (Comprobantes Fiscales Digitales por Internet)**, es decir, facturas electrónicas en formato XML, y muestra de forma clara los datos de cada factura. Su objetivo es consultar rápidamente la información de cada comprobante sin tener que abrir y revisar cada XML a mano.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/) para ejecutar el proyecto
- No requiere dependencias externas: solo usa la biblioteca estándar de Python.

## Instalación

Clona el repositorio y entra a la carpeta del proyecto:

```bash
git clone https://github.com/Avsamo/cfdi-resumen.git
cd cfdi-resumen
```

## Uso

1. Coloca tus archivos XML en la carpeta `datos/`.
2. Desde la terminal, en la carpeta del proyecto, ejecuta:

```bash
uv run cfdi-resumen
```

El programa leerá automáticamente todos los XML de la carpeta `datos/` y mostrará los datos de cada factura.

con la nueva implementacion de excel y argumentos de linea de comandos, se incluyen --ruta (la cual te permite seleccionar la carpeta de donde quieres extraer nuevos datos dentro de cfdi-resumen) y --salida (la cual permite seleccionar una ruta para generar un xlsx con la informacion extraida de los documentos)

algunos ejemplos son:

```bash
uv run cfdi-resumen --ruta datos
uv run cfdi-resumen --ruta ejemplos --salida salida/resumen.xlsx
```

donde la carpeta "salida" fue creada anteriormente