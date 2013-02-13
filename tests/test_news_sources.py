import unittest

from newsable.news import Bernama
from newsable.news import BorneoPost
from newsable.news import FreeMalaysiaToday
from newsable.news import TheStar
from newsable.news import TheSunDaily

class TestNewsSource(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def bernama(self):
        news = Bernama()
        news.scrapSources()
    
    def borneoPost(self):
        news = BorneoPost()
        news.scrapSources()

    def freeMalaysiaToday(self):
        news = FreeMalaysiaToday()
        news.scrapSources()
    
    def theSunDaily(self):
        news = TheSunDaily()
        news.scrapSources()
    
    def theStar(self):
        news = TheStar()
        news.scrapSources()
            
if __name__ == '__main__':
    #unittest.main()
    tests = ['theSunDaily']
    testClass = TestNewsSource
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)