import xml.etree.ElementTree as ET
from pathlib import Path
import os
from decimal import Decimal
base_dir = Path(__file__).resolve().parents[2]

valores_a_buscar = ["UUID","Fecha","Rfc","Nombre","SubTotal","Total","TotalImpuestosTrasladados"]

def leer_cfdi(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    temp_dict = {}
    for values in root.iter():
        temp_dict[values.tag.split("}")[1]] = values.attrib
    
    final_dict = {}
    for main_key in temp_dict:
        for sub_key in temp_dict[main_key]:
            if sub_key in valores_a_buscar:
                string = sub_key
                if main_key == "Emisor":
                    string = sub_key + "_emisor"     
                elif main_key == "Receptor":
                    string = sub_key + "_receptor"
                
                value = temp_dict[main_key][sub_key]
                try:
                    value = Decimal((value))
                except Exception as e:
                    value = temp_dict[main_key][sub_key]
                final_dict[string] = value

    return final_dict    
    
ruta = os.path.join(base_dir,"datos/ejemplos/factura_001.xml")
result = leer_cfdi(ruta)
for value in result:
    print(value+":",result[value])




