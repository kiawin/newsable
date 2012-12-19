#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.MalaysiaKini import MalaysiaKiniNewsSource

class MalaysiaKini(News):
    """ Class for MalaysiaKini News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect("news")
        
        self.default_url_prefix = 'http://www.malaysiakini.com'
        self.default_expression = 'div.browseRows ul li.browseRowHeadline a'
        self.default_language = 'zsm'
        self.config = {
                     'nation-bm': {
                                   'url':'http://www.malaysiakini.com/browse/my_news',
                                   'tags': ['nation'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'columns-bm': {
                                    'url': 'http://www.malaysiakini.com/browse/my_columns',
                                    'tags': ['opinion'],
                                    'language': self.default_language,
                                    'expr': self.default_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'letters-bm': {
                                    'url': 'http://www.malaysiakini.com/browse/my_letters',
                                    'tags': ['opinion'],
                                    'language': self.default_language,
                                    'expr': self.default_expression,
                                    'url_prefix': self.default_url_prefix
                                    }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = MalaysiaKiniNewsSource(
                                                     url=self.config[self.news_category]['url_prefix']+url,
                                                     category=self.news_category,
                                                     tags=self.config[self.news_category]['tags'],
                                                     language=self.config[self.news_category]['language']
                                                     )
                newsSources.save()
            except OperationError:
                """ Error raised when url exist in collection """
                pass
    
    def purge(self):
        """ Purge the collection """
        
        newsSources = MalaysiaKiniNewsSource()
        newsSources.drop_collection()
    
if __name__ == '__main__':
    mkini = MalaysiaKini()
    mkini.list('nation')
    urls = mkini.news_urls
    print len(urls)
    for url in urls:
        print url
    mkini.save()