#!/usr/bin/env python

import unittest
from news.TheStar import TheStar

class TestNewsListTheStar(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.thestar = TheStar()
        #self.thestar.purge()
    
    def test_list_nation(self):
        """ Get thestar news listings """
        self.thestar.list('nation')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_sarawak(self):
        """ Get thestar news listings """
        self.thestar.list('sarawak')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_business(self):
        """ Get thestar news listings """
        self.thestar.list('business')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_central(self):
        """ Get thestar news listings """
        self.thestar.list('metro-central')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_metro_north(self):
        """ Get thestar news listings """
        self.thestar.list('metro-north')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_metro_biz(self):
        """ Get thestar news listings """
        self.thestar.list('metro-biz')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_metro_southneast(self):
        """ Get thestar news listings """
        self.thestar.list('metro-southneast')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_perak(self):
        """ Get thestar news listings """
        self.thestar.list('metro-perak')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_courts(self):
        """ Get thestar news listings """
        self.thestar.list('courts')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_parliament(self):
        """ Get thestar news listings """
        self.thestar.list('parliament')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_opinion(self):
        """ Get thestar news listings """
        self.thestar.list('opinion')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_maritime(self):
        """ Get thestar news listings """
        self.thestar.list('maritime')
        urls = self.thestar.news_urls
        self.assertNotEqual(len(urls),0)
        self.thestar.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    
if __name__ == '__main__':
    unittest.main()