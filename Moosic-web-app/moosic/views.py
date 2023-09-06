# Save the routes where our users can go to on our page
# Everything that isn't related to authentication (like login) comes in here
from flask import render_template
from flask_appbuilder import expose, BaseView, IndexView

class MoosicIndexViews(IndexView):
    route_base = '/'
    index_template = 'index.html'
    # Define a view
    @expose('/')
    def index(self):
        return  render_template('index.html')

class MoosicViews(BaseView):
    route_base = '/'
    genres = ['Jazz', 'Country', 'Pop', 'Reggae', 'Electronic', 'Indie Rock', 'Gospel', 
                'House', 'Hip Hop', 'Classical', 'R&B', 'Punk Rock', 'Folk', 'Techno', 'Disco', 'EDM', 'Rock',
                'Blues', 'Metal', 'Soul', 'Funk', 'Alternative', 'Dubstep', 'World Music', 'Rockabilly', 'Other']
    
    @expose('/choose-genre-mood')
    def choose_genre_mood(self):
        return render_template('choose-genre-mood.html', genres=self.genres)
    

    @expose('/list/')
    def list(self):
        return ""