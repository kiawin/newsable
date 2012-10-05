from mongoengine import *
import datetime
from mongo.News import *

class BernamaNewsSource(Document,NewsSource):
    """ News Source Collection """
    
class BernamaNewsItem(Document,NewsItem):
    """ News Item Collection """
    