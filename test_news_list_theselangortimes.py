#!/usr/bin/env python

import unittest
from news.TheSelangorTimes import TheSelangorTimes

class TestNewsListTheSelangorTimes(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.tst = TheSelangorTimes()
        #self.tst.purge()
    
    def test_list_nation(self):
        """ Get tst news listings """
        self.tst.list('nation')
        urls = self.tst.news_urls
        self.assertNotEqual(len(urls),0)
        self.tst.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_nation_bm(self):
        """ Get tst news listings """
        self.tst.list('nation-bm')
        urls = self.tst.news_urls
        self.assertNotEqual(len(urls),0)
        self.tst.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get tst news listings """
        self.tst.list('business')
        urls = self.tst.news_urls
        self.assertNotEqual(len(urls),0)
        self.tst.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_ge13(self):
        """ Get tst news listings """
        self.tst.list('ge13')
        urls = self.tst.news_urls
        self.assertNotEqual(len(urls),0)
        self.tst.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_opinion(self):
        """ Get tst news listings """
        self.tst.list('opinion')
        urls = self.tst.news_urls
        self.assertNotEqual(len(urls),0)
        self.tst.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()