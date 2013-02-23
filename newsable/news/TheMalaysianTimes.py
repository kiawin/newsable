from newsable.news import News

class TheMalaysianTimes(News):
    '''
    Class for TheMalaysianTimes News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'theMalaysianTimes'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.themalaysiantimes.com.my'
        self.append_url_prefix = False
        self.default_news_source_expression = ['h2.post-title a']
        self.default_news_item_expression = 'div#content div.singlepost div div.entry'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                #'url': 'http://www.themalaysiantimes.com.my/category/nation',
                                'url': 'http://www.themalaysiantimes.com.my/?cat=5',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'nation-bm': {
                                   #'url': 'http://www.themalaysiantimes.com.my/category/bahasa-malaysia',
                                   'url': 'http://www.themalaysiantimes.com.my/?cat=4',
                                   'tags': ['nation'],
                                   'language': 'zsm',
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'business': {
                                  #'url': 'http://www.themalaysiantimes.com.my/category/business',
                                  'url': 'http://www.themalaysiantimes.com.my/?cat=6',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'ge13': {
                              #'url': 'http://www.themalaysiantimes.com.my/category/ge13',
                              'url': 'http://www.themalaysiantimes.com.my/?cat=17',
                              'tags': ['ge13','politics'],
                              'language': self.default_language,
                              'news_source_expr': self.default_news_source_expression,
                              'news_item_expr': self.default_news_item_expression,
                              'url_prefix': self.default_url_prefix
                              },
                     'education': {
                                   #'url': 'http://www.themalaysiantimes.com.my/category/education',
                                   'url': 'http://www.themalaysiantimes.com.my/?cat=30',
                                   'tags': ['education'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'opinion': {
                                 #'url': 'http://www.themalaysiantimes.com.my/category/opinion',
                                 'url': 'http://www.themalaysiantimes.com.my/?cat=11',
                                 'tags': ['opinion'],
                                 'language': 'und',
                                 'news_source_expr': self.default_news_source_expression,
                                 'news_item_expr': self.default_news_item_expression,
                                 'url_prefix': self.default_url_prefix
                                 }
                     }
    
    def sanitize(self, text):
        '''
        Sanitize text
        '''
        return text.replace('\u2018','\'').replace('\u2019','\'').replace('\u201C','\"').replace('\u201D','\"')

    def __del__(self):
        pass