#!/usr/bin/env python

import unittest
from news.BorneoPost import BorneoPost

class TestNewsListBorneoPost(unittest.TestCase):
    """ Test Case for News Listings """
    
    def setUp(self):
        self.borneoPost = BorneoPost()
        #self.borneoPost.purge()

    def test_list_metro_sarawak(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('metro-sarawak')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)
            
    def test_list_nation(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('nation')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_sabah(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('metro-sabah')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_business(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('business')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_our_stand(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-our-stand')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_letters(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-letters')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_peace_corps(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-peace-corps')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_uncle_di(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-uncle-di')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_tired_eye(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-tired-eye')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_perspective(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-perspective')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_singhealth(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-singhealth')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_others(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-others')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_youth_talents(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-youth-talents')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_local_entrepreneurs(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-local-entrepreneurs')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_paul_sir(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-paul-sir')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_hornbill_corner(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-hornbill-corner')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_edge_of_town(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-edge-of-town')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_columns_and_so(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('columns-and-so')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_sarawak_bm(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('metro-sarawak-bm')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_nation_bm(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('nation-bm')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_sarawak_iban(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('metro-sarawak-iban')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)

    def test_list_metro_sabah_bm(self):
        """ Get borneoPost news listings """
        self.borneoPost.list('metro-sabah-bm')
        urls = self.borneoPost.news_urls
        self.assertNotEqual(len(urls),0)
        self.borneoPost.save()
        print 'Total URL(s) retrieved: ', len(urls)
                        
if __name__ == '__main__':
    unittest.main()