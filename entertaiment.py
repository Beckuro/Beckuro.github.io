import fresh_tomatoes
import media

def list_of_movies():
    FBAWTFT = media.Movie("Fantastic Beast and Where to Find Them", "unknown", 
    	"http://sidomi.com/wp-content/uploads/2016/04/Fantastic-Beasts-And-Where-to-Find-Them.jpg",
    	"YdgQj7xcDJo")
    Oldboy = media.Movie("Oldboy", "120 mins", "http://www.gstatic.com/tv/thumb/movieposters/35948/p35948_p_v8_aa.jpg" , 
    	"2HkjrJ6IK5E")
    TDK = media.Movie("The Dark Night", "120 mins", "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_aa.jpg" , 
    	"EXeTwQWrcwY")
    movies = [ FBAWTFT , Oldboy , TDK]
    return movies
   
   

def create_page():
	movies = list_of_movies()
	fresh_tomatoes.open_movies_page(movies)

create_page()