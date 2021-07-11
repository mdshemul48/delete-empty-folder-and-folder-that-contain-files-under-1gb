import glob

# this will return a list of paths for root path given by user..
def get_all_folder_dir(root_folder_path: str):
    return [
        folder_path
        for folder_path in glob.glob(
            glob.escape(root_folder_path) + "/*", recursive=True
        )
    ]


# this will go through all the folder_path and get all those folders sub folder.
def go_and_get_all_the_sub_folder(root_folder_path):
    sub_folders_array = []

    for folder_path in root_folder_path:
        print(folder_path)
        sub_folders_array += get_all_folder_dir(folder_path)

    return sub_folders_array


def main():
    all_sub_folder = get_all_folder_dir(r"A:\.uploading_1tb\check")
    all_movies_folders = go_and_get_all_the_sub_folder(all_sub_folder)


if __name__ == "__main__":
    main()
