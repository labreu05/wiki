from controllers.Handler import Handler
from google.appengine.ext import db
from google.appengine.api import memcache

class LogOutHandler(Handler):
    def get(self):
    	long_url = self.request.url
    	url = long_url[long_url.rfind('/'):]
        user_id = str(self.request.cookies.get('user_id',None))
        users = db.GqlQuery("select * from Users")
        for user in users: 
            if str(user.cookie_code)==user_id:
                self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' %"")
            	self.redirect(str(memcache.get('Last_Page')))