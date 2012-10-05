#!/usr/bin/env python

import unittest
from news.FreeMalaysiaToday import FreeMalaysiaToday

class TestNewsListFreeMalaysiaToday(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.fmt = FreeMalaysiaToday()
        #self.fmt.purge()
    
    def test_list_nation(self):
        """ Get fmt news listings """
        self.fmt.list('nation')
        urls = self.fmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.fmt.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_opinion(self):
        """ Get fmt news listings """
        self.fmt.list('opinion')
        urls = self.fmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.fmt.save()
        print 'Total URL(s) retrieved: ', len(urls)
              
    def test_list_business(self):
        """ Get fmt news listings """
        self.fmt.list('business')
        urls = self.fmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.fmt.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
            
        
if __name__ == '__main__':
    unittest.main()