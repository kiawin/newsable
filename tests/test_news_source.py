import unittest
from newsable.news import TheStar
from newsable.news import Bernama
from newsable.news import TheSunDaily
from newsable.news import BorneoPost

class Test_news_sourceTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_news_source_theborneopost(self):
        theBorneoPost = BorneoPost()
        theBorneoPost.scrapSource('nation')
    
    #def test_news_source_thesundaily(self):
    #    theSunDaily = TheSunDaily()
    #    theSunDaily.scrapSource('nation')
    
    #def test_news_source_thestar(self):
    #    theStar = TheStar()
    #    theStar.scrapSource('nation')
    
    #def test_news_source_bernama(self):
    #    bernama = Bernama()
    #    bernama.scrapSource('metro-south')
    
if __name__ == '__main__':
    unittest.main()