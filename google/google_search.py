from mpire import WorkerPool
import requests
from googlesearch import search
import os

def process_page(page_url):
    response = requests.get(page_url)
    response.raise_for_status()
    data = response.json()
    items = data['items']
    for item in items:
        image_links.append(item['link'])
        
def accumulate_image_links(query, limit):
    image_links = []



    urls = []
    for url in search(query, num_results=limit, lang="en"):
        urls.append(url)

    with WorkerPool() as pool:
        pool.map(process_page, urls)

    return image_links

def download_images(image_links, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def download_image(image_link):
        try:
            response = requests.get(image_link)
            response.raise_for_status()
            image_name = image_link.split('/')[-1]
            image_path = os.path.join(output_dir, image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {image_name}")
        except Exception as e:
            print(f"Error downloading {image_link}: {e}")

    with WorkerPool() as pool:
        pool.map(download_image, image_links)

if __name__ == "__main__":
    query = "cats"
    limit = 10
    output_dir = "images"
    
    image_links = accumulate_image_links(query, limit)
    download_images(image_links, output_dir)
