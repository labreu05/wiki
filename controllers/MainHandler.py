from controllers.Handler import Handler
from models.pages import Pages
from google.appengine.ext import db
from google.appengine.api import memcache
from models.history import History

class MainHandler(Handler):
    def get(self,url):
        found = False
        v = self.request.get("v")
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
                if v:
                    versions = History.get_versions(url)
                    for version in versions:
                        if str(version.version) == v:
                            match.content = version.content
                            found = True
                    if not found:
                        self.redirect(url)
                memcache.set('Last_Page', url)
                self.render("Page.html",content=match.content,user=user,edit_url="_edit"+url,history_url="_history"+url)
            else:
                self.redirect('/_edit'+ url)
    	else:
            self.redirect('/_edit'+ url)