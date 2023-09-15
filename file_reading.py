import PyPDF2
from abc import ABC

class Read(ABC):
    def __int__(self, file: str):
        self.file = file
        self.raw = []
        self.processed = []
        pass
    
    @staticmethod
    def is_valid_file(self, file: str) -> bool:
        """ Returns if given file is a valid type for reading

        Args:
            file (str): file path

        Returns:
            bool: able to be read
        """
        pass
    
    def read_file(self, file: str) -> list[str]:
        """ Returns raw text read from file
        
        Abstract method, must be instantiated in child class depending on file-
        type

        Args:
            file (str): location of file to be read

        Returns:
            list[str]: raw text of file split at spaces
        """
        
    def first_level_filtering(self, raw: list[str]) -> list[str]:
        """ filters raw word data
        - removes words with numbers
        - removes words with certain characters [@#$%^&*+=]
        - removes certain characters from words [[]()'":;,.!]
        
        #TODO deal with hypenated words, contracted words, acryonyms 

        Args:
            raw (list[str]): file text split at spaces

        Returns:
            list[str]: filtered text (should only be made of real words)
        """
        
        processed = []
        NAUGHTY = '0123456789@#$%^&*+='
        MILDLY_NAUGHTY = '[]()\'":;,.!/\\|'
        
        for word in raw:
            for char in word:
                if char in NAUGHTY:
                    continue
                elif char in MILDLY_NAUGHTY:
                    