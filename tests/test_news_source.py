import unittest

from newsable.news import Bernama
from newsable.news import BorneoPost
from newsable.news import FreeMalaysiaToday
from newsable.news import IpohEcho
from newsable.news import TheMalaysianInsider
from newsable.news import TheStar
from newsable.news import TheSunDaily

class TestNewsSource(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def bernama(self):
        news = Bernama()
        news.scrapSource('metro-south')

    def borneoPost(self):
        news = BorneoPost()
        news.scrapSource('nation')
    
    def freeMalaysiaToday(self):
        news = FreeMalaysiaToday()
        news.scrapSource('nation')
        
    def ipohEcho(self):
        news = IpohEcho()
        news.scrapSource('metro-ipoh')

    def theMalaysianInsider(self):
        news = TheMalaysianInsider()
        news.scrapSource('nation')
    
    def theStar(self):
        news = TheStar()
        news.scrapSource('nation')
    
    def theSunDaily(self):
        news = TheSunDaily()
        news.scrapSource('nation')
    
if __name__ == '__main__':
    #unittest.main()
    tests = ['ipohEcho']
    testClass = TestNewsSource
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)