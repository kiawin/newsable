#!/usr/bin/env python

import unittest
from news.Bernama import Bernama

class TestNewsListBernama(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.bernama = Bernama()
        #self.bernama.purge()
    
    def test_list_nation(self):
        """ Get bernama news listings """
        self.bernama.list('nation')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_politics(self):
        """ Get bernama news listings """
        self.bernama.list('politics')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get bernama news listings """
        self.bernama.list('business')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_features(self):
        """ Get bernama news listings """
        self.bernama.list('features')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_1malaysia(self):
        """ Get bernama news listings """
        self.bernama.list('1malaysia')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_metro_north(self):
        """ Get bernama news listings """
        self.bernama.list('metro-north')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_east(self):
        """ Get bernama news listings """
        self.bernama.list('metro-east')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_south(self):
        """ Get bernama news listings """
        self.bernama.list('metro-south')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_central(self):
        """ Get bernama news listings """
        self.bernama.list('metro-central')
        urls = self.bernama.news_urls
        self.assertNotEqual(len(urls),0)
        self.bernama.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()