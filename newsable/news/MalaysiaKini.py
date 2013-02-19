from newsable.news import News

class MalaysiaKini(News):
    '''
    Class for MalaysiaKini News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'malaysiaKini'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.malaysiakini.com'
        self.append_url_prefix = True
        self.default_news_source_expression = 'div.browseRows ul li.browseRowHeadline a'
        self.default_news_item_expression = 'div.contentBody'
        self.default_language = 'zsm'
        self.sources = {
                     'nation-bm': {
                                   'url':'http://www.malaysiakini.com/browse/c/my/news',
                                   'tags': ['nation'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'columns-bm': {
                                    'url': 'http://www.malaysiakini.com/browse/c/my/columns',
                                    'tags': ['opinion'],
                                    'language': self.default_language,
                                    'news_source_expr': self.default_news_source_expression,
                                    'news_item_expr': self.default_news_item_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'letters-bm': {
                                    'url': 'http://www.malaysiakini.com/browse/c/my/letters',
                                    'tags': ['opinion'],
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