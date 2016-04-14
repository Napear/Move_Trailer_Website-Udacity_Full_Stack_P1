import sys

import fresh_tomatoes
from media import MediaMaker

"""This script uses the fresh_tomatoes module to dynamically generate an html document
containing a gallery of movie posters, each of which links to a trailer for that film"""

# this list must contain the proper title of a film as key and the YouTube ID for its trailer as the respective value
movie_list = {
    'Forrest Gump': 'eYSnxZKTZzU',
    'Star Wars: Episode V': 'JNwNXF9Y6kY',
    'Mallrats': 'LU8762ow8is',
    'Fargo': 'h2tY82z3xXU',
    'Master and Commander': 'KpNhN-L9L-g',
    'Gladiator': '0BLZbrLogTo',
    'Not A Real Movie': 'not_a_real_link'}

# Create a list of Movie objects (favs[]) from the entries in movie_list
favs = []
for key, value in movie_list.iteritems():
    movie = MediaMaker.create_movie(key, value)
    if movie:  # only adds movies with valid data
        favs.append(movie)

if not favs:  # exit execution if no Movie object were created
    sys.exit('[!!] No movie data found')

favs.sort(key=lambda x: x.title)  # sort the list of movies by title
fresh_tomatoes.open_movies_page(favs)  # generate the html doc
