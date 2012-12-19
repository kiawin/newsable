#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.Utusan import UtusanNewsSource

class Utusan(News):
    """ Class for Utusan News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.utusan.com.my'
        self.default_expression = 'div#ContentContainer div.summary div a'
        self.default_language = 'zsm'
        self.config = {
                     'nation': {
                                'url': 'http://www.utusan.com.my/utusan/Dalam_Negeri',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'politics': {
                                  'url': 'http://www.utusan.com.my/utusan/Politik',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'parliament': {
                                    'url': 'http://www.utusan.com.my/utusan/Parlimen',
                                    'tags': ['parliament'],
                                    'language': self.default_language,
                                    'expr': self.default_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'crime': {
                               'url': 'http://www.utusan.com.my/utusan/Jenayah',
                               'tags': ['crime','nation'],
                               'language': self.default_language,
                               'expr': self.default_expression,
                               'url_prefix': self.default_url_prefix
                               },
                     'courts': {
                                'url': 'http://www.utusan.com.my/utusan/Mahkamah',
                                'tags': ['courts'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'special': {
                                 'url': 'http://www.utusan.com.my/utusan/Laporan_Khas',
                                 'tags': ['special'],
                                 'language': self.default_language,
                                 'expr': self.default_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'business': {
                                  'url': 'http://www.utusan.com.my/utusan/Bisnes',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': 'div#ContentContainer div div.summary div a',
                                  'url_prefix': self.default_url_prefix
                                  },
                     'education': {
                                   'url': 'http://www.utusan.com.my/utusan/iPendidikan',
                                   'tags': ['education'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = UtusanNewsSource(
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
        
        newsSources = UtusanNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    print "1"
    utusan = Utusan()
    print "2"
    utusan.list('nation')
    print "3"
    urls = utusan.news_urls
    print "4"
    print len(urls)
    print "5"
    for url in urls:
        print url
    utusan.save()