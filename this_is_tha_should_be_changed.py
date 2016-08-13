import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">
	<link type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/redmond/jquery-ui.css" rel="stylesheet" />

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="https://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <!-- <link href="https://getbootstrap.com/examples/navbar-fixed-top/navbar-fixed-top.css" rel="stylesheet"> -->
    <!-- Script for this site -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <style type="text/css" media="screen">
		body {
		    width: 80%;
		    margin: 30px auto;
		    font-family: sans-serif;
		}
		#trailer .modal-dialog {
		    margin-top: 200px;
		    width: 640px;
		    height: 480px;
		}
		.hanging-close {
		    position: absolute;
		    top: -12px;
		    right: -12px;
		    z-index: 9001;
		}
		#trailer-video {
		    width: 100%;
		    height: 100%;
		}
		.scale-media {
		    padding-bottom: 56.25%;
		    position: relative;
		}
		.scale-media iframe {
		    border: none;
		    height: 100%;
		    position: absolute;
		    width: 100%;
		    left: 0;
		    top: 0;
		    background-color: white;
		}
		.gallery-container {
		    display: flex;
		    flex-wrap: wrap;
		}
		h3 {
		    text-align: center;
		    font-size: 1.65em;
		    margin: 0 0 30px;
		}
		.photo {
		    display: inline-block;
		    margin-bottom: 8px;
		    width: calc(50% - 4px);
		    margin-right: 8px;
		    text-decoration: none;
		    color: black;
		}
		.photo:nth-of-type(2n) {
		    margin-right: 0;
		}
		@media screen and (min-width: 50em) {
		    .photo {
		        width: calc(25% - 6px);
		    }
		    .photo:nth-of-type(2n) {
		        margin-right: 8px;
		    }
		    .photo:nth-of-type(4n) {
		        margin-right: 0;
		    }
		}
		.photo:hover img {
		    transform: scale(1.15);
		}
		figure {
		    margin: 0;
		    overflow: hidden;
		}
		figcaption {
		    margin-top: 15px;
		}
		img {
		    border: none;
		    max-width: 100%;
		    height: auto;
		    display: block;
		    background: #ccc;
		    transition: transform .2s ease-in-out;
		}
		body > .text-container {
			padding-top: 30px;
		    margin: 20px 0px 10px;
		}
		.footer {
		    position: absolute;
		    bottom: 0;
		    width: 100%;
		    /* Set the fixed height of the footer here */
	    
		    height: 60px;
		    background-color: #f5f5f5;
		}
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.photo', function (event) {
            var sourceUrl = $(this).attr('data-trailer-youtube-url')
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
    </script>

        <script src="https://getbootstrap.com/assets/js/ie-emulation-modes-warning.js"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
'''
# The main page layout and title bar
main_page_content= '''
<body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" />
                </a>
                <div class="scale-media" id="trailer-video-container">
                </div>
        </div>
    </div>

    <!-- Content -->
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Project name</a>
            </div>
            <div id="navbar" class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li><a href="#">Home</a>
                    </li>
                    <li><a href="#about">About</a>
                    </li>
                    <li><a href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
            <!--/.nav-collapse -->
        </div>
    </nav>
    <div class="text-container">
        <h3>Action</h3>
	 </div>
    <hr>
    <div class="gallery-container">
        {movie_tiles_action}
    </div>
    <div class="text-container">
        <h3>Comedy</h3>
    </div>
    <hr>
    <div class="gallery-container">
        {movie_tiles_comedy}
    </div>
    <div class="text-container">
        <h3>Drama</h3>
    </div>
    <hr>
    <div class="gallery-container">
        {movie_tiles_drama}
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>
        window.jQuery || document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"><\/script>')
    </script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="https://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
</body>

</html>
'''
# A single movie entry html template
movie_tile_content = '''
	<a class="photo" data-trailer-youtube-url="http://www.youtube.com/embed/{trailer_youtube_id}?autoplay=1&html5=1" data-toggle="modal" data-target="#trailer">
		<figure>
   			<img src="{poster_image_url}"><img>
   				<figcaption>
   	 			{movie_title}
   				</figcaption>
   	 	</figure>
   	</a>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(action,comedy,drama):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles_action=create_movie_tiles_content(action),
        movie_tiles_comedy=create_movie_tiles_content(comedy),
        movie_tiles_drama=create_movie_tiles_content(drama))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)