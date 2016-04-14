import json
import urllib

OMDD = 'http://www.omdbapi.com/?'  # API access point for the Open Movie Database


class Movie:
    """Data class for the storage of information about movies"""

    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url


class MediaMaker(object):
    """Static class used to create media objects"""

    @staticmethod
    def create_movie(title, trailer_youtube_id):
        """Returns a Movie object if data on the film can be found based on the title.
         Returns False if no data can be found.  Result logs are printed to stdout."""
        params = 't=' + title

        try:  # Attempt to retrieve film data from OMDd API
            movie_data = json.loads(urllib.urlopen(OMDD + params).read())
        except IOError, err:
            print("[!!] Could not contact OMDd for search " + params)
            print (err)
            return False

        if movie_data['Response'] != 'True':
            print ("[!] No data found with for \"" + title + "\"")
            return False

        print ("[*] Data recovered for " + movie_data['Title'])
        movie = Movie(
            movie_data['Title'],
            movie_data['Plot'],
            movie_data['Poster'],
            'https://youtu.be/' + trailer_youtube_id
        )
        return movie
