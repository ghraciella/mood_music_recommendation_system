# Save the routes where our users can go to on our page
# Everything that isn't related to authentication (like login) comes in here
from flask import render_template
from flask_appbuilder import expose, BaseView

class Views(BaseView):
    route_base = '/'
    index_template = 'index.html'
    # Define a view
    @expose('/')
    def index(self):
        return  render_template('index.html')


    @expose('/try-me')
    def try_me(self):
        return render_template('try-me.html')
