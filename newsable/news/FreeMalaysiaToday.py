#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.FreeMalaysiaToday import FreeMalaysiaTodayNewsSource

class FreeMalaysiaToday(News):
    """ Class for FreeMalaysiaToday News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect("news")
        
        self.default_url_prefix = ''
        self.default_news_source_expression = 'div.ind-post h2 a'
        self.default_language = 'und'
        self.sources = {
                       'nation': {
                                  'url': 'http://www.freemalaysiatoday.com/category/nation/',
                                  'tags': ['nation'],
                                  'language': self.default_language,
                                  'expr': self.default_news_source_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                       'business': {
                                    'url': 'http://www.freemalaysiatoday.com/category/business/',
                                    'tags': ['business'],
                                    'language': self.default_language,
                                    'expr': self.default_news_source_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                       'opinion': {
                                   'url': 'http://www.freemalaysiatoday.com/category/opinion/',
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
                newsSources = FreeMalaysiaTodayNewsSource(
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
        
        newsSources = FreeMalaysiaTodayNewsSource()
        newsSources.drop_collection()
    
if __name__ == '__main__':
    fmt = FreeMalaysiaToday()
    fmt.list('nation')
    urls = fmt.news_urls
    print len(urls)
    for url in urls:
        print url
    fmt.save()