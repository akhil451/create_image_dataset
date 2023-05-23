# refer here -- https://pixabay.com/api/docs/
import os
import requests
from settings import pixabay_api_code
import os
import multiprocessing

def save_images_to_folders(image_dict, output_location):
    for key, links in image_dict.items():
        folder_path = os.path.join(output_location, key)
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

        for link in links:
            file_name = link.split('/')[-1]  # Extract file name from the link
            file_path = os.path.join(folder_path, file_name)

            try:
                response = requests.get(link)
                response.raise_for_status()
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f'Saved image: {file_name}')
            except requests.exceptions.RequestException as e:
                print(f'Error saving image: {file_name} - {e}')

def save_images_to_folders_multiprocessing(image_dict, output_location):
    # Determine the number of available CPU cores
    num_processes = multiprocessing.cpu_count()

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Distribute the work across the worker processes
    for key, links in image_dict.items():
        pool.apply_async(save_images_to_folder, args=(key, links, output_location))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

def save_images_to_folder(key, links, output_location):
    folder_path = os.path.join(output_location, key)
    os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

    for link in links:
        file_name = link.split('/')[-1]  # Extract file name from the link
        file_path = os.path.join(folder_path, file_name)

        try:
            response = requests.get(link)
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Saved image: {file_name}')
        except requests.exceptions.RequestException as e:
            print(f'Error saving image: {file_name} - {e}')

def download_pixabay_images(api_key, query_list, n_images_per_class, output_location):
    result_dict = {}
    for query in query_list:
        base_url = 'https://pixabay.com/api/'
        params = {
            'key': api_key,
            'q': query,
            'image_type': 'photo',
            'per_page': n_images_per_class
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            image_urls = [item['webformatURL'] for item in data['hits']]
            result_dict[query] = image_urls
        else:
            print('Error occurred during API request.')
            return []
    save_images_to_folders(result_dict, output_location)



if __name__ == "main":
    # Example usage
    query = ['nature',"dog"]  # Search query
    n_images_per_class = 5  # Number of image URLs to retrieve
    output_location = '.\\temp\\temp'

    image_urls = download_pixabay_images(pixabay_api_code, query, n_images_per_class)
    print("image_urls", image_urls)
    save_images_to_folders(image_urls, output_location)

