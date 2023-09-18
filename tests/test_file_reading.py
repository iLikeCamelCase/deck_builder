from file_reading import Read, ReadPDF
import os
 
def test_ReadPDF_raw():
    file_path = os.path.abspath('test.pdf')
    read = ReadPDF(file_path)
    good_raw_list = ['Chat', 'Chat', 'Chat', 'Soleil', 'Soleil', 'Livre',
                     'Maison', 'Pomme', 'Pomme', 'Pomme', 'Pomme', 'Avion',
                     'Musique', 'Jardin', 'Heureux', 'Plage', '2012', '1', '+',
                     '2', '=', '3']
    
    assert read.raw == good_raw_list

def test_ReadPDF_processed():
    file_path = os.path.abspath('test.pdf')
    read = ReadPDF(file_path)
    good_processed_list = [ 'Chat', 'Chat', 'Chat', 'Soleil', 'Soleil',
                            'Livre', 'Maison', 'Pomme', 'Pomme', 'Pomme',
                            'Pomme', 'Avion', 'Musique', 'Jardin', 'Heureux',
                            'Plage']

    assert read.processed == good_processed_list

def test_ReadPDF_ordered():
    file_path = os.path.abspath('test.pdf')
    read = ReadPDF(file_path)
    
    first_three = ['Pomme', 'Chat', 'Soleil']
    
    assert read.ordered[:3] == first_three