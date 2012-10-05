#!/usr/bin/env python

import unittest
from news.TheSunDaily import TheSunDaily

class TestNewsListTheSunDaily(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.thesundaily = TheSunDaily()
        #self.thesundaily.purge()
    
    def test_list_nation(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('nation')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_business(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('business')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_property(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('property')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_media_marketing(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('media-marketing')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)
        
    def test_list_education(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('education')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('metro')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_opinion(self):
        """ Get thesundaily news listings """
        self.thesundaily.list('opinion')
        urls = self.thesundaily.news_urls
        self.assertNotEqual(len(urls),0)
        self.thesundaily.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()