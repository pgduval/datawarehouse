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


files = get_list_file(PATH)
print(files)

for root, dirs, files in os.walk(PATH):
    if "doc" in root:
        print(root)
    for file in files:
        if file.endswith('.ktr') or file.endswith('.kjb'):
            list_files.append(str(os.path.join(root, file)))



pdi_file = '/home/elmaster/project/datawarehouse/dimension/dim1/etl/tr_dim1.ktr'

root = etree.parse(pdi_file).getroot()

# Extraction du nom des etapes
list_steps = []
list_descriptions = []
for step in root.findall("step"):

    step_name = step.find("name").text
    step_description = ""
    if step.find("description").text:
        step_description = step.find("description").text
    list_steps.append(step_name)
    list_descriptions.append(step_description)

print(list_steps)


# Extraction du Notes contextuelles
list_notepads = []
notepads = root.find("notepads")
for notepad in notepads.findall("notepad"):
    list_notepads.append((notepad.find("note").text))

template = """
Documentation fonctionnelle - {code}
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
""".format(code = pdi_file.split("/")[-1],
           etapes = "\n- ".join(list_steps),
           note  = "\n".join(list_notepads))

print(template)
with open(os.path.join(PATH, "documentation", "doc_fonctionelle.rst"), "w") as doc_file:
    doc_file.write(template)


