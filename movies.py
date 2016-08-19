import media
import fresh_tomatoes

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=EzETGqZN6dU")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                     "http://vignette3.wikia.nocookie.net/moviepedia/images/2/29/Poster-de-ratatouille.jpg/revision/latest?cb=20130930090447&path-prefix=de",
                     "https://www.youtube.com/watch?v=wlCAq45TcxU")

movies = [avatar, ratatouille]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
