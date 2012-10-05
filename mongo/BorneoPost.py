from mongoengine import *
import datetime
from mongo.News import *

class BorneoPostNewsSource(Document, NewsSource):
    """ News Source Collection """

class BorneoPostNewsItem(Document, NewsItem):
    """ News Item Collection """