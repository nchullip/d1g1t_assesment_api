###########################################################################################
# 1. Use the IMDbPY (https://imdbpy.readthedocs.io/en/latest/index.html) package to
#    get movie data from IMDB database.
# 2. Get the list of bottom 100 movies (use the builtin method - get_bottom100_movies())
# 3. Get director name for each movies (use the builtin method - get_movie())
# 4. Collect only the movie names and director names(in ascending order by director names)
# 5. Pretty-print the data in json and store in a json file
############################################################################################


# Importing  Dependencies
import json, os
import pprint
import imdb

# Creating the IMDb object
ia = imdb.IMDb()

# Getting the list of of the Bottom 100 movies
bottom_movies = ia.get_bottom100_movies()

final_data_list = []
cntr = 0

# Traversing through each movie in the List
for movie in bottom_movies:
    cntr +=1
    print ("Getting Data for Movie " + str(cntr))
    temp_dir = {}
    dir_str = ""
    res = ia.get_movie(movie.movieID)
    for i in res['director']:
        # Appending  Director names in case Movie has multiple directors
        dir_str = dir_str + str(i)  + " / "
    dir_str = dir_str.rstrip(" / ")

    # Creating a Temp Directory  with Name of Movie and Director name and then append that to List
    temp_dir["name"] = str(movie)
    temp_dir["director"] = dir_str
    final_data_list.append(temp_dir)

# Sort the Final Data List based on Key 'director'
sorted_final = sorted(final_data_list, key= lambda i: i['director'])

# Check and Delete Output File, if already exists
if os.path.isfile("output.json"):
    os.remove("output.json")

# Create a JSON File from the Data List
with open('output.json', 'w') as fout:
    json.dump(sorted_final , fout)

# Pretty Print the Data on the Console
pprint.pprint(sorted_final)



