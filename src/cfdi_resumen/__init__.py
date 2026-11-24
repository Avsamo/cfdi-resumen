from pathlib import Path
import os
from .lector import leer_cfdi 
import argparse
import pandas as pd
base_dir = Path(__file__).resolve().parents[2]


def procesar_carpeta(carpeta,nombre_archivo_salida):
    ruta_final = Path(carpeta)
    resultados = {}
    all_dicts = {}
    emisores_totales = {}
    for archivo in ruta_final.iterdir():
        nombre_archivo = str(archivo)
        nombre_archivo = nombre_archivo.split("/")[-1]
        #aqui cada ruta de archivo se manda a lector.py
        dict_archivo = leer_cfdi(archivo)
        total = dict_archivo["Total"]
        resultados[nombre_archivo] = total
        all_dicts[nombre_archivo] = dict_archivo

        if "Nombre_emisor" in dict_archivo.keys(): #aqui va la suma de todas las facturas por emisor, subtotal, iva y total de todas esas facturas
            emisor = dict_archivo["Nombre_emisor"]
            subtotal = dict_archivo["SubTotal"]
            iva = dict_archivo["TotalImpuestosTrasladados"]
            total = dict_archivo["Total"]
            if emisor in emisores_totales.keys():
                emisores_totales[emisor]["SubTotal"] += subtotal
                emisores_totales[emisor]["TotalImpuestosTrasladados"] += iva
                emisores_totales[emisor]["Total"] += total
            else:
                emisores_totales[emisor] = {"SubTotal": subtotal, "TotalImpuestosTrasladados": iva, "Total": total}
        print("\n")
    for key, valor in resultados.items():
        print(f"archivo: {key}, total: {valor}")

    all_dicts_df = pd.DataFrame.from_dict(all_dicts, orient='index')
    emisores_totales_df = pd.DataFrame.from_dict(emisores_totales, orient='index')

    with pd.ExcelWriter(os.path.join(base_dir, nombre_archivo_salida)) as writer:
        all_dicts_df.to_excel(writer, sheet_name='Facturas', index=True)
        emisores_totales_df.to_excel(writer, sheet_name='Emisores', index=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ruta", default=Path("datos"),type=Path)
    parser.add_argument("--salida", default=Path("salidas/resumen.xlsx"), type=Path)
    args = parser.parse_args()
    ruta_carpeta = ""
    if args.ruta:
        ruta_carpeta = os.path.join(base_dir, args.ruta)
    else:
        ruta_carpeta = os.path.join(base_dir, "datos")
    procesar_carpeta(ruta_carpeta, args.salida)
