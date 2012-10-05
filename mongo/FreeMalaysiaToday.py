from mongoengine import *
import datetime
from mongo.News import *

class FreeMalaysiaTodayNewsSource(Document, NewsSource):
    """ News Source Collection """

class FreeMalaysiaTodayNewsItem(Document, NewsItem):
    """ News Item Collection """