from newsable.news import News

class TheSunDaily(News):
    '''
    Class for TheSunDaily News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'theSunDaily'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.thesundaily.my'
        self.append_url_prefix = True
        self.default_news_source_expression = 'h2.node-title a'
        self.default_news_item_expression= 'div#content-content div div.content'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.thesundaily.my/news/local',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'business': {
                                  'url': 'http://www.thesundaily.my/news/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'property': {
                                  'url': 'http://www.thesundaily.my/news/media-marketing/property',
                                  'tags': ['property','business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'media-marketing': {
                                         'url': 'http://www.thesundaily.my/news/media-marketing',
                                         'tags': ['business'],
                                         'language': self.default_language,
                                         'news_source_expr': self.default_news_source_expression,
                                         'news_item_expr': self.default_news_item_expression,
                                         'url_prefix': self.default_url_prefix
                                         },
                     'education': {
                                   'url': 'http://www.thesundaily.my/news/education',
                                   'tags': ['education'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     #'metro': {
                     #          'url': 'http://www.thesundaily.my/news/community',
                     #          'tags': ['metro'],
                     #          'language': self.default_language,
                     #          'news_source_expr': self.default_news_source_expression,
                     #          'news_item_expr': self.default_news_item_expression,
                     #          'url_prefix': self.default_url_prefix
                     #          },
                     'opinion': {
                                 'url': 'http://www.thesundaily.my/news/columns',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 'news_source_expr': self.default_news_source_expression,
                                 'news_item_expr': self.default_news_item_expression,
                                 'url_prefix': self.default_url_prefix
                                 }
                     }
        
    def sanitize(self, text):
        '''
        Sanitize text
        '''
        return text.replace('\u2018','\'').replace('\u2019','\'').replace('\u0060','\'').replace('\n','')
    
    def __del__(self):
        pass