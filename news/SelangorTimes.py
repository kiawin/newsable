#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.SelangorTimes import SelangorTimesNewsSource

class SelangorTimes(News):
    """ Class for SelangorTimes News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useXPath(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.selangortimes.com/'
        self.default_expression = '//div[@class=\'main_news_desc\']/p/a[@class=\'current_news_title\'] | //div[@class=\'main_news_desc\']/div/p/a[@class=\'current_news_title\']'
        self.default_language = 'eng'
        self.config = {
                     'metro-selangor': {
                                'url': 'http://www.selangortimes.com/index.php?section=news',
                                'tags': ['metro','selangor','central'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'opinion': {
                                  'url': 'http://www.selangortimes.com/index.php?section=views',
                                  'tags': ['opinion'],
                                  'language': self.default_language,
                                  'expr': '//td[@class=\'centerBody\']/div/p/a',
                                  'url_prefix': self.default_url_prefix
                                  },
                     'culture': {
                                  'url': 'http://www.selangortimes.com/index.php?section=culture',
                                  'tags': ['culture','special'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'insight': {
                                  'url': 'http://www.selangortimes.com/index.php?section=insight',
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
                newsSources = SelangorTimesNewsSource(
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
        
        newsSources = SelangorTimesNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    selangortimes = SelangorTimes()
    selangortimes.list('metro-selangor')
    urls = selangortimes.news_urls
    print len(urls)
    for url in urls:
        print url
    selangortimes.save()