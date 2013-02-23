from newsable import Scraper
from newsable import Logger
from newsable import Stripper

from newsable import NewsSource
from newsable import NewsItem

from pymongo.errors import OperationFailure

class News():
    '''
    News Scraper Class
    '''
    
    def __init__(self, news):
        '''
        Constructor
        '''
        self.logger = Logger(news).get()
        
        self.default_database = 'news'
        self.default_collection = news
        self.default_url_prefix = None
        self.append_url_prefix = False
        self.default_news_source_expression = None
        self.default_news_item_expression = None
        self.default_language = 'eng'

        self.sources = {}
    
    def sanitize(self, text):
        '''
        Sanitize text (Abstract method)
        '''
        return text
    
    def scrapItem(self, url=None, category=None):
        '''
        Save news item
        '''
        newsSource = NewsSource(self.default_database, self.default_collection)
        newsItem = NewsItem(self.default_database, self.default_collection)
        
        if(url == None):
            item = newsSource.findEmptyNewsItem()
            title = item['title']
            url = item['url']
            category = item['category']
            self.logger.debug("Item: "+title+" / "+category)
            
        details = self.sources[category]
        scraper = Scraper(url)
        scrap = scraper.get()
        
        #Include the possibility of scraping multiple elements as news content
        allNews = scrap.select(details['news_item_expr'])
        if len(allNews) > 1:
            content = " ".join(str(n) for n in allNews)
        else:
            content = allNews[0]
        #content = scrap.select(details['news_item_expr'])[0]
        
        newsItem.addNewsItem(url, content)
        try:
            newsItem.insertNewsItem()
            self.logger.debug(Stripper().strip(str(content)))
        except OperationFailure as of:
            pass
        finally:
            newsItem.resetNewsItem()
                
        info = "Item Scraped: "+url
        self.logger.info(info)
        print(info)
    
    def scrapSource(self, category, multi=False):
        '''
        Save all news urls from one category into collection
        '''
        source = category #Interim
        
        newsSource = NewsSource(self.default_database, self.default_collection)
        count = {'total': 0, 'scraped': 0}
        details = self.sources[source]
        
        scraper = Scraper(details['url'])
        scrap = scraper.get()
        self.logger.debug("Section: "+source)
        
        #For temporal - Testing only
        allNews = scrap.select(details['news_source_expr'])
        print('Size: '+str(len(allNews)))
        
        for news in scrap.select(details['news_source_expr']):
            #title = str(news.contents)
            if self.append_url_prefix is True:
                url = details['url_prefix'] + news['href']
            else:
                url = news['href']
            
            '''
            Customization to retrieve data
            (Temporary measure)
            '''
            if self._news == 'bernama':
                #title = str(news.font.b.contents[0])
                title = self.sanitize(list(news.descendants)[len(list(news.descendants))-1])
            else:
                title = self.sanitize(news.contents[0])
            
            print(self._news+" - Title: "+str(title))
            #print(self._news+" - Title: "+title)
            
            category = source
            tags = details['tags']
            language = details['language']
            newsSource.addNewsSource(url, title, category, tags, language)
            count['total'] = count['total'] + 1
            self.logger.debug(count['total'])
            self.logger.debug(url)
            self.logger.debug(title)
            try:
                newsSource.insertNewsSources()
                count['scraped'] = count['scraped'] + 1
            except OperationFailure as of:
                self.logger.error("Skipped - "+str(of))
                pass
            finally:
                newsSource.resetNewsSources()
                
        if multi is False:
            info = "Total Items Scraped: "+str(count['scraped'])+"/"+str(count['total'])
            self.logger.info(info)
            print(info)
        else:
            return count
    
    def scrapSources(self):
        '''
        Save all news urls from all news sources into collection
        '''
        count = {'total': 0, 'scraped': 0}
        for source in self.sources:
            multi = True
            r = self.scrapSource(source, multi)
            count['total'] = count['total'] + r['total']
            count['scraped'] = count['scraped'] + r['scraped']
        
        info = "Total Items Scraped: "+str(count['scraped'])+"/"+str(count['total'])
        self.logger.info(info)
        print(info)
    
    def __del__(self):
        pass
