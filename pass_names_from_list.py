# function to accept a list of movie file names and pass each one of them as string arguments to single_movie_rename()
import single_movie_rename


def pass_names_from_list(movie_file_list):
    renamed = 0
    print('Movies in directory: ')
    for movie_file in movie_file_list:
        print(movie_file)
        renamed = renamed + single_movie_rename.single_movie_rename(movie_file)
    return renamed
