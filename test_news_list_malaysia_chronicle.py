#!/usr/bin/env python

import unittest
from news.MalaysiaChronicle import MalaysiaChronicle

class TestNewsListMalaysiaChronicle(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.malaysiaChronicle = MalaysiaChronicle()
        #self.malaysiaChronicle.purge()
    
    def test_list_politics(self):
        """ Get malaysiaChronicle news listings """
        self.malaysiaChronicle.list('politics')
        urls = self.malaysiaChronicle.news_urls
        self.assertNotEqual(len(urls),0)
        self.malaysiaChronicle.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get malaysiaChronicle news listings """
        self.malaysiaChronicle.list('business')
        urls = self.malaysiaChronicle.news_urls
        self.assertNotEqual(len(urls),0)
        self.malaysiaChronicle.save()
        print 'Total URL(s) retrieved: ', len(urls)        

    def test_list_social(self):
        """ Get malaysiaChronicle news listings """
        self.malaysiaChronicle.list('social')
        urls = self.malaysiaChronicle.news_urls
        self.assertNotEqual(len(urls),0)
        self.malaysiaChronicle.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_featured(self):
        """ Get malaysiaChronicle news listings """
        self.malaysiaChronicle.list('featured')
        urls = self.malaysiaChronicle.news_urls
        self.assertNotEqual(len(urls),0)
        self.malaysiaChronicle.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()