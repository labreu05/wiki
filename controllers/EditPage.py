from controllers.Handler import Handler
from models.pages import Pages
from models.users import Users
from models.history import History

class EditPageHandler(Handler):
	def get(self,page):
		user = self.request.cookies.get('user_id')
		if user:
			self.render("PageEdit.html",content=Pages.get_content(page),user=user.split("|")[0])
		else:
			self.redirect("/login")

	def post(self,page):
		page_entry = None
		long_url = self.request.url
		url = long_url[long_url.rfind('/'):]
		user = str(self.request.cookies.get('user_id'))
		content = self.request.get("content")
		self.write(url)
		if content:
			new_page = Pages.verify_page(url);
			if new_page:
				new_page.content = content
			else:
				new_page = Pages(url=url,user=user,content=content)
			version = History.get_versions(url).count()+1
			page_entry = History(url=url,version=version,user=user,content=content)
			page_entry.put()
			new_page.put()
			self.redirect(url)
		#renderisar el error en pantalla, debe introducir un contenido
