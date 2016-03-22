import webapp2
import jinja2
import os
from google.appengine.api import memcache
from google.appengine.ext import db


class Pages(db.Model):
    url = db.StringProperty(required = True)
    user = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def get_pages(update = False):
        pages = memcache.get('pages')
        if pages is None or update:
            pages = db.GqlQuery("select * from Pages order by created ASC")
            memcache.set('pages', pages)
        return pages
    @classmethod
    def get_content(self,url):
        pages = db.GqlQuery("select * from Pages order by created DESC")
        for page in pages:
            if page.url==url:
                return page.content
        return ""

