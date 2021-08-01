#from Filter_File import TipoFile
#from Filter_File import Convert_Tabella_Dict, FilterFiles
import Filter_File as F
import unittest
import os

class TestSetUpFilter(unittest.TestCase):

    def test_classe_tipo_accetta_un_istanza_con_stringa(self):
        a = F.TipoFile('Ciao')

        self.assertEqual(a.type, 'Ciao', f'il tag del tipo è "{a.type}"')

    def test_convertInDict_works(self):
        Dict = F.Convert_Tabella_Dict('Prova.csv')

        self.assertEqual(Dict['1'], 'Uno')
        self.assertEqual(Dict['3'], 'Tre')

class FilterWorks(unittest.TestCase):


    def test_filter_one_file(self):
        a = F.FilterFiles('Prova_Filter_1.txt')
        self.assertEqual(a[0],'Prova_Filter_1.txt')
        self.assertEqual(a[1],'Uno')
        print(a)

    def test_filter_iterator(self):
        directory = 'Prova/'
        L = F.FilterIterator(directory)
        self.assertEqual(len(L), 3, f'Lenght of list is {len(L)}')
        print(L)










if __name__ == '__main__':
    unittest.main()

