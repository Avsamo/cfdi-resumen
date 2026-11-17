import xml.etree.ElementTree as ET
from pathlib import Path
import os
from decimal import Decimal
import random 
import string
import datetime


base_dir = Path(__file__).resolve().parents[1]
ruta_template = os.path.join(base_dir,"ejemplos/factura_001.xml")
ruta_salida = os.path.join(base_dir,"ejemplos/")


#dos ejemplos generados con otros nombres de emisores
facturas_emisores_diferentes = ["amoGithub","odioGithub"]

def leer_template(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    temp_dict = {}
    for values in root.iter():
        temp_dict[values.tag.split("}")[1]] = values.attrib
    
    final_dict = {}
    for main_key in temp_dict:
        for sub_key in temp_dict[main_key]:
            if sub_key == "Fecha":
                fecha = str(datetime.datetime.now()).split(" ")
                temp_dict[main_key][sub_key] = fecha[0] + "T" + fecha[1] 

            #dos diferentes emisores
            for emisores in facturas_emisores_diferentes:
                random_string = None
                if main_key == "Emisor":
                    if sub_key == "Rfc":
                        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
                        temp_dict[main_key][sub_key] = str(random_string.upper() + str(random.randint(10000,99999)) + random_string.upper())
                        tree.write(ruta_salida + f"factura_{random_string}.xml", encoding="utf-8", xml_declaration=True)
            #sin impuestos
            total = None
            if sub_key == "Total":
                impuesto_template = Decimal(temp_dict["Impuestos"]["TotalImpuestosTrasladados"]) 
                total_antes = Decimal(temp_dict[main_key][sub_key])
                temp_dict[main_key][sub_key] = str(total_antes-impuesto_template)
            elif main_key == "Traslado" and sub_key == "Importe":
                temp_dict[main_key][sub_key] = "0"
                temp_dict["Impuestos"]["TotalImpuestosTrasladados"] = "0"
                tree.write(ruta_salida + f"factura_Sin_iva_{random.randint(1,99999)}.xml", encoding="utf-8", xml_declaration=True)

leer_template(ruta_template)