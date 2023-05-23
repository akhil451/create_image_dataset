import requests
import ast
import json
import urllib.request
import os
import itertools

def get_image_links(category: str, n_images: int, authcode: str):
    my_headers = {"Authorization": authcode}
    response = requests.get(
        "https://api.pexels.com/v1/search?query="
        + category
        + "&per_page="
        + str(n_images),
        headers=my_headers,
    )
    json_data = json.loads(response.text)
    image_links = []
    print(json_data)
    for i in json_data["photos"]:
        try:
            image_link = i["src"]["original"]
            image_links.append((image_link, category))
        except Exception as error:
            print(error)
    return image_links


def download_pexel_image(output_loc: str, category: str, image_link: str):
    if not os.path.exists(os.path.join(output_loc, category)):
        os.makedirs(os.path.join(output_loc, category))
    image_path = os.path.join(
        output_loc,
        category,
        "pexels_" + image_link.rsplit("/", 1)[-1].rsplit("?", 1)[0],
    )
    response = requests.get(image_link, stream=True)
    with open(image_path, "wb") as outfile:
        outfile.write(response.content)


def download_pexel_images(
    auth_code: str, output_loc: str, n_images_per_class: int, categories: ast.List
):
    """
    Accumulate all image links at one place. To incorporate multiprocessing later
    """
    all_image_links = []
    try:
        for category in categories:
            image_links = get_image_links(category, n_images_per_class, auth_code)

            all_image_links.append(image_links)
        flat_list = list(itertools.chain(*all_image_links))
        for image_link in flat_list:
            download_pexel_image(output_loc, image_link[1], image_link[0])
    except Exception as error:
        print(error)


if __name__ == "__main__":
    download_pexel_images(
        auth_code=authcode,
        output_loc="temp",
        n_images_per_class=10,
        categories=["car", "shoes"],
    )
