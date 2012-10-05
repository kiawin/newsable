from mongoengine import *
import datetime
from mongo.News import *

class NewStraitsTimesNewsSource(Document, NewsSource):
    """ News Source Collection """

class NewStraitsTimesNewsItem(Document, NewsItem):
    """ News Item Collection """