from mongoengine import *
import datetime
from mongo.News import *

class MalaysiaKiniNewsSource(Document, NewsSource):
    """ News Source Collection """
    
class MalaysiaKiniNewsItem(Document, NewsItem):
    """ News Item Collection """