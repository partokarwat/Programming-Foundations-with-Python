import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class TvShow(Video):
    def __init__(self, tv_show_title, tv_show_season, tv_show_episode,
                 tv_show_tv_station):
        Video.__init__(self, tv_show_title, 0)
        self.tv_show_season = tv_show_season
        self.tv_show_episode = tv_show_episode
        self.tv_show_tv_station = tv_show_tv_station

    def get_local_listing(self):
        print("Something")    

class Movie(Video):
    """ This class provides a way to store moview related information"""
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        Video.__init__(self, movie_title, 0)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
