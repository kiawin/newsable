import unittest
from newsable.news import TheStar

from newsable.DB import MongoDB

class Test_news_uniqueTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_news_set_theborneopost_unique(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theBorneoPost')
        db.setUnique('url')
        db.__del__()
    
    def test_news_set_thesundaily_unique(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theSunDaily')
        db.setUnique('url')
        db.__del__()
    
    def test_news_set_bernama_unique(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','bernama')
        db.setUnique('url')
        db.__del__()
    
    def test_news_set_thestar_uniques(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theStar')
        db.setUnique('url')
        db.__del__()
           
if __name__ == '__main__':
    unittest.main()