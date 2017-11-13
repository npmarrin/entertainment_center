from imdb import IMDb, IMDbDataAccessError
from media import Movie


class IMDBSearch:
    MAX_IMDB_RESULTS = 250

    def __init__(self, logger):
        self.logger = logger

    def get_top250(self, max_results):
        try:
            # Create the object that will be used to access IMDb's database.
            imdb = IMDb()  # by default access the web.
            # Retrieve the top 250 movies from IMDb
            imdb_top250 = imdb.get_top250_movies()
            # Array of movies obtained from IMDb
            movies = []

            if max_results > 250:
                max_results = IMDBSearch.MAX_IMDB_RESULTS

            for x in range(0, max_results):
                imdb_movie = imdb_top250[x]
                """
                    fetch additional metadata from IMDb
                    see imdb.get_movie_infoset() for a list of available info sets
                """
                imdb.update(imdb_movie, ['main'])

                movies.append(
                    Movie(
                        imdb_movie['title'].encode('iso-8859-1', 'replace'),
                        imdb_movie['plot outline'].encode('iso-8859-1', 'replace'),
                        imdb_movie['cover url'],
                        ''
                    )
                )

                self.logger.info(imdb_movie.summary())

            return movies

        except IMDbDataAccessError:
            self.logger.critical('Unable to access IMDb. Please check your internet connection')
            raise
