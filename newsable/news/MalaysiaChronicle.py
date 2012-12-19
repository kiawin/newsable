#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.MalaysiaChronicle import MalaysiaChronicleNewsSource

class MalaysiaChronicle(News):
    """ Class for MalaysiaChronicle News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.malaysia-chronicle.com'
        self.default_expression = 'div.catItemBody div.catItemTitle a'
        self.default_language = 'eng'
        self.config = {
                     'politics': {
                                  'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=12&Itemid=2',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'business': {
                                  'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=13&Itemid=3',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'social': {
                                  'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=14&Itemid=4',
                                  'tags': ['social','metro'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'featured': {
                                   'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=11&Itemid=10',
                                   'tags': ['features','special'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = MalaysiaChronicleNewsSource(
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
        
        newsSources = MalaysiaChronicleNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    malaysiaChronicle = MalaysiaChronicle()
    malaysiaChronicle.list('nation')
    urls = malaysiaChronicle.news_urls
    print len(urls)
    for url in urls:
        print url
    malaysiaChronicle.save()