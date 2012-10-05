from mongoengine import *
import datetime
from mongo.News import *

class MySinchewNewsSource(Document, NewsSource):
    """ News Source Collection """
    
class MySinchewNewsItem(Document, NewsItem):
    """ News Item Collection """