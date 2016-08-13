class Video(object):
    def __init__(self,title,duration):
        self.title  		= title
        self.duration   	= duration

class Movie(Video):
    def __init__(self,title, poster , trailer, category):
        super(Movie, self).__init__(title,"")
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.category = category




