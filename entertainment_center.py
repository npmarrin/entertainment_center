#!/usr/bin/python

# This program generates and html file that shows movies and trailers based on IMDb's Top 250 list
# Sample usage:
#   python entertainment_center.py --key={DEVELOPER_KEY} --max-results=10
# NOTE: To use this program, you must provide a developer key obtained
#       in the Google APIs Console.

import argparse
from logger import Logger
from fresh_tomatoes import open_movies_page
from youtube_search import YoutubeSearch
from imdb_search import IMDBSearch


def generate_fresh_tomatoes_html(youtube_api_key, max_results, logger):

    imdb = IMDBSearch(logger)
    movies = imdb.get_top250(max_results)

    for movie in movies:

        youtube_search = YoutubeSearch(youtube_api_key, logger)
        search_result = youtube_search.search(movie.title + 'official trailer')
        if search_result:
            movie.trailer_youtube_url = search_result[0]

    open_movies_page(movies)


if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-k','--key', help='Google API developer key', required=True)
    parser.add_argument('-M','--max-results', help='Max results', default=25, type=int)
    args = parser.parse_args()

    generate_fresh_tomatoes_html(args.key, args.max_results, Logger.get_logger())
