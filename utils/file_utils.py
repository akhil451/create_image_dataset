import os


def get_classes_to_download(file_loc: str):
    """reads the classes file line by line

    Args:
        file_loc (str): _description_

    Returns:
        _type_: _description_
    """
    with open(file_loc, "r") as file:
        Lines = file.readlines()
        lines = []
        # for line in Lines:
        Lines = list(map(lambda s: s.strip(), Lines))
        # lines.append(line)

    return Lines


def get_pexel_keys(file_loc: str):
    """gets pexel keys from file

    Args:
        file_loc (str): _description_

    Returns:
        _type_: _description_
    """
    with open(file_loc) as f:
        firstline = f.readline().rstrip()

    print(firstline)
    return firstline


def check_search_file(file_loc: str):
    """checks if search file exists

    Args:
        file_loc (str): _description_

    Returns:
        _type_: _description_
    """
    if os.path.exists(file_loc):
        return True

    return False


def create_folder(folder):
    """Creates a folder if it dows not exist

    Args:
        folder (_type_): _description_
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
