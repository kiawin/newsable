from mongoengine import *
import datetime
from mongo.News import *

class TheSunDailyNewsSource(Document,NewsSource):
    """ News Source Collection """
    
class TheSunDailyNewsItem(Document,NewsItem):
    """ News Item Collection """
    