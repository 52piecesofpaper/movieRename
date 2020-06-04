import fnmatch
import os
from tkinter import messagebox

import pass_names_from_list


def find_movies_in_dir(search_directory):  # search_directory is a string
    directory = os.listdir(search_directory)
    # the path must exist and will be ensured before calling this function using path.exists()
    extensions = (
        'mkv',
        'mp4',
        'avi'
    )
    movie_files = []
    for file in directory:
        for extension in extensions:
            if fnmatch.fnmatch(file.lower(), f"*.{extension}"):
                movie_files.append(file)
                break
    if not movie_files:
        messagebox.showwarning("Nothing found", "No Movie files found in this directory")
    else:
        pass_names_from_list.pass_names_from_list(movie_files)
# input_search_directory = '/home/pratik/Downloads'
# find_movies_in_dir(input_search_directory)
