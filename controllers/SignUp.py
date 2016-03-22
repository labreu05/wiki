import re
import hashlib
from controllers.Handler import Handler
from google.appengine.ext import db
from models.pages import Pages
from models.users import Users


def validar_usuario(username=""):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    u_error=""
    if username:
            users = db.GqlQuery("select * from Users")
            for user in users:
                if user.username==username:
                    u_error="El Usuario Ya Existe"
            if USER_RE.match(username):
                return u_error
            else:
                u_error="Usuario No Valido"
    else:
            u_error="Usuario Obligatorio"
    return u_error

def validar_contrasena(password=""):
    p1_error=""
    if password:
        return p1_error
    else:
        p1_error="Password Obligatorio"
    return p1_error

def validar_contrasenas(password="",verify=""):
    p2_error=""
    if verify:
        if password==verify:
            return p2_error
        else:
            p2_error="No Coinciden"
    else:
        p2_error = "Campo Obligatorio"
    return p2_error

def validar_email(email=""):
    e_error= ""
    if email:
        e_ver = re.compile(r"/^\S+@\S+\.\S+$/")
        if e_ver.match(email):
            return e_error
        else:
            e_error="Email Invalido"
    return e_error

def validar_datos(username="",password="",verify="",email=""):
    u=validar_usuario(username)
    p=validar_contrasena(password)
    p2=validar_contrasenas(password,verify)
    e=validar_email(email)
    if u or p or p2 or e:
        errores = {'username':username,'email':email,'u_error':u,'p1_error':p,'p2_error':p2,'e_error':e}
        return errores
    else:
        return None
def codificar(user_id=""):
    return str(user_id+"|"+hashlib.md5(user_id).hexdigest())

class SignUpHandler(Handler):
    def get(self):
        self.render("SignUp.html")
    def post(self):  
        errores = {}  
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        errores = validar_datos(username,password,verify,email)
        if errores:
            self.render("signup.html", **errores)
        else:
            code = codificar(username)
            e = Users(username = username, password = password, email = email, cookie_code=code)
            e.put()
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' %codificar(username))
            self.redirect("/")