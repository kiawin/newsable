from mongoengine import *
import datetime
from mongo.News import *

class TheStarNewsSource(Document, NewsSource):
    """ News Source Collection """

class TheStarNewsItem(Document, NewsItem):
    """ News Item Collection """