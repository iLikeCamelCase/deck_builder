#import genanki
from genanki import Note, Deck, Model, Card, Package
import random

basic_model = Model(
    random.randrange(1 << 30, 1 << 31),
    'Basic Model',
    fields=[
        {'name': 'To Learn'},
        {'name': 'Known'},
    ],
    templates=[
        {'name': 'Card 1',
        'qfmt': '{{To Learn}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Known}}',},
    ]
)

def create_notes(word_list: list[(str,str)]) -> list[Note]:
    """ creates a list of notes, front being the word in the language of study,
    the rear being it's translation

    Args:
        word_list (list[(str,str)}): list of tuples (front word, rear word) 

    Returns:
        list[Note]: list of anki notes returned
    """
    note_list = []
    for word in word_list:
        note_list.append(Note(
            model=basic_model,
            fields=[word[0],word[1]]
        ))

    return note_list

def create_deck(note_list: list[Note], deck_name: str) -> Deck:
    """ creates and anki deck from a given list of notes

    Args:
        note_list (list[Note]): list of notes
        deck_name (str): deck name

    Returns:
        Deck: anki deck
    """
    my_deck = Deck(
        random.randrange(1 << 30, 1 << 31),
        deck_name
    )
    for note in note_list:
        my_deck.add_note(note)

    return my_deck

def write_deck_to_file(path: str, deck: Deck) -> None:
    """ creates actual .apkg file from the Deck object

    Args:
        path (str): path to store file
        deck (Deck): deck object
    """
    my_package = Package(deck)
    my_package.write_to_file(path + deck.name + '.apkg')

def word_list_to_file(word_list: list[(str,str)], path: str, deckname: str) -> None:
    """ given list of tuples, creates notes from them, creates deck and 
    publishes to .apkg file

    Args:
        word_list (list[(str,str)]): tuple list (original, translated)
        path (str): path for file to be stored
    """
    note_list = create_notes(word_list)
    deck = create_deck(note_list, deckname)
    write_deck_to_file(path, deck)