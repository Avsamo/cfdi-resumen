from pathlib import Path
import os
from .lector import leer_cfdi 

base_dir = Path(__file__).resolve().parents[2]
ruta_carpeta = os.path.join(base_dir,"datos")

def procesar_carpeta(carpeta):
    ruta_final = Path(carpeta)
    resultados = {}
    for archivo in ruta_final.iterdir():
        nombre_archivo = str(archivo)
        nombre_archivo = nombre_archivo.split("/")[-1]
        #aqui cada ruta de archivo se manda a lector.py
        dict_archivo = leer_cfdi(archivo)
        total = dict_archivo["Total"]
        resultados[nombre_archivo] = total
        print("\n\n")
    for key, valor in resultados.items():
        print(f"archivo: {key}, total: {valor}")

def main() -> None:
    procesar_carpeta(ruta_carpeta)
