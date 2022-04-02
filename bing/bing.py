## use this --- https://codingshiksha.com/python/python-3-script-to-build-a-bulk-bing-image-scraper-and-downloader-using-bing-image-downloader-library-full-project-for-beginners/

from bing_image_downloader import downloader


def bing_downloader(category,n_images_per_category,output_dir):
    downloader.download(str(category), limit=n_images_per_category,  output_dir=output_dir, adult_filter_off=False, force_replace=False, timeout=60)

if __name__ == "__main__":
   bing_downloader('cars',n_images_per_category=10,output_dir="user_files/temp")
