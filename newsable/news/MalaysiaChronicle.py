from newsable.news import News

class MalaysiaChronicle(News):
    '''
    Class for MalaysiaChronicle News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'malaysiaChronicle'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.malaysia-chronicle.com'
        self.append_url_prefix = True
        self.default_news_source_expression = 'div.catItemBody div.catItemTitle a'
        self.default_news_item_expression = 'div.itemBody div.itemFullText'
        self.default_language = 'eng'
        self.sources = {
                     'politics': {
                                  'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=12&Itemid=2',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'business': {
                                  'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=13&Itemid=3',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'social': {
                                  'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=14&Itemid=4',
                                  'tags': ['social','metro'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     'featured': {
                                   'url': 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=11&Itemid=10',
                                   'tags': ['features','special'],
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
        return text.replace('\n','').replace('\t','').replace('\u2018','\'').replace('\u2019','\'').strip()

    def __del__(self):
        pass