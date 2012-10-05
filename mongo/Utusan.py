from mongoengine import *
import datetime
from mongo.News import *

class UtusanNewsSource(Document, NewsSource):
    """ News Source Collection """
    
class UtusanNewsItem(Document, NewsItem):
    """ News Item Collection """