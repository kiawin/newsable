#!/usr/bin/env python

import mechanize
import lxml.html
import sys, logging
        
class News():
    """ Base Class for News Scrapper """ 
    
    def __init__(self):
        """ Constructor """
        
        #self.urls = {}
        #self.default_url_prefix = ''
        #self.tags = ''
        #self.exprs = {'default': ''}
        self.config = {}
        #self.expr = ''
        self.news_urls = []
        #elf.news_titles = []
        self.news_category = ''
        self.list_css = False
        self.list_xpath = False
        
    def __getExpr(self):
        """ get expr """
        
        return self.config[self.news_category]['expr']
        #if self.news_category in self.exprs:
        #    return self.exprs[self.news_category]
        #else:
        #    return self.exprs['default']
        
    def useXPath(self):
        """ Use XPath to traverse HTML """
        
        self.list_xpath = True
        self.list_css = False
        
    def useCSSSelector(self):
        """ Use CSSSelector to traverse HTML """
        
        self.list_css = True
        self.list_xpath = False
        
    def list(self,news_category):
        """ list news """

        self.news_category = news_category
        expr = self.__getExpr()

        logger = logging.getLogger("mechanize")
        logger.addHandler(logging.StreamHandler(sys.stdout))
        #logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.INFO)
        
        br = mechanize.Browser()
        br.set_handle_robots(False)
        #br.set_debug_responses(True)
        #Utusan has invalid meta-refresh attribute value
        br.set_handle_refresh(False)
        #Bernama blocks mechanize/urllib2
        br.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')]
        br.open(self.config[self.news_category]['url'])
        resp = br.response()
        #print resp.read()
        
        #req = mechanize.Request(self.config[self.news_category]['url'])
        #resp = mechanize.urlopen(req)
        
        html = lxml.html.parse(resp).getroot()
        if self.list_css == True:
            link_targets = [link.attrib.get('href') for link in html.cssselect(expr)]
        elif self.list_xpath == True:
            link_targets = [link.attrib.get('href') for link in html.xpath(expr)]
        self.news_urls = link_targets