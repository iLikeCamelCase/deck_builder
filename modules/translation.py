from deep_translator import GoogleTranslator

def translate_list_words(word_list: list[str], src: str, dest: str) -> list[(str,str)]:
    translated = GoogleTranslator(source=src,target=dest).translate_batch(word_list)
    tuple_list = []

    for i in range(len(word_list)):
        if word_list[i] != '':
            tuple_list.append((word_list[i],translated[i]))

    return tuple_list