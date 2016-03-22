import webapp2
import jinja2
import os
from google.appengine.api import memcache
from google.appengine.ext import db


class Users(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty(required = False)
    cookie_code = db.StringProperty(required = False)

    @classmethod
    def get_user(self,cookie_code):
	    user = db.GqlQuery("select * from Users where cookie_code='%s'" %cookie_code)
	    if user:
	    	return str(user)
	    else:
	    	return ""