#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.MySinchew import MySinchewNewsSource

class MySinchew(News):
    """ Class for MySinchew News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.mysinchew.com'
        self.default_expression = 'h4.title.teaser a#title'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://www.mysinchew.com/taxonomy/term/4',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'opinion': {
                                  'url': 'http://www.mysinchew.com/taxonomy/term/12',
                                  'tags': ['opinion'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro-mykampung': {
                                  'url': 'http://www.mysinchew.com/taxonomy/term/102',
                                  'tags': ['metro'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'features': {
                                  'url': 'http://www.mysinchew.com/taxonomy/term/10',
                                  'tags': ['features','special'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'business': {
                                   'url': 'http://www.mysinchew.com/taxonomy/term/121',
                                   'tags': ['business'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = MySinchewNewsSource(
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
        
        newsSources = MySinchewNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    mysinchew = MySinchew()
    mysinchew.list('nation')
    urls = mysinchew.news_urls
    print len(urls)
    for url in urls:
        print url
    mysinchew.save()