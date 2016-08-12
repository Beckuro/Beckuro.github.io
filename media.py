class Video(object):
    VALID_RATING = ["G", "PG" , "PG-13" , "R"]
    def __init__(self,title,duration):
        self.title  		= title
        self.duration   	= duration

class Movie(Video):
    def __init__(self,title , duration, poster,trailer):
        super(Movie, self).__init__(title,duration)
        self.poster_image_url = poster
        self.trailer_youtube_id = trailer

