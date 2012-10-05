from mongoengine import *
import datetime
from mongo.News import *

class IpohEchoNewsSource(Document, NewsSource):
    """ News Source Collection """

class IpohEchoNewsItem(Document, NewsItem):
    """ News Item Collection """