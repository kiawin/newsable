#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.TheSelangorTimes import TheSelangorTimesNewsSource

class TheSelangorTimes(News):
    """ Class for TheSelangorTimes News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = ''
        self.default_expression = 'h2.post-title a'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://www.theselangortimes.com.my/portal/category/nation/',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'nation-bm': {
                                   'url': 'http://www.theselangortimes.com.my/portal/category/bahasa-malaysia/',
                                   'tags': ['nation'],
                                   'language': 'zsm',
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'business': {
                                  'url': 'http://www.theselangortimes.com.my/portal/category/business/',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'ge13': {
                              'url': 'http://www.theselangortimes.com.my/portal/category/towards-ge-13/',
                              'tags': ['ge13','politics'],
                              'language': self.default_language,
                              'expr': self.default_expression,
                              'url_prefix': self.default_url_prefix
                              },
                     'opinion': {
                                 'url': 'http://www.theselangortimes.com.my/portal/category/opinion/',
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
                newsSources = TheSelangorTimesNewsSource(
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
        
        newsSources = TheSelangorTimesNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    tst = TheSelangorTimes()
    tst.list('nation')
    urls = tst.news_urls
    print len(urls)
    for url in urls:
        print url
    tst.save()