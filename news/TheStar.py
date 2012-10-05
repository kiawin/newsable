#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.TheStar import TheStarNewsSource
    
class TheStar(News):
    """ Class for TheStar News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect("news")
        
        self.default_url_prefix = 'http://thestar.com.my'
        self.default_expression = 'div.news_container h2 a'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://thestar.com.my/news/nation/',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'sarawak': {
                                 'url': 'http://thestar.com.my/news/sarawak/',
                                 'tags': ['nation','sarawak'],
                                 'language': self.default_language,
                                 'expr': self.default_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'business': {
                                  'url': 'http://biz.thestar.com.my/news/',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro-central': {
                                       'url': 'http://thestar.com.my/metro/central/',
                                       'tags': ['metro','central'],
                                       'language': self.default_language,
                                       'expr': self.default_expression,
                                       'url_prefix': self.default_url_prefix
                                       },
                     'metro-north': {
                                     'url': 'http://thestar.com.my/metro/north/',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                     'metro-biz': {
                                   'url': 'http://thestar.com.my/metro/biz/',
                                   'tags': ['metro','business'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'metro-southneast': {
                                          'url': 'http://thestar.com.my/metro/southneast/',
                                          'tags': ['metro','south','east'],
                                          'language': self.default_language,
                                          'expr': self.default_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                     'metro-perak': {
                                     'url': 'http://thestar.com.my/metro/perak/',
                                     'tags': ['metro','perak','north'],
                                     'language': self.default_language,
                                     'expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                     'courts': {
                                'url': 'http://thestar.com.my/news/courts/',
                                'tags': ['courts'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'parliament': {
                                    'url': 'http://thestar.com.my/news/parliament/',
                                    'tags': ['parliament'],
                                    'language': self.default_language,
                                    'expr': self.default_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'opinion': {
                                 'url': 'http://thestar.com.my/news/opinion/',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 'expr': self.default_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'maritime': {
                                  'url': 'http://thestar.com.my/maritime/',
                                  'tags': ['maritime','business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = TheStarNewsSource(
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
        
        newsSources = TheStarNewsSource()
        newsSources.drop_collection()
    
if __name__ == '__main__':
    thestar = TheStar()
    thestar.list('nation')
    urls = thestar.news_urls
    print len(urls)
    for url in urls:
        print url
    thestar.save()