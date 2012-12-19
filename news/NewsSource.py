from datetime import datetime
from news import MongoDB

class NewsSource(MongoDB):
    def __init__(self, dbname='test', colname='posts'):
        '''
        Constructor for NewsSource
        '''
        self.dbname = dbname
        self.colname = colname
        super().__init__(self.dbname, self.colname)
        ''' Instance variables '''
        self.newsItems = []
    
    def findEmptyNewsItem(self):
        '''
        Find one news source without content
        '''
        r = super().findOne({'content': {'$exists': False}})
        #print(str(r))
        return r
    
    def addNewsSource(self, url, title, category, tags, language):
        '''
        Append news source to instance variable
        '''
        modified = created = datetime.now()
        newsItem = {'url': url, 'title': title, 'category': category, 'tags': tags, 'language': language, 'created': created, 'modified': modified}
        self.newsItems.append(newsItem)
        
    def insertNewsSources(self):
        '''
        Insert news source(s) into DB
        '''
        #if len(self.newsItems) is not 0:
        #print(str(self.newsItems))
        r = super().insert(self.newsItems)
        #self.newsItems = []
        return r

    def resetNewsSources(self):
        self.newsItems = []