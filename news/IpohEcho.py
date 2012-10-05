#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.IpohEcho import IpohEchoNewsSource

class IpohEcho(News):
    """ Class for IpohEcho News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = ''
        self.default_expression = 'div.entry a'
        self.default_language = 'eng'
        self.config = {
                     'metro-ipoh': {
                                     'url': 'http://ipohecho.com.my/v2/',
                                     'tags': ['metro','north', 'ipoh'],
                                     'language': self.default_language,
                                     'expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                 }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = IpohEchoNewsSource(
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
        
        newsSources = IpohEchoNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    ipohEcho = IpohEcho()
    ipohEcho.list('nation')
    urls = ipohEcho.news_urls
    print len(urls)
    for url in urls:
        print url
    ipohEcho.save()