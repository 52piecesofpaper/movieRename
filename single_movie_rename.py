import re
import subprocess


#
def single_movie_rename(input_movie_name):  # input_movie_name is a string
    years = list(range(1950, 2051))
    years = list(map(str, years))  # convert the list elements to string elements for comparison later
    qualities = (
        '4k',
        '2160p',
        '1080p',
        '720p',
        '480p',
        '360p',
        '240p'
    )
    bad_words = (
        'X264',
        'BLURAY',
        'HDCAM',
        'BRRIP',
        'BRIP',
        'REMUX',
        'DDB',
        'ETRG',
        'HDTC',
        'V2',
        'XVID',
        'DD5.1',
        'EN',
        'NL',
        'SUBS'
    )

    # getting individual words of a movie file based on spaces
    input_movie_name_words_list = re.split('[();\-\\[\\].+\s]\s*', input_movie_name)
    input_movie_name_words_list = list(filter(None, input_movie_name_words_list))
    extension = input_movie_name_words_list[-1]
    input_movie_name_words_list.pop()

    input_movie_name_words_list_comp = re.split('[()\s]\s*', input_movie_name)
    input_movie_name_words_list_comp = list(filter(None, input_movie_name_words_list_comp))
    input_movie_name_words_list_comp.pop()

    initial_bad_word_flag = 0
    # print(input_movie_name_words_list_comp)
    # print(input_movie_name_words_list)  # to check for proper splitting
    if input_movie_name_words_list == input_movie_name_words_list_comp:
        for word in input_movie_name_words_list:
            if word.upper() in bad_words:
                print('bad word found!')
                initial_bad_word_flag = 1
                break
        if initial_bad_word_flag == 0:
            if input_movie_name_words_list[-1] in years:
                return 0
            if input_movie_name_words_list[-1] in qualities:
                return 0

    for year in years:
        f = 0
        for input_movie_name_word in input_movie_name_words_list:
            pos_year = 999
            if (year == input_movie_name_word) or (f'({year})' == input_movie_name_word):
                pos_year = input_movie_name_words_list.index(input_movie_name_word)
                # print(pos_year)
                f = 1
                break
        if f == 1:
            break

    for quality in qualities:
        f = 0
        for input_movie_name_word in input_movie_name_words_list:
            pos_quality = 999
            if quality.casefold() == input_movie_name_word.casefold():
                pos_quality = input_movie_name_words_list.index(input_movie_name_word)
                # print(pos_quality)
                f = 1
                break
        if f == 1:
            break

    if pos_year < pos_quality:
        del input_movie_name_words_list[pos_year:]
    else:
        del input_movie_name_words_list[pos_quality:]

    for bad_word in bad_words:
        for input_movie_name_word in input_movie_name_words_list:
            if bad_word.casefold() == input_movie_name_word.casefold():
                # bad_word_index = input_movie_name_words_list.index(input_movie_name_word)
                input_movie_name_words_list.remove(input_movie_name_word)
    input_movie_name_words_list = list(filter(None, input_movie_name_words_list))
    if pos_year != 999:
        input_movie_name_words_list.append(f'({year})')
    if pos_quality != 999:
        input_movie_name_words_list.append(f'({quality})')
    final_movie_name = ' '.join(input_movie_name_words_list)
    final_movie_name = final_movie_name + "." + extension

    subprocess.Popen(['mv', input_movie_name, final_movie_name])
    return 1

    # print(final_movie_name)


# input_movie = "Spider-Man.Far.from.Home.brip.2028.Spiderman-.1080p.BluRay.x264-MkvCag.mkv"
# single_movie_rename(input_movie)