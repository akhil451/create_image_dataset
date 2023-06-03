### refer this ---> https://gist.github.com/namoopsoo/154c97ef4fa0d36a4daffeeb0d1affd5

import os
import sys
import argparse
import logging
from utils.file_utils import check_search_file, get_classes_to_download
from gooey import Gooey, GooeyParser
from pexels.pexels import download_pexel_images
from bing.bing import bing_downloader
from settings import pexels_auth_code


# @Gooey()
def main():
    # parser =
    parser = argparse.ArgumentParser()

    parser.add_argument("--SOURCES", action="store_true")
    parser.add_argument("--IMAGES_PER_CLASS", type=int, default=50)
    parser.add_argument("--OUTPUT_LOCATION","-o",default="user_files/temp")
    # parser = GooeyParser(description="My Cool GUI Program!")

    args = parser.parse_args()
    # print(args.use_pexels)
    categories = args.CATEGORIES.strip(" ").split(",")

    if not os.path.exists(args.OUTPUT_LOCATION):
        os.makedirs(args.OUTPUT_LOCATION)
    if "Pexels" in args.SOURCES:
        download_pexel_images(
            auth_code=pexels_auth_code,
            output_loc=args.OUTPUT_LOCATION,
            n_images_per_class=args.IMAGES_PER_CLASS,
            categories=categories,
        )
    if "Bing" in args.SOURCES:
        bing_downloader(
            categories,
            n_images_per_category=int(args.IMAGES_PER_CLASS),
            output_dir=args.OUTPUT_LOCATION,
        )

    if "Pixabay" in args.SOURCES:
        download_pixabay_images(pixabay_api_code, categories, args.IMAGES_PER_CLASS, args.OUTPUT_LOCATION)




if __name__ == "__main__":
    main()
