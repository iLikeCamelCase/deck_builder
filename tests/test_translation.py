from modules.translation import translate_list_words

def test_translate_list_words():
    to_translate = ['Chat', 'Soleil', 'Livre', 'Maison', 'Pomme', 'Avion',
                    'Musique', 'Jardin', 'Heureux', 'Plage']
    
    translated = [
        ('Chat','Cat'),
        ('Soleil', 'Sun'),
        ('Livre','Book'),
        ('Maison','Home'),
        ('Pomme','Apple'),
        ('Avion','Plane'),
        ('Musique','Music'),
        ('Jardin','Garden'),
        ('Heureux','Happy'),
        ('Plage','Beach')
    ]

    assert translate_list_words(to_translate, dest='en', src='fr') == translated