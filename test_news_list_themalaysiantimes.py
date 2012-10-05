#!/usr/bin/env python

import unittest
from news.TheMalaysianTimes import TheMalaysianTimes

class TestNewsListTheMalaysianTimes(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.tmt = TheMalaysianTimes()
        #self.tmt.purge()
    
    def test_list_nation(self):
        """ Get tmt news listings """
        self.tmt.list('nation')
        urls = self.tmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmt.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_nation_bm(self):
        """ Get tmt news listings """
        self.tmt.list('nation-bm')
        urls = self.tmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmt.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get tmt news listings """
        self.tmt.list('business')
        urls = self.tmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmt.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_ge13(self):
        """ Get tmt news listings """
        self.tmt.list('ge13')
        urls = self.tmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmt.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_education(self):
        """ Get tmt news listings """
        self.tmt.list('education')
        urls = self.tmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmt.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_opinion(self):
        """ Get tmt news listings """
        self.tmt.list('opinion')
        urls = self.tmt.news_urls
        self.assertNotEqual(len(urls),0)
        self.tmt.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()