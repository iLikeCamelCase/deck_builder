from googletrans import Translator


def translate_list_words(word_list: list[str], src: str, dest: str) -> list[(str,str)]:
    """ translates a list of individual words, to avoid repitition parse list 
    and delete duplicates beforehand

    Args:
        word_list (list[str]): list of words to be translated
        src (str): source language (see googletrans documentation for language
        symbols)
        dest (str): destination language

    Returns:
        list[(str,str)]: list of word tuples (original, translated)
    """
    translator = Translator()
    translated_word_list = translator.translate(word_list, dest=dest, src=src)

    return_list = []

    for i in range(len(word_list)):
        return_list.append((word_list[i],translated_word_list[i]))

    return return_list