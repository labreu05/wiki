from controllers.Handler import Handler
from google.appengine.ext import db
from models.users import Users


class LogInHandler(Handler):
    def get(self):
        self.render("LogIn.html")
    def post(self):
        exist = False
        errores = {}  
        username = self.request.get("username")
        password = self.request.get("password")
        user = db.GqlQuery("select * from Users")
        for u in user: 
            if u.username==username:
                exist = True
                if u.password==password:
                    self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' %str(u.cookie_code))
                    self.redirect('/')
                else:
                    errores['p1_error']="Datos Invalidos"
                    self.render("LogIn.html", **errores)
        if exist==False:
            errores['u_error']="Usuario No Existe"
            self.render("LogIn.html", **errores)