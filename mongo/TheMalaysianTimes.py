from mongoengine import *
import datetime
from mongo.News import *

class TheMalaysianTimesNewsSource(Document,NewsSource):
    """ News Source Collection """
    
class TheMalaysianTimesNewsItem(Document,NewsItem):
    """ News Item Collection """
    