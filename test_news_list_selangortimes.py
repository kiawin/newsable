#!/usr/bin/env python

import unittest
from news.SelangorTimes import SelangorTimes

class TestNewsListSelangorTimes(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.selangortimes = SelangorTimes()
        #self.selangortimes.purge()
    
    def test_list_metro_selangor(self):
        """ Get selangortimes news listings """
        self.selangortimes.list('metro-selangor')
        urls = self.selangortimes.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangortimes.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_opinion(self):
        """ Get selangortimes news listings """
        self.selangortimes.list('opinion')
        urls = self.selangortimes.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangortimes.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_culture(self):
        """ Get selangortimes news listings """
        self.selangortimes.list('culture')
        urls = self.selangortimes.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangortimes.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_insight(self):
        """ Get selangortimes news listings """
        self.selangortimes.list('insight')
        urls = self.selangortimes.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangortimes.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()