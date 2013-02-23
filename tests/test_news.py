import unittest
from newsable import NewsSource
from newsable.news import MySinchew

class Test_newsTestCase(unittest.TestCase):
    def setUp(self):
        self.news = NewsSource()
        
    def tearDown(self):
        self.news = None
    
    def test_set_unique(self):
        newsSource = NewsSource('news','mySinchew')
        newsSource.setUnique('url')
    
    def test_news(self):
        news = MySinchew()
        news.scrapSources()
        
    #def test_test_news(self):
    #    result = self.news.findOne()
    #    print(result['name'])
    #    self.assertIsNotNone(result)
    
    #def test_test_news_rename(self):
    #    r = self.news.rename({"name": "one"}, {"roman": "romanized"})
    #    self.assertIsNotNone(r)
        
    #def test_test_newsItem_insert(self):
    #    self.news.addNewsItem('http://one.com', ["news"], ["one.com","nation"], 'en')
    #    self.news.addNewsItem('http://two.com', ["news"], ["two.com","nation"], 'en')
    #    self.assertIsNotNone(self.news.insertNewsItems())
        #print(self.news)
    
    #def test_test_newsItem_id(self):
    #    r = self.news.findOne({'category': ['news']})
    #    print('_id: '+str(r['_id']))
        
    #def test_test_news_find(self):
    #    #r = self.news.find({'_id': '12345'})
    #    r = self.news.find()
    #    self.assertIsNot(r.count(), 0)
    #    #self.assertIsNotNone(r)
    #    for item in r:
    #        print('item: ' + str(item)) 
        
if __name__ == '__main__':
    unittest.main()