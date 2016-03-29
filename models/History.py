import webapp2
import jinja2
import os
from google.appengine.api import memcache
from google.appengine.ext import db

class History(db.Model):
    url = db.StringProperty(required = True)
    version = db.IntegerProperty(required = True)
    user = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def get_versions(self,url):
        versions = History.all().filter("url = ", url).order('-version')
        return versions