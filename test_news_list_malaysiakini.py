#!/usr/bin/env python

import unittest
from news.MalaysiaKini import MalaysiaKini

class TestNewsListMalaysiaKini(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.mkini = MalaysiaKini()
        #self.mkini.purge()
    
    def test_list_nation_bm(self):
        """ Get mkini news listings """
        self.mkini.list('nation-bm')
        urls = self.mkini.news_urls
        self.assertNotEqual(len(urls),0)
        self.mkini.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_bm(self):
        """ Get mkini news listings """
        self.mkini.list('columns-bm')
        urls = self.mkini.news_urls
        self.assertNotEqual(len(urls),0)
        self.mkini.save()
        print 'Total URL(s) retrieved: ', len(urls)
    
    def test_list_letters_bm(self):
        """ Get mkini news listings """
        self.mkini.list('letters-bm')
        urls = self.mkini.news_urls
        self.assertNotEqual(len(urls),0)
        self.mkini.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
        
if __name__ == '__main__':
    unittest.main()