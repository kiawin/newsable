from newsable.news import News

class BorneoPost(News):
    '''
    Class for BorneoPost News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'theBorneoPost'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.theborneopost.com'
        self.append_url_prefix = False
        self.default_news_source_expression = 'div.catList ul li h3 a'
        self.default_news_item_expression = 'div.newsBody.floatLeft'
        self.default_language = 'eng'
        self.sources = {
                     'metro-sarawak': {
                                       'url': 'http://www.theborneopost.com/news/local/',
                                       'tags': ['local','metro','sarawak'],
                                       'language': self.default_language,
                                       'news_source_expr': self.default_news_source_expression,
                                       'news_item_expr': self.default_news_item_expression,
                                       'expr': self.default_news_source_expression,
                                       'url_prefix': self.default_url_prefix
                                       },
                     'nation': {
                                'url': 'http://www.theborneopost.com/news/nation/',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'metro-sabah': {
                                     'url': 'http://www.theborneopost.com/news/sabah/',
                                     'tags': ['sabah','metro'],
                                     'language': self.default_language,
                                     'news_source_expr': self.default_news_source_expression,
                                     'news_item_expr': self.default_news_item_expression,
                                     'url_prefix': self.default_url_prefix
                                    },
                     'business': {
                                  'url': 'http://www.theborneopost.com/news/business/',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'columns-our-stand': {
                                           'url': 'http://www.theborneopost.com/news/columns/our-stand/',
                                           'tags': ['opinion'],
                                           'language': self.default_language,
                                           'news_source_expr': self.default_news_source_expression,
                                           'news_item_expr': self.default_news_item_expression,
                                           'url_prefix': self.default_url_prefix
                                           },
                     'columns-letters': {
                                         'url': 'http://www.theborneopost.com/news/columns/letters-to-the-editor/',
                                         'tags': ['opinion','letters'],
                                         'language': self.default_language,
                                         'news_source_expr': self.default_news_source_expression,
                                         'news_item_expr': self.default_news_item_expression,
                                         'url_prefix': self.default_url_prefix
                                  },
                     'columns-peace-corps': {
                                             'url': 'http://www.theborneopost.com/news/columns/peace-corps/',
                                             'tags': ['opinion'],
                                             'language': self.default_language,
                                             'news_source_expr': self.default_news_source_expression,
                                             'news_item_expr': self.default_news_item_expression,
                                             'url_prefix': self.default_url_prefix
                                             },
                     'columns-uncle-di': {
                                          'url': 'http://www.theborneopost.com/news/columns/uncle-di/',
                                          'tags': ['opinion'],
                                          'language': self.default_language,
                                          'news_source_expr': self.default_news_source_expression,
                                          'news_item_expr': self.default_news_item_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                     'columns-tired-eye': {
                                           'url': 'http://www.theborneopost.com/news/columns/the-tired-eye/',
                                           'tags': ['opinion'],
                                           'language': self.default_language,
                                           'news_source_expr': self.default_news_source_expression,
                                           'news_item_expr': self.default_news_item_expression,
                                           'url_prefix': self.default_url_prefix
                                           },
                     'columns-perspective': {
                                             'url': 'http://www.theborneopost.com/news/columns/perspective/',
                                             'tags': ['opinion'],
                                             'language': self.default_language,
                                             'news_source_expr': self.default_news_source_expression,
                                             'news_item_expr': self.default_news_item_expression,
                                             'url_prefix': self.default_url_prefix
                                             },
                     'columns-singhealth': {
                                            'url': 'http://www.theborneopost.com/news/columns/singhealth-columns/',
                                            'tags': ['opinion'],
                                            'language': self.default_language,
                                            'news_source_expr': self.default_news_source_expression,
                                            'news_item_expr': self.default_news_item_expression,
                                            'url_prefix': self.default_url_prefix
                                            },
                       'columns-others': {
                                          'url': 'http://www.theborneopost.com/news/columns/other-columns/',
                                          'tags': ['opinion'],
                                          'language': self.default_language,
                                          'news_source_expr': self.default_news_source_expression,
                                          'news_item_expr': self.default_news_item_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                       'columns-youth-talents': {
                                                 'url': 'http://www.theborneopost.com/news/columns/talent2012/',
                                                 'tags': ['opinion'],
                                                 'language': self.default_language,
                                                 'news_source_expr': self.default_news_source_expression,
                                                 'news_item_expr': self.default_news_item_expression,
                                                 'url_prefix': self.default_url_prefix
                                                 },
                       'columns-local-entrepreneurs': {
                                                       'url': 'http://www.theborneopost.com/news/columns/local-entrepreneurs/',
                                                       'tags': ['opinion','business'],
                                                       'language': self.default_language,
                                                       'news_source_expr': self.default_news_source_expression,
                                                       'news_item_expr': self.default_news_item_expression,
                                                       'url_prefix': self.default_url_prefix
                                                       },
                       'columns-paul-sir': {
                                            'url': 'http://www.theborneopost.com/news/columns/paul-sir/',
                                            'tags': ['opinion'],
                                            'language': self.default_language,
                                            'news_source_expr': self.default_news_source_expression,
                                            'news_item_expr': self.default_news_item_expression,
                                            'url_prefix': self.default_url_prefix
                                            },
                       'columns-hornbill-corner': {
                                                   'url': 'http://www.theborneopost.com/news/columns/hermit-corner/',
                                                   'tags': ['opinion'],
                                                   'language': self.default_language,
                                                   'news_source_expr': self.default_news_source_expression,
                                                   'news_item_expr': self.default_news_item_expression,
                                                   'url_prefix': self.default_url_prefix
                                                   },
                       'columns-edge-of-town': {
                                                'url': 'http://www.theborneopost.com/news/columns/edge-of-town/',
                                                'tags': ['opinion'],
                                                'language': self.default_language,
                                                'news_source_expr': self.default_news_source_expression,
                                                'news_item_expr': self.default_news_item_expression,
                                                'url_prefix': self.default_url_prefix
                                                },
                       'columns-and-so': {
                                          'url': 'http://www.theborneopost.com/news/columns/and-so-it-goes/',
                                          'tags': ['opinion'],
                                          'language': self.default_language,
                                          'news_source_expr': self.default_news_source_expression,
                                          'news_item_expr': self.default_news_item_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                       'metro-sarawak-bm': {
                                            'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-tempatan/',
                                            'tags': ['local','metro','sarawak'],
                                            'language': 'zsm',
                                            'news_source_expr': self.default_news_source_expression,
                                            'news_item_expr': self.default_news_item_expression,
                                            'url_prefix': self.default_url_prefix
                                            },
                       'nation-bm': {
                                     'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-nasional/',
                                     'tags': ['nation'],
                                     'language': 'zsm',
                                     'news_source_expr': self.default_news_source_expression,
                                     'news_item_expr': self.default_news_item_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                       'metro-sarawak-iban': {
                                      'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-iban/',
                                      'tags': ['metro','sarawak','iban'],
                                      'language': 'iba',
                                      'news_source_expr': self.default_news_source_expression,
                                      'news_item_expr': self.default_news_item_expression,
                                      'url_prefix': self.default_url_prefix
                                      },
                       'metro-sabah-bm': {
                                       'url': 'http://www.theborneopost.com/news/utusan-borneo/berita-sabah/',
                                       'tags': ['metro','sabah'],
                                       'language': 'zsm',
                                       'news_source_expr': self.default_news_source_expression,
                                       'news_item_expr': self.default_news_item_expression,
                                       'url_prefix': self.default_url_prefix
                                       }
                     }
        
    #def sanitize(self, text):
        '''
        Sanitize text
        '''
    #    return text.replace('\u0092','\'').replace('\u0091','\'')

    def __del__(self):
        pass    