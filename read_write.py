import os


def read_files():
    if not os.path.exists('directoryHistory.txt'):
        rename_directory_history = open('directoryHistory.txt', 'w+')
        rename_directory_history.close()
    rename_directory_history = open("directoryHistory.txt")
    lines = rename_directory_history.read().splitlines()
    rename_directory_history.close()
    return lines


def write_to_file(address):
    rename_directory_history = open("directoryHistory.txt")
    lines = rename_directory_history.read().splitlines()
    if address in lines:
        rename_directory_history.close()
        return
    else:
        rename_directory_history.close()
        rename_directory_history = open("directoryHistory.txt", "a+")
        rename_directory_history.seek(0)
        data = rename_directory_history.read(2)
        if len(data) > 0:
            rename_directory_history.write("\n")
            rename_directory_history.write(address)
        else:
            rename_directory_history.write(address)
    rename_directory_history.close()
