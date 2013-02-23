import unittest

from newsable.news import Bernama
from newsable.news import BorneoPost
from newsable.news import FreeMalaysiaToday
from newsable.news import IpohEcho
from newsable.news import MalayMail
from newsable.news import MalaysiaChronicle
from newsable.news import MalaysiaKini
from newsable.news import MySinchew
from newsable.news import NewStraitsTimes
from newsable.news import Selangorku
from newsable.news import SelangorTimes
from newsable.news import TheStar
from newsable.news import TheSunDaily

class TestNewsItem(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def bernama(self):
        news = Bernama()
        url = None
        category = None
        news.scrapItem(url, category)
            
    def borneoPost(self):
        news = BorneoPost()
        url = None
        category = None
        news.scrapItem(url, category)

    def freeMalaysiaToday(self):
        news = FreeMalaysiaToday()
        url = None
        category = None
        news.scrapItem(url, category)

    def ipohEcho(self):
        news = IpohEcho()
        url = None
        category = None
        news.scrapItem(url, category)

    def malayMail(self):
        news = MalayMail()
        url = None
        category = None
        news.scrapItem(url, category)

    def malaysiaChronicle(self):
        news = MalaysiaChronicle()
        url = None
        category = None
        news.scrapItem(url, category)

    def malaysiaKini(self):
        news = MalaysiaKini()
        url = None
        category = None
        news.scrapItem(url, category)

    def mySinchew(self):
        news = MySinchew()
        url = None
        category = None
        news.scrapItem(url, category)

    def newStraitsTimes(self):
        news = NewStraitsTimes()
        url = None
        category = None
        news.scrapItem(url, category)

    def selangorku(self):
        news = Selangorku()
        url = None
        category = None
        news.scrapItem(url, category)

    def selangorTimes(self):
        news = SelangorTimes()
        url = None
        category = None
        news.scrapItem(url, category)
        
    def theStar(self):
        news = TheStar()
        url = None
        category = None
        news.scrapItem(url, category)

    def theSunDaily(self):
        news = TheSunDaily()
        url = None
        category = None
        news.scrapItem(url, category)
    
if __name__ == '__main__':
    #unittest.main()
    tests = ['selangorTimes']
    testClass = TestNewsItem
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)