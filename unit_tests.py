from Filter_File import TipoFile
from Filter_File import Crea_dizionario_tipi, Convert_Tabella_Dict
import unittest

class TestSetUpFilter(unittest.TestCase):

    def test_classe_tipo_rifiuta_un_istanza_senza_tipo_stringa(self):
        a = TipoFile(5)

        self.assertNotIsInstance(a, TipoFile, "Instance has being created without string parameter")

    def test_classe_tipo_accetta_un_istanza_con_stringa(self):
        a = TipoFile('Ciao')
        self.assertEqual(a.type, 'Ciao', f'il tag del tipo è "{a.type}"')

    def test_crea_dizionario_crea_un_dizionario(self):

        Lista = [("StringaEsempio1", "TagEsempio1"),("StringaEsempio2", "TagEsempio2"),("StringaEsempio3", "TagEsempio3")]
        D = Crea_dizionario_tipi(Lista)
        self.assertEqual(D["StringaEsempio1"], "TagEsempio1", f'Invece che TagEsempio1, {D["StringaEsempio1"]}')
        self.assertEqual(D["StringaEsempio2"], "TagEsempio2", f'Invece che TagEsempio2, {D["StringaEsempio2"]}')
        self.assertEqual(D["StringaEsempio3"], "TagEsempio3", f'Invece che TagEsempio3, {D["StringaEsempio3"]}')

    def test_convertInDict_works(self):
        Dict = Convert_Tabella_Dict('Prova.csv')

        self.assertEqual(Dict['1'], 'Uno')
        self.assertEqual(Dict['3'], 'Tre')




if __name__ == '__main__':
    unittest.main()

