from newsable.news import News

class Selangorku(News):
    '''
    Class for Selangorku News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'selangorku'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.selangorku.com'
        self.append_url_prefix = False
        self.default_news_source_expression = ['h3.entry-title a']
        self.default_news_item_expression = 'div.entry-content.clearfix p'
        self.default_language = 'zsm'
        self.sources = {
                     'metro-selangor': {
                                'url': 'http://www.selangorku.com/?cat=241',
                                'tags': ['state', 'selangor'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'mb-news': {
                                  'url': 'http://www.selangorku.com/?cat=11',
                                  'tags': ['state','selangor'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'mb-programme': {
                                  'url': 'http://www.selangorku.com/?cat=12',
                                  'tags': ['state', 'selangor'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'mb-politics': {
                                  'url': 'http://www.selangorku.com/?cat=54',
                                  'tags': ['state','selangor', 'politics'],
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