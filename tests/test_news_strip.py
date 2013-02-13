import unittest
from newsable import NewsItem
from newsable import Stripper

class Test_news_stripTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_news_item_thestar_trip(self):
        #url = 'http://thestar.com.my/news/story.asp?file=/2012/12/17/nation/20121217144240&sec=nation'
        #newsItem = NewsItem('news','theStar')
        url = 'http://www.thesundaily.my/news/572375'
        newsItem = NewsItem('news', 'theSunDaily')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
        
if __name__ == '__main__':
    unittest.main()