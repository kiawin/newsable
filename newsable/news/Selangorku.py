#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.Selangorku import SelangorkuNewsSource

class Selangorku(News):
    """ Class for Selangorku News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = ''
        self.default_expression = 'h3.entry-title a'
        self.default_language = 'zsm'
        self.config = {
                     'state': {
                                'url': 'http://www.selangorku.com/?cat=241',
                                'tags': ['state', 'selangor'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'mb-news': {
                                  'url': 'http://www.selangorku.com/?cat=11',
                                  'tags': ['state','selangor'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'mb-programme': {
                                  'url': 'http://www.selangorku.com/?cat=12',
                                  'tags': ['state', 'selangor'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'mb-politics': {
                                  'url': 'http://www.selangorku.com/?cat=54',
                                  'tags': ['state','selangor', 'politics'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                               }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = SelangorkuNewsSource(
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
        
        newsSources = SelangorkuNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    selangorku = Selangorku()
    selangorku.list('nation')
    urls = selangorku.news_urls
    print len(urls)
    for url in urls:
        print url
    selangorku.save()