from newsable.news import News

class SelangorTimes(News):
    '''
    Class for SelangorTimes News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'selangorTimes'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.selangortimes.com/'
        self.append_url_prefix = True
        #self.default_news_source_expression = 'div.main_news_desc a[style="text-decoration:underline"]'
        self.default_news_source_expression = ['div.main_news_desc p a.current_news_title']
        #'div.main_news_desc div p a.current_news_title'
        #'//div[@class=\'main_news_desc\']/p/a[@class=\'current_news_title\'] | //div[@class=\'main_news_desc\']/div/p/a[@class=\'current_news_title\']'
        self.default_news_item_expression = 'div.contentdetails'
        self.default_language = 'eng'
        self.sources = {
                     'metro-selangor': {
                                'url': 'http://www.selangortimes.com/index.php?section=news',
                                'tags': ['metro','selangor','central'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     #'opinion': {
                     #             'url': 'http://www.selangortimes.com/index.php?section=views',
                     #             'tags': ['opinion'],
                     #             'language': self.default_language,
                                  #'expr': '//td[@class=\'centerBody\']/div/p/a',
                     #             'news_source_expr': 'td.centerBody div p a',
                     #             'news_item_expr': self.default_news_item_expression,
                     #             'url_prefix': self.default_url_prefix
                     #             },
                     'culture': {
                                  'url': 'http://www.selangortimes.com/index.php?section=culture',
                                  'tags': ['culture','special'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'insight': {
                                  'url': 'http://www.selangortimes.com/index.php?section=insight',
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
    #    return text.replace('â€™','\'').replace('â€˜','\'')
    #    return text.replace('\u0092','\'').replace('\u0091','\'').replace('\n','').replace('\u2018','\'').replace('\u2019','\'')

    def __del__(self):
        pass