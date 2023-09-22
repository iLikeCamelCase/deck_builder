import logging
import PyPDF2
from abc import ABC

VALID_FILE_TYPES = []

class Read(ABC):
    """
    Abstract class to read documents. Child classes must instantiate read_file()
    method. Child classes should be specific to file type being read, e.g. word,
    pdf, epub
    """
    def __init__(self, file: str):
        self.file: str = file
        self.raw: list[str] = self.read_file(self.file)
        self.processed: dict[str,int] = self.first_level_filtering(self.raw)
        self.ordered: list[str] = self.rank_by_occurence(self.processed)
        pass
    
    @staticmethod
    def is_valid_file(file: str) -> bool:
        """ Returns if given file is a valid type for reading

        Args:
            file (str): file path

        Returns:
            bool: able to be read
        """
        return '.' in file and \
        file.rsplit('.', 1)[1].lower() in VALID_FILE_TYPES
    
    def read_file(self, file: str) -> list[str]:
        """ Returns raw text read from file
        
        Abstract method, must be instantiated in child class depending on file-
        type

        Args:
            file (str): location of file to be read

        Returns:
            list[str]: raw text of file split at spaces
        """
        pass
        
    def first_level_filtering(self, raw: list[str]) -> dict[str,int]:
        """ filters raw word data
        - removes words with numbers
        - removes words with certain characters [@#$%^&*+=]
        - removes certain characters from words [[]()'":;,.!]
        - words made lowercase
        
        also counts occurence 
        #TODO deal with hypenated words, contracted words, acryonyms 

        Args:
            raw (list[str]): file text split at spaces

        Returns:
            dict[str,int]: filtered text, keys are (hopefully real) words,
                        values are amount of time that word was found
        """
        
        processed = {}
        NAUGHTY = '0123456789@#$%^&*+=-_–'
        MILDLY_NAUGHTY = '[]()\'":;,.!/\\|'
        
        for word in raw:
            remove_word = False
            remove_these = {}
            for char in word:
                if char in NAUGHTY:
                    # remove word
                    remove_word = True
                elif char in MILDLY_NAUGHTY:
                    # list chars to remove
                    remove_these[char]=None
            if remove_word:
                continue
            else:
                for key in remove_these:
                    word = word.replace(key,'')

                if word.lower() not in processed:
                    processed[word.lower()] = 0

                processed[word.lower()] += 1
        
        return processed

    def rank_by_occurence(self, processed: dict[str,int]) -> list[str]:
        """ takes dict of words and their rate of occurence, returns list of words
        in order based on rate of occurence

        Args:
            processed (dict[str,int]): dict of words/occurence rate 

        Returns:
            list[str]: list of unique words in order of occurence
        """
        tuple_list = list(processed.items())
        tuple_list.sort(key= lambda x: x[1], reverse= True)
        word_list = []
        for tuple in tuple_list:
            word_list.append(tuple[0])
        return word_list
                
class ReadPDF(Read):
    
    def __init__(self, file:str):
        super().__init__(file)
                    
    def read_file(self, file:str) -> list[str]:
        """reads (PDF) file and returns list of (possible) words. basically splits
        raw text at whitespace

        Args:
            file (str): file path

        Returns:
            list[str]: list of raw text split at whitespace
        """
        pdf_file_object = open(file, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_object)
        raw_word_list = []
        page_number = 0
        still_pages = True
        #while still_pages:
            #try:
                #page_obj = pdf_reader.pages[page_number]
                #page_text = page_obj.extract_text()
                #raw_word_list.extend(page_text.split())
            #except:
                #still_pages = False
                #pass
            
            #page_number += 1

        # TESTING PURPOSES, JUST ONE PAGE AT A TIME
        page_obj = pdf_reader.pages[0]
        page_text = page_obj.extract_text()
        raw_word_list.extend(page_text.split())

        return raw_word_list
    
class ReadTXT(Read):
    def __init__(self, file:str):
        super().__init__(file)

    def read_file(self, file: str) -> list[str]:
        with open(file,'r') as file:
            file_contents = file.read()

        return file_contents.split()