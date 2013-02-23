from newsable.news import News

class NewStraitsTimes(News):
    '''
    Class for NewStraitsTimes News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'newStraitsTimes'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.nst.com.my'
        self.append_url_prefix = True
        self.default_news_source_expression = ['div.news-content h3 a']
        self.default_news_item_expression = 'div#main div.element.article div.news-article'
        #self.default_news_item_expression = 'div#main div.element.article div.news-article p'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.nst.com.my/nation/general',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'politics': {
                                  'url': 'http://www.nst.com.my/nation/politics',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'extras': {
                                  'url': 'http://www.nst.com.my/nation/extras',
                                  'tags': ['extras','special'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'umno': {
                                  'url': 'http://www.nst.com.my/nation/umno',
                                  'tags': ['features','special'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'metro-north': {
                                     'url': 'http://www.nst.com.my/streets/northern',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'news_source_expr': self.default_news_source_expression,
                                     'news_item_expr': self.default_news_item_expression,
                                     'url_prefix': self.default_url_prefix
                                 },
                     'metro-johor': {
                                   'url': 'http://www.nst.com.my/streets/johor',
                                   'tags': ['metro','south', 'johor'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'metro-central': {
                                   'url': 'http://www.nst.com.my/streets/central',
                                   'tags': ['metro','central'],
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
        return " ".join(text.split())
    #    return text.replace('\u0092','\'').replace('\u0091','\'').replace('\n','').replace('\u2018','\'').replace('\u2019','\'')

    def __del__(self):
        pass