from newsable.news import News

class TheStar(News):
    '''
    Class for TheStar News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'theStar'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://thestar.com.my'
        self.default_news_source_expression = 'div.news_container h2 a'
        self.default_news_item_expression = 'div#story_main div#story_content'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://thestar.com.my/news/nation/',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'sarawak': {
                                 'url': 'http://thestar.com.my/news/sarawak/',
                                 'tags': ['nation','sarawak'],
                                 'language': self.default_language,
                                 'news_source_expr': self.default_news_source_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'business': {
                                  'url': 'http://biz.thestar.com.my/news/',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro-central': {
                                       'url': 'http://thestar.com.my/metro/central/',
                                       'tags': ['metro','central'],
                                       'language': self.default_language,
                                       'news_source_expr': self.default_news_source_expression,
                                       'url_prefix': self.default_url_prefix
                                       },
                     'metro-north': {
                                     'url': 'http://thestar.com.my/metro/north/',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'news_source_expr': self.default_news_source_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                     'metro-biz': {
                                   'url': 'http://thestar.com.my/metro/biz/',
                                   'tags': ['metro','business'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'metro-southneast': {
                                          'url': 'http://thestar.com.my/metro/southneast/',
                                          'tags': ['metro','south','east'],
                                          'language': self.default_language,
                                          'news_source_expr': self.default_news_source_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                     'metro-perak': {
                                     'url': 'http://thestar.com.my/metro/perak/',
                                     'tags': ['metro','perak','north'],
                                     'language': self.default_language,
                                     'news_source_expr': self.default_news_source_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                     'courts': {
                                'url': 'http://thestar.com.my/news/courts/',
                                'tags': ['courts'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'parliament': {
                                    'url': 'http://thestar.com.my/news/parliament/',
                                    'tags': ['parliament'],
                                    'language': self.default_language,
                                    'news_source_expr': self.default_news_source_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'opinion': {
                                 'url': 'http://thestar.com.my/news/opinion/',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 'news_source_expr': self.default_news_source_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'maritime': {
                                  'url': 'http://thestar.com.my/maritime/',
                                  'tags': ['maritime','business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'url_prefix': self.default_url_prefix
                                  }
                     }
    
    def sanitize(self, text):
        '''
        Sanitize text
        '''
        return text.replace('\u0092','\'').replace('\u0091','\'')

    def __del__(self):
        pass