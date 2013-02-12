#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.MalayMail import MalayMailNewsSource

class MalayMail(News):
    """ Class for MalayMail News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = 'http://www.mmail.com.my'
        self.default_news_source_expression = 'div.node-inner div.teaser-title a'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.mmail.com.my/nation',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_news_source_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'business': {
                                  'url': 'http://www.mmail.com.my/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_news_source_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro': {
                               'url': 'http://www.mmail.com.my/Hotline',
                               'tags': ['metro'],
                               'language': self.default_language,
                               'expr': self.default_news_source_expression,
                               'url_prefix': self.default_url_prefix
                               },
                     'opinion': {
                                 'url': 'http://www.mmail.com.my/op-ed',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 'expr': self.default_news_source_expression,
                                 'url_prefix': self.default_url_prefix
                                 }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = MalayMailNewsSource(
                                                  url=self.sources[self.news_category]['url_prefix']+url,
                                                  category=self.news_category,
                                                  tags=self.sources[self.news_category]['tags'],
                                                  language=self.sources[self.news_category]['language']
                                                  )
                newsSources.save()
            except OperationError:
                """ Error raised when url exist in collection """
                pass
    
    def purge(self):
        """ Purge the collection """
        
        newsSources = MalayMailNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    mmail = MalayMail()
    mmail.list('metro')
    urls = mmail.news_urls
    print len(urls)
    for url in urls:
        print url
    mmail.save()