from newsable.news import News

class FreeMalaysiaToday(News):
    '''
    Class for FreeMalaysiaToday News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'freeMalaysiaToday'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.freemalaysiatoday.com'
        self.append_url_prefix = False
        self.default_news_source_expression = 'div.ind-post h2 a'
        self.default_news_item_expression = 'div.storycontent-post'
        self.default_language = 'eng'
        self.sources = {
                       'nation': {
                                  'url': 'http://www.freemalaysiatoday.com/category/nation/',
                                  'tags': ['nation'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                       'business': {
                                    'url': 'http://www.freemalaysiatoday.com/category/business/',
                                    'tags': ['business'],
                                    'language': self.default_language,
                                    'news_source_expr': self.default_news_source_expression,
                                    'news_item_expr': self.default_news_item_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                       'opinion': {
                                   'url': 'http://www.freemalaysiatoday.com/category/opinion/',
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
        return text.replace('\u2018','\'').replace('\u2019','\'')

    def __del__(self):
        pass