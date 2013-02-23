from newsable.news import News

class Utusan(News):
    '''
    Class for Utusan News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'utusan'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.utusan.com.my'
        self.append_url_prefix = True
        self.default_news_source_expression = ['div#ContentContainer div.summary div a']
        self.default_news_item_expression = 'div#ContentContainer div.fullstory'
        self.default_language = 'zsm'
        self.sources = {
                     'nation': {
                                'url': 'http://www.utusan.com.my/utusan/Dalam_Negeri',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'politics': {
                                  'url': 'http://www.utusan.com.my/utusan/Politik',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'parliament': {
                                    'url': 'http://www.utusan.com.my/utusan/Parlimen',
                                    'tags': ['parliament'],
                                    'language': self.default_language,
                                    'news_source_expr': self.default_news_source_expression,
                                    'news_item_expr': self.default_news_item_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'crime': {
                               'url': 'http://www.utusan.com.my/utusan/Jenayah',
                               'tags': ['crime','nation'],
                               'language': self.default_language,
                               'news_source_expr': self.default_news_source_expression,
                               'news_item_expr': self.default_news_item_expression,
                               'url_prefix': self.default_url_prefix
                               },
                     'courts': {
                                'url': 'http://www.utusan.com.my/utusan/Mahkamah',
                                'tags': ['courts'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'special': {
                                 'url': 'http://www.utusan.com.my/utusan/Laporan_Khas',
                                 'tags': ['special'],
                                 'language': self.default_language,
                                 'news_source_expr': self.default_news_source_expression,
                                 'news_item_expr': self.default_news_item_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'business': {
                                  'url': 'http://www.utusan.com.my/utusan/Bisnes',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': ['div#ContentContainer div div.summary div a'],
                                  'news_item_expr': self.default_news_item_expression,
                                  #'expr': 'div#ContentContainer div div.summary div a',
                                  'url_prefix': self.default_url_prefix
                                  },
                     'education': {
                                   'url': 'http://www.utusan.com.my/utusan/iPendidikan',
                                   'tags': ['education'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                   }
                     }
        
    #def sanitize(self, text):
        '''
        Sanitize text
        '''
    #    return text.replace('\u0092','\'').replace('\u0091','\'').replace('\n','').replace('\u2018','\'').replace('\u2019','\'')

    def __del__(self):
        pass