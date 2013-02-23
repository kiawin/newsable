from newsable.news import News

class MySinchew(News):
    '''
    Class for MySinchew News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'mySinchew'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.mysinchew.com'
        self.append_url_prefix = True
        self.default_news_source_expression = ['div#front div#inpage_left h4.title.teaser a#title']
        self.default_news_item_expression = 'div.node div.content div.content_wrapper'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.mysinchew.com/taxonomy/term/4',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'opinion': {
                                  'url': 'http://www.mysinchew.com/taxonomy/term/12',
                                  'tags': ['opinion'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro-mykampung': {
                                  'url': 'http://www.mysinchew.com/taxonomy/term/102',
                                  'tags': ['metro'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'features': {
                                  'url': 'http://www.mysinchew.com/taxonomy/term/10',
                                  'tags': ['features','special'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'business': {
                                   'url': 'http://www.mysinchew.com/taxonomy/term/121',
                                   'tags': ['business'],
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