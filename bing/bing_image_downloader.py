from pathlib import Path
import urllib.request
import urllib
import imghdr
import posixpath
import re
import itertools
import uuid
import os
from mpire import WorkerPool
import multiprocessing
from multiprocessing import Value

n_jobs= multiprocessing.cpu_count()*2


'''
Python API to download images from Bing.
Author: Guru Prasad (g.gaurav541@gmail.com)
'''

class Bing:
    def __init__(self, query, limit_, output_dir, adult, timeout, filter='', verbose=True):
        # Initialize the Bing class
        self.download_count = 0
        self.limit = limit_ 
        self.query = query
        self.output_dir = output_dir
        self.adult = adult
        self.filter = filter
        self.verbose = verbose
        self.seen = set()
        self.page_counter = 0
        # Validate and set the limit and timeout values
        assert type(timeout) == int, "timeout must be an integer"
        self.timeout = timeout

        # Set the user agent headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                          'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

    def get_filter(self, shorthand):
        # Get the filter string based on the shorthand provided
        if shorthand == "line" or shorthand == "linedrawing":
            return "+filterui:photo-linedrawing"
        elif shorthand == "photo":
            return "+filterui:photo-photo"
        elif shorthand == "clipart":
            return "+filterui:photo-clipart"
        elif shorthand == "gif" or shorthand == "animatedgif":
            return "+filterui:photo-animatedgif"
        elif shorthand == "transparent":
            return "+filterui:photo-transparent"
        else:
            return ""

    def save_image(self, link, file_path):
        # Save the image to the specified file path
        request = urllib.request.Request(link, None, self.headers)
        image = urllib.request.urlopen(request, timeout=self.timeout).read()
        if not imghdr.what(None, image):
            print('[Error] Invalid image, not saving {}\n'.format(link))
            raise ValueError('Invalid image, not saving {}\n'.format(link))
        with open(str(file_path), 'wb') as f:
            f.write(image)

    def download_image(self, link):
        # Download the image from the provided link
        try:
            self.download_count+=1
            if int(self.download_count)<self.limit:
                self.download_count += 1
                path = urllib.parse.urlsplit(link).path
                filename = posixpath.basename(path).split('?')[0]
                file_type = filename.split(".")[-1]
                if file_type.lower() not in ["jpe", "jpeg", "jfif", "exif", "tiff", "gif", "bmp", "png", "webp", "jpg"]:
                    file_type = "jpg"

                if self.verbose:
                    print("[%] Downloading Image #{} from {}".format(self.download_count, link))

                self.save_image(link, self.output_dir.joinpath("bing_{}.{}".format(
                    str(uuid.uuid4()), file_type)))
                if self.verbose:
                    print("[%] File Downloaded !\n")
            else:
                pass
        except Exception as e:
            self.download_count -= 1
            print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))

    def run(self):
        # Run the image download process
        # total_links =  []
        n_files_present = len(os.listdir(self.output_dir))
        while self.download_count<self.limit:
            if self.verbose:
                print('\n\n[!!] Indexing page: {}\n'.format(self.page_counter + 1))
            # Parse the page source and download images
            request_url = 'https://www.bing.com/images/async?q=' + urllib.parse.quote_plus(self.query) \
                          + '&first=' + str(self.page_counter) + '&count=' + str(self.limit) \
                          + '&adlt=' + self.adult + '&qft=' + (
                                          '' if self.filter is None else self.get_filter(self.filter))
            request = urllib.request.Request(request_url, None, headers=self.headers)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf8')
            if html == "":
                print("[%] No more images are available")
                break
            links = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
            if self.verbose:
                print("[%] Indexed {} Images on Page {}.".format(len(links), self.page_counter + 1))
                print("\n===============================================\n")
            # total_links.append(links)
            # total_links= list(itertools.chain(*total_links))
            # with WorkerPool(n_jobs=n_jobs) as pool:  # Set the number of processes as per your requirement
            #     pool.map(self.download_image,links)
            for link in links:
                self.download_image(link)
            self.page_counter += 1
        
        # total_links= list(itertools.chain(*total_links))

        # Use multiprocessing for downloading images
        # with WorkerPool(n_jobs=n_jobs) as pool:  # Set the number of processes as per your requirement
        #         pool.map(self.download_image, total_links)
        # print("\n\n[%] Done. Downloaded {} images.".format(total_links))


if __name__ == "__main__":
    bing = Bing(query="your_query", limit=100, output_dir=Path("output"), adult="Off", timeout=10, verbose=True)
    bing.run()
