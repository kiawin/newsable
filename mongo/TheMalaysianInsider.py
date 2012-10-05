from mongoengine import *
import datetime
from mongo.News import *

class TheMalaysianInsiderNewsSource(Document, NewsSource):
    """ News Source Collection """

class TheMalaysianInsiderNewsItem(Document, NewsItem):
    """ News Item Collection """