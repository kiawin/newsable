from newsable import Scraper
from newsable import Logger
from newsable import Stripper

from newsable import NewsSource
from newsable import NewsItem

from pymongo.errors import OperationFailure

class TheStar():
    """ Class for TheStar News Scraper """ 
    
    def __init__(self):
        """ Constructor """
        #logging.basicConfig(filename='theStar.log',level=logging.DEBUG, format='%(levelname)s:  %(message)s')
        self._logger = Logger().get()
        
        self.default_database = 'news'
        self.default_collection = 'theStar' 
        self.default_url_prefix = 'http://thestar.com.my'
        self.default_expression = 'div.news_container h2 a'
        self.default_news_item_expression = 'div#story_main div#story_content'
        self.default_language = 'eng'
        self.sources = {
                     'nation': {
                                'url': 'http://thestar.com.my/news/nation/',
                                'tags': ['nation'],
                                'language': self.default_language,
                                'news_source_expr': self.default_expression,
                                'news_item_expr': self.default_news_item_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'sarawak': {
                                 'url': 'http://thestar.com.my/news/sarawak/',
                                 'tags': ['nation','sarawak'],
                                 'language': self.default_language,
                                 'news_source_expr': self.default_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'business': {
                                  'url': 'http://biz.thestar.com.my/news/',
                                  'tags': ['business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  },
                     'metro-central': {
                                       'url': 'http://thestar.com.my/metro/central/',
                                       'tags': ['metro','central'],
                                       'language': self.default_language,
                                       'news_source_expr': self.default_expression,
                                       'url_prefix': self.default_url_prefix
                                       },
                     'metro-north': {
                                     'url': 'http://thestar.com.my/metro/north/',
                                     'tags': ['metro','north'],
                                     'language': self.default_language,
                                     'news_source_expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                     'metro-biz': {
                                   'url': 'http://thestar.com.my/metro/biz/',
                                   'tags': ['metro','business'],
                                   'language': self.default_language,
                                   'news_source_expr': self.default_expression,
                                   'url_prefix': self.default_url_prefix
                                   },
                     'metro-southneast': {
                                          'url': 'http://thestar.com.my/metro/southneast/',
                                          'tags': ['metro','south','east'],
                                          'language': self.default_language,
                                          'news_source_expr': self.default_expression,
                                          'url_prefix': self.default_url_prefix
                                          },
                     'metro-perak': {
                                     'url': 'http://thestar.com.my/metro/perak/',
                                     'tags': ['metro','perak','north'],
                                     'language': self.default_language,
                                     'news_source_expr': self.default_expression,
                                     'url_prefix': self.default_url_prefix
                                     },
                     'courts': {
                                'url': 'http://thestar.com.my/news/courts/',
                                'tags': ['courts'],
                                'language': self.default_language,
                                'news_source_expr': self.default_expression,
                                'url_prefix': self.default_url_prefix
                                },
                     'parliament': {
                                    'url': 'http://thestar.com.my/news/parliament/',
                                    'tags': ['parliament'],
                                    'language': self.default_language,
                                    'news_source_expr': self.default_expression,
                                    'url_prefix': self.default_url_prefix
                                    },
                     'opinion': {
                                 'url': 'http://thestar.com.my/news/opinion/',
                                 'tags': ['opinion'],
                                 'language': self.default_language,
                                 'news_source_expr': self.default_expression,
                                 'url_prefix': self.default_url_prefix
                                 },
                     'maritime': {
                                  'url': 'http://thestar.com.my/maritime/',
                                  'tags': ['maritime','business'],
                                  'language': self.default_language,
                                  'news_source_expr': self.default_expression,
                                  'url_prefix': self.default_url_prefix
                                  }
                     }
    
    def sanitize(self, text):
        return text.replace('\u0092','\'').replace('\u0091','\'')
    
    def scrapItem(self, url=None, category=None):
        """
        Save news item
        """
        newsSource = NewsSource(self.default_database, self.default_collection)
        newsItem = NewsItem(self.default_database, self.default_collection)
        
        if(url == None):
            item = newsSource.findEmptyNewsItem()
            title = item['title']
            url = item['url']
            category = item['category']
            self._logger.debug("Item: "+title+" / "+category)
            
        details = self.sources[category]
        scraper = Scraper(url)
        scrap = scraper.get()
        for content in scrap.select(details['news_item_expr']):
            #print(str(content))
            newsItem.addNewsItem(url, content)
            try:
                newsItem.insertNewsItem()
                self._logger.debug(Stripper().strip(str(content)))
            except OperationFailure as of:
                pass
            finally:
                newsItem.resetNewsItem()
                
        info = "Item Scraped: "+url
        self._logger.info(info)
        print(info)
    
    def scrapSource(self, category, multi=False):
        """
        Save all news urls from one category into collection
        """
        source = category #Interim
        
        newsSource = NewsSource(self.default_database, self.default_collection)
        count = {'total': 0, 'scraped': 0}
        details = self.sources[source]
        
        scraper = Scraper(details['url'])
        scrap = scraper.get()
        self._logger.debug("Section: "+source)
        for news in scrap.select(details['news_source_expr']):
            #title = str(news.contents)
            url = details['url_prefix'] + news['href']
            title = self.sanitize(news.contents[0])
            category = source
            tags = details['tags']
            language = details['language']
            newsSource.addNewsSource(url, title, category, tags, language)
            count['total'] = count['total'] + 1
            self._logger.debug(count['total'])
            self._logger.debug(url)
            self._logger.debug(title)
            try:
                newsSource.insertNewsSources()
                count['scraped'] = count['scraped'] + 1
            except OperationFailure as of:
                self._logger.error("Skipped - "+str(of))
                pass
            finally:
                newsSource.resetNewsSources()
                
        if multi is False:
            info = "Total Items Scraped: "+str(count['scraped'])+"/"+str(count['total'])
            self._logger.info(info)
            print(info)
        else:
            return count
    
    def scrapSources(self):
        """
        Save all news urls from all news sources into collection
        """
        count = {'total': 0, 'scraped': 0}
        for source in self.sources:
            multi = True
            r = self.scrapSource(source, multi)
            count['total'] = count['total'] + r['total']
            count['scraped'] = count['scraped'] + r['scraped']
        
        info = "Total Items Scraped: "+str(count['scraped'])+"/"+str(count['total'])
        self._logger.info(info)
        print(info)
    
    def __del__(self):
        pass