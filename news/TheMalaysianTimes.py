#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.TheMalaysianTimes import TheMalaysianTimesNewsSource

class TheMalaysianTimes(News):
    """ Class for TheMalaysianTimes News Scraper """ 
    
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
                                'url': 'http://www.themalaysiantimes.com.my/category/nation',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'nation-bm': {
                                   'url': 'http://www.themalaysiantimes.com.my/category/bahasa-malaysia',
                                   'tags': ['nation'],
                                   'language': 'zsm',
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'business': {
                                  'url': 'http://www.themalaysiantimes.com.my/category/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'ge13': {
                              'url': 'http://www.themalaysiantimes.com.my/category/ge13',
                              'tags': ['ge13','politics'],
                              'language': self.default_language,
                              'expr': self.default_expression,
                              'url_prefix': self.default_url_prefix
                              },
                     'education': {
                                   'url': 'http://www.themalaysiantimes.com.my/category/education',
                                   'tags': ['education'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'opinion': {
                                 'url': 'http://www.themalaysiantimes.com.my/category/opinion',
                                 'tags': ['opinion'],
                                 'language': 'und',
                                 'expr': self.default_expression,
                                 'url_prefix': self.default_url_prefix
                                 }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = TheMalaysianTimesNewsSource(
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
        
        newsSources = TheMalaysianTimesNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    tmt = TheMalaysianTimes()
    tmt.list('nation')
    urls = tmt.news_urls
    print len(urls)
    for url in urls:
        print url
    tmt.save()