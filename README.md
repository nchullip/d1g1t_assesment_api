# d1g1t_assesment_api
Solution to d1g1t Assessment on API

### Problem Statement
* Use the IMDbPY (https://imdbpy.readthedocs.io/en/latest/index.html) package to get movie data from IMDB database.
* Get the list of bottom 100 movies (use the builtin method - get_bottom100_movies())
* Get director name for each movies (use the builtin method - get_movie())
* Collect only the movie names and director names(in ascending order by director names)
* Pretty-print the data in json and store in a json file

### Required Python Packages
* imdb
* json
* os
* pprint

### Solution
* Run the file ***api_test.py***.
* The script prints the Movie Name and Director Name of the Bottom 100 movies on the console, sorted by the Director Name.
* It creates a file ***output.json*** with all the data. 
* For handling movies with multiple directors, it appends the name separated by "**/**"
