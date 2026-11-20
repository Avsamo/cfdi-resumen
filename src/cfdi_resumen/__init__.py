from pathlib import Path
import os
from .lector import leer_cfdi 
import argparse

base_dir = Path(__file__).resolve().parents[2]


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
        print("\n")
    for key, valor in resultados.items():
        print(f"archivo: {key}, total: {valor}")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ruta", default=Path("datos"),type=Path)
    args = parser.parse_args()
    ruta_carpeta = ""
    if args.ruta:
        ruta_carpeta = os.path.join(base_dir, args.ruta)
    else:
        ruta_carpeta = os.path.join(base_dir, "datos")
    procesar_carpeta(ruta_carpeta)
