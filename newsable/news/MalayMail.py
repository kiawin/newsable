from newsable.news import News

class MalayMail(News):
    '''
    Class for MalayMail News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'malayMail'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.mmail.com.my'
        self.append_url_prefix = True
        self.default_news_source_expression = 'div.node-inner div.teaser-title a'
        self.default_news_item_expression = 'div.node-inner div.content.clear-block'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.mmail.com.my/nation',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'business': {
                                  'url': 'http://www.mmail.com.my/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro': {
                               'url': 'http://www.mmail.com.my/Hotline',
                               'tags': ['metro'],
                               'language': self.default_language,
                               'news_source_expr': self.default_news_source_expression,
                               'news_item_expr': self.default_news_item_expression,
                               'url_prefix': self.default_url_prefix
                               },
                     'opinion': {
                                 'url': 'http://www.mmail.com.my/op-ed',
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