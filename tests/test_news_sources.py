import unittest

from newsable.news import Bernama
from newsable.news import BorneoPost
from newsable.news import FreeMalaysiaToday
from newsable.news import IpohEcho
from newsable.news import MalayMail
from newsable.news import MalaysiaChronicle
from newsable.news import MalaysiaKini
from newsable.news import MySinchew
from newsable.news import TheStar
from newsable.news import TheSunDaily

class TestNewsSources(unittest.TestCase):
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

    def ipohEcho(self):
        news = IpohEcho()
        news.scrapSources()

    def malayMail(self):
        news = MalayMail()
        news.scrapSources()

    def malaysiaChronicle(self):
        news = MalaysiaChronicle()
        news.scrapSources()
    
    def malaysiaKini(self):
        news = MalaysiaKini()
        news.scrapSources()
    
    def mySinchew(self):
        news = MySinchew()
        news.scrapSources()
            
    def theSunDaily(self):
        news = TheSunDaily()
        news.scrapSources()
    
    def theStar(self):
        news = TheStar()
        news.scrapSources()
            
if __name__ == '__main__':
    #unittest.main()
    tests = ['mySinchew']
    testClass = TestNewsSources
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)