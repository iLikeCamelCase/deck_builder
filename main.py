import file_reading as fr
import translation2 as tr
import deck_builder as db

def create_deck_from_file(file: str, filetype: str, source: str, dest: str,
                          deckname: str, path: str) -> None:
    
    match filetype:
        case 'pdf':
            reader = fr.ReadPDF('uploads/'+file)
        case 'docx':
            #TODO docx
            raise ValueError(f"Unsupported file type: {filetype}")
        case 'txt':
            #TODO txt
            raise ValueError(f"Unsupported file type: {filetype}")
        case '.rtf':
            #TODO rtf
            raise ValueError(f"Unsupported file type: {filetype}")
        case _:
            raise ValueError(f"Unsupported file type: {filetype}")
        
    ordered_word_list = reader.ordered
    print(type(ordered_word_list))
    translated_tuple_list = tr.translate_list_words(ordered_word_list, source, dest)
    #print(translated_tuple_list)
    print('Translated!')
    # create anki deck file from tuple list
    db.word_list_to_file(translated_tuple_list, path, deckname)
    print('Done Deck!')


if __name__ == '__main__':
    create_deck_from_file('test.pdf','pdf','fr','en',
                          'Plan de cours','created/')