import fresh_tomatoes
import media

def list_of_movies():
    FBAWTFT = media.Movie("Fantastic Beast and Where to Find Them", 
    	"http://sidomi.com/wp-content/uploads/2016/04/Fantastic-Beasts-And-Where-to-Find-Them.jpg",
    	"YdgQj7xcDJo", "act")
    Oldboy = media.Movie("Oldboy", "http://www.gstatic.com/tv/thumb/movieposters/35948/p35948_p_v8_aa.jpg" , 
    	"2HkjrJ6IK5E", "act")
    TDK = media.Movie("The Dark Night", "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_aa.jpg" , 
    	"EXeTwQWrcwY", "act")
    TH = media.Movie("The Hangover", "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg" , 
    	"vhFVZsk3XEs", "com")
    HGTG = media.Movie("The Hitchhiker's Guide to the Galaxy", "https://images-na.ssl-images-amazon.com/images/I/51N6THN5ZXL._SY445_.jpg" , 
    	"eLdiWe_HJv4", "com")
    DAD = media.Movie("Dumb and Dumber", "http://static.metacritic.com/images/products/movies/2/cbb1dc56593f3c3537d1b39735091077.jpg" , 
    	"GXHVlEklgQ", "com")
    TP = media.Movie("The Prestige", "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg" , 
    	"o4gHCmTQDVI", "dra")
    Boyhood = media.Movie("Boyhood", "http://t0.gstatic.com/images?q=tbn:ANd9GcTj0AWSMjSJ2T7vk2yQTjOIaU6XOnzXis9egJzJh6YBWrT0A5td" , 
    	"mbHXyWX4", "dra")
    TSR = media.Movie("The Shawsank Redemption", "https://i.jeded.com/i/the-shawshank-redemption.18663.jpg" , 
    	"6hB3S9bIaco", "dra")

    movies = [ FBAWTFT , Oldboy , TDK , TH , HGTG , DAD , TP , Boyhood , TSR]
    return movies
   
   

def create_page():
	movies = list_of_movies()
	action = []
	drama = []
	comedy = []

	for movie in movies:
		if movie.category == "act":
			action.append(movie)
		elif movie.category == "com":
			comedy.append(movie)
		else:
			drama.append(movie)
	print(comedy)
	fresh_tomatoes.open_movies_page(action,comedy,drama)

create_page()