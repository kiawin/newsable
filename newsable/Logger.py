import logging


class Logger():
    
    def __init__(self, news):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self._fileHandler = logging.FileHandler('../logs/'+news+'.log')
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._fileHandler.setFormatter(self._formatter)
        self.logger.addHandler(self._fileHandler)
        
    def get(self):
        return self.logger