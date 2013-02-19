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
    tests = ['malaysiaChronicle']
    testClass = TestNewsContentStrip
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)