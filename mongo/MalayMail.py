from mongoengine import *
import datetime
from mongo.News import *

class MalayMailNewsSource(Document, NewsSource):
    """ News Source Collection """
    
class MalayMailNewsItem(Document, NewsItem):
    """ News Item Collection """