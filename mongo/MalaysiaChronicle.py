from mongoengine import *
import datetime
from mongo.News import *

class MalaysiaChronicleNewsSource(Document, NewsSource):
    """ News Source Collection """

class MalaysiaChronicleNewsItem(Document, NewsItem):
    """ News Item Collection """