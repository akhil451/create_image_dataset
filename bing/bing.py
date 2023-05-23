
import os, sys
import shutil
from pathlib import Path
from utils.file_utils import create_folder
try:
    from bing_image_downloader import Bing
except ImportError:  # Python 3
    from .bing_image_downloader import Bing


def download(query, limit=100, output_dir='dataset', adult_filter_off=True, 
force_replace=False, timeout=60, filter="", verbose=True):

    # engine = 'bing'
    if adult_filter_off:
        adult = 'off'
    else:
        adult = 'on'

    
    image_dir = Path(output_dir)

    if force_replace:
        if Path.is_dir(image_dir):
            shutil.rmtree(image_dir)

    # check directory and create if necessary
    try:
        if not Path.is_dir(image_dir):
            Path.mkdir(image_dir, parents=True)

    except Exception as e:
        print('[Error]Failed to create directory.', e)
        sys.exit(1)
        
    print("[%] Downloading Images to {}".format(str(image_dir.absolute())))
    bing = Bing(query, limit, image_dir, adult, timeout, filter, verbose)
    bing.run()


def bing_downloader(categories,n_images_per_category,output_dir):
    for category in categories:
        output_dir_category = os.path.join(output_dir,category)
        create_folder(output_dir_category)
        download(str(category), limit=n_images_per_category,  output_dir=output_dir_category, adult_filter_off=False, force_replace=False, timeout=60)

if __name__ == '__main__':
    download('dog', output_dir="temp\\TEST", limit=10, timeout=1)

