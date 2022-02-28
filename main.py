import requests
import ast
import json
import urllib.request
import os

def get_image_links(category,n_images):
    response = requests.get("https://api.pexels.com/v1/search?query="+category+"&per_page=10",headers= my_headers)
    json_data = json.loads(response.text)
#     print( json_data['photos'][0]['src']['large'])
    image_links= []
    for i in json_data['photos']:
#         print(i)
        image_link = i['src']['large']
#         print(image_link)
        image_links.append(image_link)
    return image_links

def download_images(category,image_links):
    if not os.path.exists("temp/data/"+category):
        os.makedirs("temp/data/"+category)
    for image_link in image_links:
#         urllib.request.urlretrieve(image_link, os.path.join("temp/data/"+category,image_link.rsplit("/",1)[-1]))
        image_path = os.path.join("temp/data/"+category,image_link.rsplit("/",1)[-1].rsplit("?",1)[0])
        response = requests.get(image_link, stream=True)
        with open(image_path, 'wb') as outfile:
            outfile.write(response.content)