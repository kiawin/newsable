import unittest
from newsable.news import TheStar

class Test_news_sourceTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    #def test_news_source_thestar(self):
    #    theStar = TheStar()
    #    theStar.scrapSource('nation')
    
    def test_news_sources_thestar(self):
        theStar = TheStar()
        theStar.scrapSources()
        
if __name__ == '__main__':
    unittest.main()