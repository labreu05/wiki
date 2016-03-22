from controllers.Handler import Handler
from models.pages import Pages
from models.users import Users

class EditPageHandler(Handler):
	def get(self,page):
		user = self.request.cookies.get('user_id')
		if user:
			self.render("PageEdit.html",content=Pages.get_content(page),user=user.split("|")[0])
		else:
			self.redirect("/login")

	def post(self,page):
		long_url = self.request.url
		url = long_url[long_url.rfind('/'):]
		user = str(self.request.cookies.get('user_id'))
		content = self.request.get("content")
		self.write(url)
		if content:
			new_page = Pages.verify_page(url);
			if new_page:
				new_page.content = content
				new_page.put()
			else:
				new_page = Pages(url=url,user=user,content=content)
				new_page.put()
			self.redirect(url)
		#renderisar el error en pantalla, debe introducir un contenido
