#!/usr/bin/env python

import unittest
from news.IpohEcho import IpohEcho

class TestNewsListIpohEcho(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.ipohEcho = IpohEcho()
        #self.ipohEcho.purge()
    
    def test_list_metro_ipoh(self):
        """ Get ipohEcho news listings """
        self.ipohEcho.list('metro-ipoh')
        urls = self.ipohEcho.news_urls
        self.assertNotEqual(len(urls),0)
        self.ipohEcho.save()
        print 'Total URL(s) retrieved: ', len(urls)
                
if __name__ == '__main__':
    unittest.main()