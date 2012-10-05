#!/usr/bin/env python

import unittest
from news.Selangorku import Selangorku

class TestNewsListSelangorku(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.selangorku = Selangorku()
        #self.selangorku.purge()
    
    def test_list_state(self):
        """ Get selangorku news listings """
        self.selangorku.list('state')
        urls = self.selangorku.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangorku.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_mb_news(self):
        """ Get selangorku news listings """
        self.selangorku.list('mb-news')
        urls = self.selangorku.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangorku.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_mb_programme(self):
        """ Get selangorku news listings """
        self.selangorku.list('mb-programme')
        urls = self.selangorku.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangorku.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_mb_politics(self):
        """ Get selangorku news listings """
        self.selangorku.list('mb-politics')
        urls = self.selangorku.news_urls
        self.assertNotEqual(len(urls),0)
        self.selangorku.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()