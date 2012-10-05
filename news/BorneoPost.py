#!/usr/bin/env python

from mongoengine import connection, OperationError
from news.News import News
from mongo.BorneoPost import BorneoPostNewsSource

class BorneoPost(News):
    """ Class for BorneoPost News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        
        News.__init__(self)
        News.useCSSSelector(self)
        connection.connect('news')
        
        self.default_url_prefix = ''
        self.default_expression = 'div.catList ul li h3 a'
        self.default_language = 'eng'
        self.config = {
                     'metro-sarawak': {
                                       'url': 'http://www.theborneopost.com/news/local/',
                                       'tags': ['local','metro','sarawak'],
                                       'language': self.default_language,
                                       'expr': self.default_expression,
                                       'url_prefix': self.default_url_prefix
                                       },
                     'nation': {
                                'url': 'http://www.theborneopost.com/news/nation/',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'metro-sabah': {
                                     'url': 'http://www.theborneopost.com/news/sabah/',
                                     'tags': ['sabah','metro'],
                                     'language': self.default_language,
                                     'expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                    },
                     'business': {
                                  'url': 'http://www.theborneopost.com/news/business/',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'columns-our-stand': {
                                           'url': 'http://www.theborneopost.com/news/columns/our-stand/',
                                           'tags': ['opinion'],
                                           'language': self.default_language,
                                           'expr': self.default_expression,
                                           'url_prefix': self.default_url_prefix
                                           },
                     'columns-letters': {
                                         'url': 'http://www.theborneopost.com/news/columns/letters-to-the-editor/',
                                         'tags': ['opinion','letters'],
                                         'language': self.default_language,
                                         'expr': self.default_expression,
                                         'url_prefix': self.default_url_prefix
                                  },
                     'columns-peace-corps': {
                                             'url': 'http://www.theborneopost.com/news/columns/peace-corps/',
                                             'tags': ['opinion'],
                                             'language': self.default_language,
                                             'expr': self.default_expression,
                                             'url_prefix': self.default_url_prefix
                                             },
                     'columns-uncle-di': {
                                          'url': 'http://www.theborneopost.com/news/columns/uncle-di/',
                                          'tags': ['opinion'],
                                          'language': self.default_language,
                                          'expr': self.default_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                     'columns-tired-eye': {
                                           'url': 'http://www.theborneopost.com/news/columns/the-tired-eye/',
                                           'tags': ['opinion'],
                                           'language': self.default_language,
                                           'expr': self.default_expression,
                                           'url_prefix': self.default_url_prefix
                                           },
                     'columns-perspective': {
                                             'url': 'http://www.theborneopost.com/news/columns/perspective/',
                                             'tags': ['opinion'],
                                             'language': self.default_language,
                                             'expr': self.default_expression,
                                             'url_prefix': self.default_url_prefix
                                             },
                     'columns-singhealth': {
                                            'url': 'http://www.theborneopost.com/news/columns/singhealth-columns/',
                                            'tags': ['opinion'],
                                            'language': self.default_language,
                                            'expr': self.default_expression,
                                            'url_prefix': self.default_url_prefix
                                            },
                       'columns-others': {
                                          'url': 'http://www.theborneopost.com/news/columns/other-columns/',
                                          'tags': ['opinion'],
                                          'language': self.default_language,
                                          'expr': self.default_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                       'columns-youth-talents': {
                                                 'url': 'http://www.theborneopost.com/news/columns/talent2012/',
                                                 'tags': ['opinion'],
                                                 'language': self.default_language,
                                                 'expr': self.default_expression,
                                                 'url_prefix': self.default_url_prefix
                                                 },
                       'columns-local-entrepreneurs': {
                                                       'url': 'http://www.theborneopost.com/news/columns/local-entrepreneurs/',
                                                       'tags': ['opinion','business'],
                                                       'language': self.default_language,
                                                       'expr': self.default_expression,
                                                       'url_prefix': self.default_url_prefix
                                                       },
                       'columns-paul-sir': {
                                            'url': 'http://www.theborneopost.com/news/columns/paul-sir/',
                                            'tags': ['opinion'],
                                            'language': self.default_language,
                                            'expr': self.default_expression,
                                            'url_prefix': self.default_url_prefix
                                            },
                       'columns-hornbill-corner': {
                                                   'url': 'http://www.theborneopost.com/news/columns/hermit-corner/',
                                                   'tags': ['opinion'],
                                                   'language': self.default_language,
                                                   'expr': self.default_expression,
                                                   'url_prefix': self.default_url_prefix
                                                   },
                       'columns-edge-of-town': {
                                                'url': 'http://www.theborneopost.com/news/columns/edge-of-town/',
                                                'tags': ['opinion'],
                                                'language': self.default_language,
                                                'expr': self.default_expression,
                                                'url_prefix': self.default_url_prefix
                                                },
                       'columns-and-so': {
                                          'url': 'http://www.theborneopost.com/news/columns/and-so-it-goes/',
                                          'tags': ['opinion'],
                                          'language': self.default_language,
                                          'expr': self.default_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                       'metro-sarawak-bm': {
                                            'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-tempatan/',
                                            'tags': ['local','metro','sarawak'],
                                            'language': 'zsm',
                                            'expr': self.default_expression,
                                            'url_prefix': self.default_url_prefix
                                            },
                       'nation-bm': {
                                     'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-nasional/',
                                     'tags': ['nation'],
                                     'language': 'zsm',
                                     'expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                       'metro-sarawak-iban': {
                                      'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-iban/',
                                      'tags': ['metro','sarawak','iban'],
                                      'language': 'iba',
                                      'expr': self.default_expression,
                                      'url_prefix': self.default_url_prefix
                                      },
                       'metro-sabah-bm': {
                                       'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-sabah/',
                                       'tags': ['metro','sabah'],
                                       'language': 'zsm',
                                       'expr': self.default_expression,
                                       'url_prefix': self.default_url_prefix
                                       }
                     }
        
    def save(self):
        """ Save all news urls into collection """
        
        for url in self.news_urls:
            try:
                newsSources = BorneoPostNewsSource(
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
        
        newsSources = BorneoPostNewsSource()
        newsSources.drop_collection()
            
if __name__ == '__main__':
    borneoPost = BorneoPost()
    borneoPost.list('columns-our-stand')
    urls = borneoPost.news_urls
    print len(urls)
    for url in urls:
        print url
    borneoPost.save()