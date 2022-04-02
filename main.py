### refer this ---> https://gist.github.com/namoopsoo/154c97ef4fa0d36a4daffeeb0d1affd5

import os
import sys
import argparse
import logging
from utils.file_utils import check_search_file,get_classes_to_download
from gooey import Gooey
from pexels.pexels import download_pexel_images

# @Gooey()     
def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser.add_argument('--use_pexels',action='store_true')
    parser.add_argument("--images_per_class",type=int,default=50)
    parser.add_argument('--search_file',default="user_files/classes_to_search.txt")
    parser.add_argument('--output_location', default = "user_files/temp")
    parser.add_argument('--pexels_auth_code', default = "")


    args = parser.parse_args()
    # print(args.use_pexels)
    if args.use_pexels:
        assert not args.pexels_auth_code==None
        assert check_search_file(args.search_file) == True
        if not os.path.exists(args.output_location):
            os.makedirs(args.output_location)
        categories =  get_classes_to_download(args.search_file)
        print("categories",categories)
        download_pexel_images(auth_code=args.pexels_auth_code,output_loc=\
            args.output_location,n_images_per_class=args.images_per_class,categories=categories)
if __name__ == "__main__":

    main()