#!/usr/bin/env python

import unittest
from news.MySinchew import MySinchew

class TestNewsListMySinchew(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.mysinchew = MySinchew()
        #self.mysinchew.purge()
    
    def test_list_nation(self):
        """ Get mysinchew news listings """
        self.mysinchew.list('nation')
        urls = self.mysinchew.news_urls
        self.assertNotEqual(len(urls),0)
        self.mysinchew.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_opinion(self):
        """ Get mysinchew news listings """
        self.mysinchew.list('opinion')
        urls = self.mysinchew.news_urls
        self.assertNotEqual(len(urls),0)
        self.mysinchew.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_mykampung(self):
        """ Get mysinchew news listings """
        self.mysinchew.list('metro-mykampung')
        urls = self.mysinchew.news_urls
        self.assertNotEqual(len(urls),0)
        self.mysinchew.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_features(self):
        """ Get mysinchew news listings """
        self.mysinchew.list('features')
        urls = self.mysinchew.news_urls
        self.assertNotEqual(len(urls),0)
        self.mysinchew.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get mysinchew news listings """
        self.mysinchew.list('business')
        urls = self.mysinchew.news_urls
        self.assertNotEqual(len(urls),0)
        self.mysinchew.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()