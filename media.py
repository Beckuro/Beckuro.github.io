class Video(object):
    def __init__(self,title,duration,starring, year):
        self.title  		= title
        self.duration   	= duration
        self.starring		= starring
        self.year			= year

class Movie(Video):
    def __init__(self, title, plot, starring, poster, trailer, category, year):
        super(Movie, self).__init__(title,"",starring,year)
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.category = category
        self.plot	= plot

    def getActor(self,starring):
    	actors = starring
    	starring  = ""

    	for actor in actors:
    		starring += actor

    	return starring 



