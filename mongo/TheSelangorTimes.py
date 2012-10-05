from mongoengine import *
import datetime
from mongo.News import *

class TheSelangorTimesNewsSource(Document,NewsSource):
    """ News Source Collection """
    
class TheSelangorTimesNewsItem(Document,NewsItem):
    """ News Item Collection """
    