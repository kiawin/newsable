#!/usr/bin/env python

import unittest
from news.Utusan import Utusan

class TestNewsListUtusan(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.utusan = Utusan()
        #self.utusan.purge()
    
    def test_list_nation(self):
        """ Get utusan news listings """
        self.utusan.list('nation')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_politics(self):
        """ Get utusan news listings """
        self.utusan.list('politics')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_parliament(self):
        """ Get utusan news listings """
        self.utusan.list('parliament')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_crime(self):
        """ Get utusan news listings """
        self.utusan.list('crime')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)        

    def test_list_courts(self):
        """ Get utusan news listings """
        self.utusan.list('courts')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_special(self):
        """ Get utusan news listings """
        self.utusan.list('special')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_business(self):
        """ Get utusan news listings """
        self.utusan.list('business')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_education(self):
        """ Get utusan news listings """
        self.utusan.list('education')
        urls = self.utusan.news_urls
        self.assertNotEqual(len(urls),0)
        self.utusan.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
if __name__ == '__main__':
    unittest.main()