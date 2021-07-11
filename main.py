import glob, os, shutil

# this will return a list of paths for root path given by user..
def get_all_folder_dir(root_folder_path: str):
    return [
        folder_path
        for folder_path in glob.glob(
            glob.escape(root_folder_path) + "/*", recursive=True
        )
    ]


# this will go through all the folder_path and get all those folders sub folder.
def go_and_get_all_the_sub_folder(root_folder_path: list):
    sub_folders_array = []

    for folder_path in root_folder_path:
        sub_folders_array += get_all_folder_dir(folder_path)

    return sub_folders_array


# this will check if folders size is lower than 1gb..
# if folder size is lower then 1gb then delete the folder. else none.
def check_folder_size_and_delete_folder(movie_folder_path: str):
    for path, dirs, files in os.walk(movie_folder_path):
        # removing folder if folder is empty.
        if len(files) == 0:
            print("deleting empty folder-------------------->", path)
            shutil.rmtree(path)
            return

        # this will print if movie folder has multiple files.
        if len(files) >= 2:
            return print("multiple files -------------------> ", movie_folder_path)

        # getting file size
        file_path = os.path.join(path, files[0])
        file_size = os.path.getsize(file_path)

        # checking if file size is lower 800mb or not.
        # if file size is lower than 800mb then delete the file.
        if (file_size / 1024 / 1024) <= 800:
            shutil.rmtree(path)
            print(files[0], "deleted.")


def main():
    get_input = input("Please enter the root folder path: ")
    all_sub_folder = get_all_folder_dir(get_input)
    all_movies_folders = go_and_get_all_the_sub_folder(all_sub_folder)
    for folder_path in all_movies_folders:
        check_folder_size_and_delete_folder(folder_path)


if __name__ == "__main__":
    main()
