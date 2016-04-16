# Movie Trailer Web Page
---

This is a simple program designed to dynamically create a web page with a gallery of movie posters which can be clicked to show the trailer for the corresponding movie.  

## Usage
---

The three python files (entertainment_center.py, media.py and fresh_tomatoes.py) must all be all be placed in the same folder.  Next the title and YouTube ID of the trailer for each film to be displayed should be added to the movie_list hash located in the entertainment_center.py file. 
<pre>movie_list = {'<b>Move Title</b>': '<b>YouTube ID</b>'}`</pre>
 
 Finally the run the entertainment_center.py script. 

`python  ./entertainment_center.py`

## External Resources
---

The information for each film is obtained via the Open Movie Database API (OMDb).  Information about the API can be found at [http://omdbapi.com/](http://omdbapi.com/)

This program was writen as part of the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) and fresh_tomatoes.py is sourced from [ardash0806/ud036_StarterCode](https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py) which is included in the course materials.
