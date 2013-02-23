import unittest
from newsable import NewsItem
from newsable import Stripper

class TestNewsContentStrip(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def ipohEcho(self):
        url = 'http://ipohecho.com.my/v2/2013/02/16/flood-mitigation-projects-whats-been-done/'
        newsItem = NewsItem('news', 'ipohEcho')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
    
    def malayMail(self):
        url = 'http://www.mmail.com.my/story/bukit-aman-task-force-probe-info-dept-hacking-48005'
        newsItem = NewsItem('news', 'malayMail')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
    
    def malaysiaChronicle(self):
        url = 'http://www.malaysia-chronicle.com/index.php?option=com_k2&view=item&id=57921:have-you-gone-senile-karpal?-apologize-immediately-to-jui-meng&Itemid=2'
        newsItem = NewsItem('news', 'malaysiaChronicle')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))    
    
    def malaysiaKini(self):
        url = 'http://www.malaysiakini.com/news/221767'
        newsItem = NewsItem('news', 'malaysiaKini')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))

    def mySinchew(self):
        url = 'http://www.mysinchew.com/node/83148'
        newsItem = NewsItem('news', 'mySinchew')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))

    def newStraitsTimes(self):
        url = 'http://www.nst.com.my/nation/general/indians-now-backing-bn-says-dpm-1.221564'
        newsItem = NewsItem('news', 'newStraitsTimes')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))

    def selangorku(self):
        url = 'http://www.selangorku.com/?p=23146'
        newsItem = NewsItem('news', 'selangorku')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))

    def selangorTimes(self):
        #url = 'http://www.selangortimes.com/index.php?section=news&permalink=20130207180252-mindef-spending-raises-eyebrows'
        url = 'http://www.selangortimes.com/index.php?section=culture&permalink=20130222113339-a-chance-to-dazzle-like-teresa-teng'
        newsItem = NewsItem('news', 'selangorTimes')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
        #content = Stripper().strip(r['content'])
        #print(" ".join(content))
        
    def theMalaysianInsider(self):
        url = 'http://www.themalaysianinsider.com/bahasa/article/mb-terengganu-akui-kontraktor-lemah-punca-bumbung-runtuh-kali-kedua/'
        newsItem = NewsItem('news','theMalaysianInsider')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
    
    def theMalaysianTimes(self):
        url = 'http://www.themalaysiantimes.com.my/?p=62774'
        newsItem = NewsItem('news','theMalaysianTimes')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
    
    def theStar(self):
        url = 'http://thestar.com.my/news/story.asp?file=/2012/12/17/nation/20121217144240&sec=nation'
        newsItem = NewsItem('news','theStar')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
    
    def theSunDaily(self):
        url = 'http://www.thesundaily.my/news/572375'
        newsItem = NewsItem('news', 'theSunDaily')
        r = newsItem.findOne({'url': url})
        print(Stripper().strip(r['content']))
        
if __name__ == '__main__':
    #unittest.main()
    tests = ['theMalaysianTimes']
    testClass = TestNewsContentStrip
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)