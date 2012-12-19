import logging

class Logger():
    
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        self._fileHandler = logging.FileHandler('theStar.log')
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._fileHandler.setFormatter(self._formatter)
        self._logger.addHandler(self._fileHandler)
        
    def get(self):
        return self._logger