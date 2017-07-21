import os
import xml.etree.ElementTree
import glob
from lxml import etree




PATH = "/home/elmaster/project/datawarehouse/"

def get_list_file(directory):
    """
    Etant donne un directory la fonction
    retourne une liste de tous les fichier
    .ktr ou .kjb
    """
    list_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ktr') or file.endswith('.kjb'):
                list_files.append(str(os.path.join(root, file)))
    return list_files

def parse_documentation(file):

    root = etree.parse(pdi_file).getroot()

    # Extraction du nom des etapes
    list_steps = []
    list_descriptions = []
    for step in root.findall("step"):

        step_name = step.find("name").text
        step_description = "Description non-disponible"
        if step.find("description").text:
            step_description = step.find("description").text
        list_steps.append(step_name)
        list_descriptions.append(step_description)

    # Concatenner steps et la description correspondante
    list_step_descripton = [": ".join(list(i)) for i in zip(list_steps, list_descriptions)]

    # Extraction du Notes contextuelles
    list_notepads = []
    notepads = root.find("notepads")
    for notepad in notepads.findall("notepad"):
        list_notepads.append((notepad.find("note").text))

    return list_step_descripton, list_notepads


# pdi_file = '/home/elmaster/project/datawarehouse/dimension/dim1/etl/tr_dim1.ktr'

all_pdi_file = get_list_file(PATH)

for pdi_file in all_pdi_file:

    # Extraire nom de la transformation/job sans l'extension
    transfo = pdi_file.split("/")[-1].split(".")[0]
    print("Generation de la documentation pour fichier {}".format(transfo))

    # Parse documentation from xml file
    steps, notepads = parse_documentation(pdi_file)

    template = """
Documentation - {code}
************************

Image: 
===================
.. image:: tr_dim1.png

Etapes: 
===================
- {etapes}

Notes Contextuelles: 
===================
{note}
""".format(code = transfo,
       etapes = "\n- ".join(steps),
       note  = "\n".join(notepads))

    # Exporter la documentation dans le folder de documentation
    with open(os.path.join(PATH, "documentation", "{0}.rst".format(transfo)), "w") as doc_file:
        doc_file.write(template)


