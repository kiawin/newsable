from newsable.news import News

class TheMalaysianInsider(News):
    '''
    Class for TheMalaysianInsider News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'theMalaysianInsider'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.themalaysianinsider.com'
        self.append_url_prefix = False
        #self.default_news_source_expression = '//div[@class=\'sectionNews\']/h1/a | //div[@class=\'borderless\']/div[@class=\'bordered\']/h3/a | //div[@id=\'left\']/ul/li/a | //div[@id=\'center\']/ul/li/a | //div[@id=\'right\']/ul/li/a'
        #self.default_news_source_expression = 'div[class=\'sectionNews\'] h1 a | div[class=\'borderless\'] div[class=\'bordered\'] h3 a | div[id=\'left\'] ul li a | div[id=\'center\'] ul li a | div[id=\'right\'] ul li a'
        self.default_news_source_expression = ['div.sectionNews h1 a','div.newsBlock div div h3 a','div.articleBlock div ul li a']
        self.default_news_item_expression = 'div.articleBlock div#article'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.themalaysianinsider.com/malaysia',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'business': {
                                  'url': 'http://www.themalaysianinsider.com/business',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'bahasa': {
                                'url': 'http://www.themalaysianinsider.com/bahasa',
                                'tags': ['nation'],
                                'language': 'ms',
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'opinion': {
                                 'url': 'http://www.themalaysianinsider.com/opinion',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 #'news_source_expr': '//div[@class=\'items\']/div[@class=\'item\']/div[@class=\'title\']/a | //div[@class=\'main\']/div[@class=\'title\']/a',
                                 'news_source_expr': ['div#mainContentSection div.breaking-views div div.items div.item div.title a','div#mainContentSection div.opinionsBlock div.columnists div.scrollable.vertical div div.category div.entries div.main div.title a'],
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