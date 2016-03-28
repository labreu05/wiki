from controllers.Handler import Handler
from google.appengine.ext import db
from models.users import Users
from models.history import History
from models.pages import Pages


class HistoryHandler(Handler):
    def get(self,url):
        user = str(self.request.cookies.get('user_id').split("|")[0])
        long_url = self.request.url
        url = long_url[long_url.rfind('/'):]
        versions = History.get_versions(url)
        if versions.count() == 0:
            self.redirect(url)
        else:
            self.render("History.html",user=user,versions=versions)
            



        