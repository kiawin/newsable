#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.TheSunDaily import TheSunDailyNewsSource

class TheSunDaily(News):
    """ Class for TheSunDaily News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.thesundaily.my'
        self.default_expression = 'h2.node-title a'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://www.thesundaily.my/news/local',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'business': {
                                  'url': 'http://www.thesundaily.my/news/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'property': {
                                  'url': 'http://www.thesundaily.my/news/media-marketing/property',
                                  'tags': ['property','business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'media-marketing': {
                                         'url': 'http://www.thesundaily.my/news/media-marketing',
                                         'tags': ['business'],
                                         'language': self.default_language,
                                         'expr': self.default_expression,
                                         'url_prefix': self.default_url_prefix
                                         },
                     'education': {
                                   'url': 'http://www.thesundaily.my/news/education',
                                   'tags': ['education'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'metro': {
                               'url': 'http://www.thesundaily.my/news/community',
                               'tags': ['metro'],
                               'language': self.default_language,
                               'expr': self.default_expression,
                               'url_prefix': self.default_url_prefix
                               },
                     'opinion': {
                                 'url': 'http://www.thesundaily.my/news/columns',
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
                newsSources = TheSunDailyNewsSource(
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
        
        newsSources = TheSunDailyNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    thesundaily = TheSunDaily()
    thesundaily.list('nation')
    urls = thesundaily.news_urls
    print len(urls)
    for url in urls:
        print url
    thesundaily.save()