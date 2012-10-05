from mongoengine import *
import datetime

class NewsSource():
    """ News Source Collection """
    
    url = URLField(required=True,unique=True)
    category = StringField(max_length=30)
    tags = ListField()
    language = StringField(max_length=3)
    created = DateTimeField(default=datetime.datetime.now)
    modified = DateTimeField(default=datetime.datetime.now)

class NewsItem():
    """ News Item Collection """
    
    url = URLField(required=True, unique=True)
    title = StringField(required=True, max_length=100)
    content = StringField(required=True)
    category = StringField(max_length=30)
    tags = ListField()
    language = StringField(max_length=3)
    created = DateTimeField(default=datetime.datetime.now)
    modified = DateTimeField(default=datetime.datetime.now)