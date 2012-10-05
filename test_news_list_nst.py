#!/usr/bin/env python

import unittest
from news.NewStraitsTimes import NewStraitsTimes

class TestNewsListNewsStraitsTimes(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.nst = NewStraitsTimes()
        #self.nst.purge()
    
    def test_list_nation(self):
        """ Get nst news listings """
        self.nst.list('nation')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_politics(self):
        """ Get nst news listings """
        self.nst.list('politics')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_extras(self):
        """ Get nst news listings """
        self.nst.list('extras')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_umno(self):
        """ Get nst news listings """
        self.nst.list('umno')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_metro_north(self):
        """ Get nst news listings """
        self.nst.list('metro-north')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_johor(self):
        """ Get nst news listings """
        self.nst.list('metro-johor')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_central(self):
        """ Get nst news listings """
        self.nst.list('metro-central')
        urls = self.nst.news_urls
        self.assertNotEqual(len(urls),0)
        self.nst.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()