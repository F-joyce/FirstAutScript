import csv


# Funzione che filtra i file e dice questo file è di questo tipo quindi usa questa funzione
# Quindi mi serve una lista di tuples che collegano stringa con tipo
# Una funzione che da questa lista crea un dizionario
# Una funzione il cui input e un file e l'output un tipo
# Una funzione che collega tipo a funzione
import os

""""Questa lista collega delle stringhe che identificano il nome del file col suo tipo, per inserire un nuovo tipo di file
inserire una parentesi, il cui primo elemento è una stringa, e il secondo elemento un tag identificativo di un tipo"""
LISTA_TIPI_FILE = [("StringaEsempio1", "TagEsempio1"),("StringaEsempio2", "TagEsempio2"),("StringaEsempio3", "TagEsempio3")]

RELATIVE_PATH_FILE = "Prova.csv"

class TipoFile(object):
    def __init__(self, tipo):
        assert type(tipo) == str, f"{tipo} must be a string"
        self.type = tipo

def Convert_Tabella_Dict(stringname = RELATIVE_PATH_FILE):
    with open(stringname, 'r') as file:
        reader = csv.reader(file)
        d = dict(reader)
    return d

def FilterFiles(filename, Dict = Convert_Tabella_Dict()):
    for identifier in Dict:
        if identifier in filename:
            break
    return (filename, Dict[identifier])

def FilterIterator(folder_path):
    List = []
    for file in os.listdir(folder_path):
        filename = os.fsdecode(file)
        List.append(FilterFiles(filename))

    return List

