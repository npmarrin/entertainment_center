# See https://github.com/youtube/api-samples/blob/master/python/search.py
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeSearch:

    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='

    def __init__(self, developer_key, logger):
        self.developer_key = developer_key
        self.logger = logger

    def search(self, search_string, max_results=1):

        try:
            youtube = build(YoutubeSearch.YOUTUBE_API_SERVICE_NAME,
                            YoutubeSearch.YOUTUBE_API_VERSION,
                            developerKey=self.developer_key)

            # Call the search.list method to retrieve results matching the specified
            # query term.
            search_response = youtube.search().list(
                q=search_string,
                part='id,snippet',
                maxResults=max_results,
                type='video'
            ).execute()

            videos = []

            for search_result in search_response.get('items', []):
                videos.append('%s%s' % (YoutubeSearch.YOUTUBE_VIDEO_URL, search_result['id']['videoId']))

            return videos
        except HttpError, e:
            self.logger.critical('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
            raise
