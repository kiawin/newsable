from newsable.news import News

class IpohEcho(News):
    '''
    Class for IpohEcho News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'ipohEcho'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://ipohecho.com.my/v2/'
        self.append_url_prefix = False
        self.default_news_source_expression = 'div.entry h3.post-title a'
        self.default_news_item_expression = 'div.entry'
        self.default_language = 'eng'
        self.sources = {
                     'featured': {
                                  'url': 'http://ipohecho.com.my/v2/',
                                  'tags': ['metro','north', 'ipoh'],
                                  'language': self.default_language,
                                  'news_source_expr': 'div.entry h2.post-title a',
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                 },
                     'metro-ipoh': {
                                    'url': 'http://ipohecho.com.my/v2/',
                                    'tags': ['metro','north', 'ipoh'],
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