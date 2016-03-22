from controllers.Handler import Handler
from models.pages import Pages
from google.appengine.ext import db
from google.appengine.api import memcache

class MainHandler(Handler):
    def get(self,url):
        match = None
        user =str(self.request.cookies.get('user_id')).split("|")[0]
        if user=="None":
            user = ""
    	pages = Pages.get_pages() 
    	if pages:
            for page in pages:
                if page.url==url:
                    match = page                   
            if match:
                memcache.set('Last_Page', url)
                self.render("Page.html",content=match.content,user=user,edit_url="_edit"+url)
            else:
                self.redirect('/_edit'+ url)
    	else:
            self.redirect('/_edit'+ url)