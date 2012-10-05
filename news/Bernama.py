#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.Bernama import BernamaNewsSource

class Bernama(News):
    """ Class for Bernama News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.bernama.com/bernama/v6/'
        self.default_expression = 'div#newsContainer p#titleNewsList a'
        self.default_language = 'eng'
        self.config = {
                     'nation': {
                                'url': 'http://www.bernama.com/bernama/v6/listgeneral.php?pg=1',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'politics': {
                                  'url': 'http://www.bernama.com/bernama/v6/listpolitic.php?pg=1',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'business': {
                                  'url': 'http://www.bernama.com/bernama/v6/listbusiness.php?pg=1',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'features': {
                                  'url': 'http://www.bernama.com/bernama/v6/listfeatures.php?pg=1',
                                  'tags': ['features','special'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     '1malaysia': {
                                   'url': 'http://www.bernama.com/bernama/v6/1Malaysia.php?pg=1',
                                   'tags': ['1malaysia','special'],
                                   'language': self.default_language,
                                   'expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                },
                     'metro-north': {
                                     'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=nt&page=1',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'expr': 'td.news p a.news_summ',
                                     'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                 },
                     'metro-east': {
                                    'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=et&page=1',
                                    'tags': ['metro','east'],
                                    'language': self.default_language,
                                    'expr': 'td.news p a.news_summ',
                                    'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                  },
                     'metro-south': {
                                   'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=st&page=1',
                                   'tags': ['metro','south'],
                                   'language': self.default_language,
                                   'expr': 'td.news p a.news_summ',
                                   'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                   },
                     'metro-central': {
                                   'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=ct&page=1',
                                   'tags': ['metro','central'],
                                   'language': self.default_language,
                                   'expr': 'td.news p a.news_summ',
                                   'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                   }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = BernamaNewsSource(
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
        
        newsSources = BernamaNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    bernama = Bernama()
    bernama.list('nation')
    urls = bernama.news_urls
    print len(urls)
    for url in urls:
        print url
    bernama.save()