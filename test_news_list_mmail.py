#!/usr/bin/env python

import unittest
from news.MalayMail import MalayMail

class TestNewsListMalayMail(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.mmail = MalayMail()
        #self.mmail.purge()
    
    def test_list_nation(self):
        """ Get mmail news listings """
        self.mmail.list('nation')
        urls = self.mmail.news_urls
        self.assertNotEqual(len(urls),0)
        self.mmail.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_business(self):
        """ Get mmail news listings """
        self.mmail.list('business')
        urls = self.mmail.news_urls
        self.assertNotEqual(len(urls),0)
        self.mmail.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_metro(self):
        """ Get mmail news listings """
        self.mmail.list('metro')
        urls = self.mmail.news_urls
        self.assertNotEqual(len(urls),0)
        self.mmail.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_opinion(self):
        """ Get mmail news listings """
        self.mmail.list('opinion')
        urls = self.mmail.news_urls
        self.assertNotEqual(len(urls),0)
        self.mmail.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
if __name__ == '__main__':
    unittest.main()