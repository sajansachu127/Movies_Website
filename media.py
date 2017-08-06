import webbrowser

'''This DocString explains that this is a class named movie_info'''

class Movie():

    '''This DocString is the constructor which initialize the instance and
     here we are also initializing instance variables'''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
		
	'''This DocString is the instance method,this method is called by the instace
       that has been created for this class'''
                    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
