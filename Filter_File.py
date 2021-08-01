import csv


# Funzione che filtra i file e dice questo file è di questo tipo quindi usa questa funzione
# Quindi mi serve una lista di tuples che collegano stringa con tipo
# Una funzione che da questa lista crea un dizionario
# Una funzione il cui input e un file e l'output un tipo
# Una funzione che collega tipo a funzione

""""Questa lista collega delle stringhe che identificano il nome del file col suo tipo, per inserire un nuovo tipo di file
inserire una parentesi, il cui primo elemento è una stringa, e il secondo elemento un tag identificativo di un tipo"""
LISTA_TIPI_FILE = [("StringaEsempio1", "TagEsempio1"),("StringaEsempio2", "TagEsempio2"),("StringaEsempio3", "TagEsempio3")]

PATH_FILE = "username/Esempio/Cartella"

class TipoFile(object):
    def __init__(self, tipo):
        assert type(tipo) == str, f"{tipo} must be a string"
        self.type = tipo

def Crea_dizionario_tipi(lista):
    TypesChecker = dict()
    for e in lista:
        TypesChecker[e[0]] = e[1]
    return TypesChecker

def Convert_Tabella_Dict(stringname):
    with open(stringname, 'r') as file:
        reader = csv.reader(file)
        d = dict(reader)
    return d