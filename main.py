import glob

# this will return a list of paths for root path given by user..
def get_all_folder_dir(root_folder_path: str):
    return [
        folder_path
        for folder_path in glob.glob(
            glob.escape(root_folder_path) + "/*", recursive=True
        )
    ]


def main():
    all_sub_folder = get_all_folder_dir(r"A:\.uploading_1tb\check")


if __name__ == "__main__":
    main()
