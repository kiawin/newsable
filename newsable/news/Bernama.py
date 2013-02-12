from newsable.news import News

class Bernama(News):
    '''
    Class for Bernama News Scraper
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''
        self._news = 'bernama'
        super().__init__(self._news)
        
        self.default_url_prefix = 'http://www.bernama.com/bernama/v6/'
        self.default_news_source_expression = 'div#newsContainer p#titleNewsList a'
        self.default_news_item_expression = 'div#newsContainer2 p#news'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://www.bernama.com/bernama/v6/listgeneral.php?pg=1',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_news_source_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'politics': {
                                  'url': 'http://www.bernama.com/bernama/v6/listpolitic.php?pg=1',
                                  'tags': ['politics','nation'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'business': {
                                  'url': 'http://www.bernama.com/bernama/v6/listbusiness.php?pg=1',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                                    },
                     'features': {
                                  'url': 'http://www.bernama.com/bernama/v6/listfeatures.php?pg=1',
                                  'tags': ['features','special'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_news_source_expression,
                                  'news_item_expr': self.default_news_item_expression,
                                  'url_prefix': self.default_url_prefix
                               },
                     '1malaysia': {
                                   'url': 'http://www.bernama.com/bernama/v6/1Malaysia.php?pg=1',
                                   'tags': ['1malaysia','special'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_news_source_expression,
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': self.default_url_prefix
                                },
                     'metro-north': {
                                     'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=nt&page=1',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'news_source_expr': 'td.news p a.news_summ',
                                     'news_item_expr': self.default_news_item_expression,
                                     'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                 },
                     'metro-east': {
                                    'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=et&page=1',
                                    'tags': ['metro','east'],
                                    'language': self.default_language,
                                    'news_source_expr': 'td.news p a.news_summ',
                                    'news_item_expr': self.default_news_item_expression,
                                    'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                  },
                     'metro-south': {
                                   'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=st&page=1',
                                   'tags': ['metro','south'],
                                   'language': self.default_language,
                                   'news_source_expr': 'td.news p a.news_summ',
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                   },
                     'metro-central': {
                                   'url': 'http://www.bernama.com/bernama/state_news/news_list.php?cat=ct&page=1',
                                   'tags': ['metro','central'],
                                   'language': self.default_language,
                                   'news_source_expr': 'td.news p a.news_summ',
                                   'news_item_expr': self.default_news_item_expression,
                                   'url_prefix': 'http://www.bernama.com/bernama/state_news/'
                                   }
                     }
    
    #def sanitize(self, text):
    #    return text.replace('\u0092','\'').replace('\u0091','\'')

    def __del__(self):
        pass