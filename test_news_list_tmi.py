#!/usr/bin/env python

import unittest
from news.TheMalaysianInsider import TheMalaysianInsider

class TestNewsListTheMalaysianInsider(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.tmi = TheMalaysianInsider()
        #self.tmi.purge()
    
    def test_list_nation(self):
        """ Get tmi news listings """
        self.tmi.list('nation')
        urls = self.tmi.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmi.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get tmi news listings """
        self.tmi.list('business')
        urls = self.tmi.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmi.save()
        print 'Total URL(s) retrieved: ', len(urls)
 
    def test_list_bahasa(self):
        """ Get tmi news listings """
        self.tmi.list('bahasa')
        urls = self.tmi.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmi.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_opinion(self):
        """ Get tmi news listings """
        self.tmi.list('opinion')
        urls = self.tmi.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmi.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
if __name__ == '__main__':
    unittest.main()