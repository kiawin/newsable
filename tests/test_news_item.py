import unittest
from newsable.news import TheStar
from newsable.news import Bernama
from newsable.news import TheSunDaily
from newsable.news import BorneoPost

class Test_news_itemTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_news_item_theborneopost(self):
        theBorneoPost = BorneoPost()
        url = None
        category = None
        theBorneoPost.scrapItem(url, category)

    #def test_news_item_thesundaily(self):
    #    theSunDaily = TheSunDaily()
    #    url = None
    #    category = None
    #    theSunDaily.scrapItem(url, category)

    #def test_news_item_bernama(self):
    #    bernama = Bernama()
    #    url = None
    #    category = None
    #    bernama.scrapItem(url, category)
    
    #def test_news_item_thestar(self):
    #    theStar = TheStar()
    #    url = None
    #    category = None
    #    theStar.scrapItem(url, category)
    
if __name__ == '__main__':
    unittest.main()