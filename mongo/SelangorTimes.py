from mongoengine import *
import datetime
from mongo.News import *

class SelangorTimesNewsSource(Document,NewsSource):
    """ News Source Collection """
    
class SelangorTimesNewsItem(Document,NewsItem):
    """ News Item Collection """
    