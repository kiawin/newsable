#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.NewStraitsTimes import NewStraitsTimesNewsSource

class NewStraitsTimes(News):
    """ Class for NewStraitsTimes News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.nst.com.my'
        self.default_expression = 'div.news-content h3 a'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://www.nst.com.my/nation/general',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'politics': {
                                  'url': 'http://www.nst.com.my/nation/politics',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'extras': {
                                  'url': 'http://www.nst.com.my/nation/extras',
                                  'tags': ['extras','special'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'umno': {
                                  'url': 'http://www.nst.com.my/nation/umno',
                                  'tags': ['features','special'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'metro-north': {
                                     'url': 'http://www.nst.com.my/streets/northern',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                 },
                     'metro-johor': {
                                   'url': 'http://www.nst.com.my/streets/johor',
                                   'tags': ['metro','south', 'johor'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'metro-central': {
                                   'url': 'http://www.nst.com.my/streets/central',
                                   'tags': ['metro','central'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = NewStraitsTimesNewsSource(
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
        
        newsSources = NewStraitsTimesNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    nst = NewStraitsTimes()
    nst.list('nation')
    urls = nst.news_urls
    print len(urls)
    for url in urls:
        print url
    nst.save()