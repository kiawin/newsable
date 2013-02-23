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
from newsable.news import TheMalaysianInsider
from newsable.news import TheMalaysianTimes
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

    def malayMail(self):
        news = MalayMail()
        news.scrapSource('nation')

    def malaysiaChronicle(self):
        news = MalaysiaChronicle()
        news.scrapSource('politics')

    def malaysiaKini(self):
        news = MalaysiaKini()
        news.scrapSource('nation-bm')

    def mySinchew(self):
        news = MySinchew()
        news.scrapSource('nation')

    def newStraitsTimes(self):
        news = NewStraitsTimes()
        news.scrapSource('nation')

    def selangorku(self):
        news = Selangorku()
        news.scrapSource('metro-selangor')

    def selangorTimes(self):
        news = SelangorTimes()
        #news.scrapSource('metro-selangor')
        #news.scrapSource('opinion')
        news.scrapSource('insight')
        
    def theMalaysianInsider(self):
        news = TheMalaysianInsider()
        news.scrapSource('opinion')
        
    def theMalaysianTimes(self):
        news = TheMalaysianTimes()
        news.scrapSource('nation')
            
    def theStar(self):
        news = TheStar()
        news.scrapSource('nation')
    
    def theSunDaily(self):
        news = TheSunDaily()
        news.scrapSource('nation')
    
if __name__ == '__main__':
    #unittest.main()
    tests = ['theMalaysianTimes']
    testClass = TestNewsSource
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)