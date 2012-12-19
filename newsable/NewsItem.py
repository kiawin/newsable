from datetime import datetime
from newsable import MongoDB

class NewsItem(MongoDB):
    def __init__(self, dbname='test', colname='posts'):
        '''
        Constructor for NewsItem
        '''
        self.dbname = dbname
        self.colname = colname
        super().__init__(self.dbname, self.colname)
        ''' Instance variables '''
        self.newsItem = {}
    
    def addNewsItem(self, url, content):
        self.newsItem['url'] = url
        self.newsItem['content'] = content
    
    def insertNewsItem(self):
        modified = datetime.now()
        r = super().set({"url": self.newsItem['url']},{"content": str(self.newsItem['content']), "modified": modified})
        return r
    
    def resetNewsItem(self):
        self.newsItem = {}