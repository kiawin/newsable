from mongoengine import *
import datetime
from mongo.News import *

class SelangorkuNewsSource(Document,NewsSource):
    """ News Source Collection """
    
class SelangorkuNewsItem(Document,NewsItem):
    """ News Item Collection """
    