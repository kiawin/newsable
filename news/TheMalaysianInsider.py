#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.TheMalaysianInsider import TheMalaysianInsiderNewsSource

class TheMalaysianInsider(News):
    """ Class for TheMalaysianInsider News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useXPath(self)
        connection.connect('news')
        
        self.default_url_prefix = ''
        self.default_expression = '//div[@class=\'sectionNews\']/h1/a | //div[@class=\'borderless\']/div[@class=\'bordered\']/h3/a | //div[@id=\'left\']/ul/li/a | //div[@id=\'center\']/ul/li/a | //div[@id=\'right\']/ul/li/a'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://www.themalaysianinsider.com/malaysia',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'business': {
                                  'url': 'http://www.themalaysianinsider.com/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'bahasa': {
                                'url': 'http://www.themalaysianinsider.com/bahasa',
                                'tags': ['nation'],
                                'language': 'ms',
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'opinion': {
                                 'url': 'http://www.themalaysianinsider.com/opinion',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 'expr': '//div[@class=\'items\']/div[@class=\'item\']/div[@class=\'title\']/a | //div[@class=\'main\']/div[@class=\'title\']/a',
                                 'url_prefix': self.default_url_prefix
                                 }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = TheMalaysianInsiderNewsSource(
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
        
        newsSources = TheMalaysianInsiderNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    tmi = TheMalaysianInsider()
    tmi.list('business')
    urls = tmi.news_urls
    print len(urls)
    for url in urls:
        print url
    tmi.save()