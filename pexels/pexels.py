# import requests
# import ast
# import json
# import os
# import itertools
# import multiprocessing
# from settings import pexels_auth_code
# def get_image_links(category: str, n_images: int, authcode: str):
#     my_headers = {"Authorization": authcode}
#     response = requests.get(
#         "https://api.pexels.com/v1/search?query="
#         + category
#         + "&per_page="
#         + str(n_images),
#         headers=my_headers,
#     )
#     json_data = json.loads(response.text)
#     image_links = []
#     for i in json_data["photos"]:
#         try:
#             image_link = i["src"]["original"]
#             image_links.append((image_link, category))
#         except Exception as error:
#             print(error)
#     return image_links


# def download_pexel_image(output_loc: str, category: str, image_link: str):
#     if not os.path.exists(os.path.join(output_loc, category)):
#         os.makedirs(os.path.join(output_loc, category))
#     image_path = os.path.join(
#         output_loc,
#         category,
#         "pexels_" + image_link.rsplit("/", 1)[-1].rsplit("?", 1)[0],
#     )
#     response = requests.get(image_link, stream=True)
#     with open(image_path, "wb") as outfile:
#         outfile.write(response.content)


# def download_pexel_images(
#     auth_code: str, output_loc: str, n_images_per_class: int, categories: ast.List
# ):
#     """
#     Accumulate all image links at one place. To incorporate multiprocessing later
#     """
#     all_image_links = []
#     try:
#         for category in categories:
#             image_links = get_image_links(category, n_images_per_class, auth_code)
#             all_image_links.append(image_links)
#             print(category," -- ",len(image_links))
#         flat_list = list(itertools.chain(*all_image_links))
#         for image_link in flat_list:
#             download_pexel_image(output_loc, image_link[1], image_link[0])
#     except Exception as error:
#         print(error)


# if __name__ == "__main__":
#     from time import time
#     start = time()
#     download_pexel_images(
#         auth_code=pexels_auth_code,
#         output_loc="temp",
#         n_images_per_class=100,
#         categories=["car", "shoes"],
#     )
#     print("time taken", time()-start)


import requests
import ast
import json
import os
import itertools
import mpire
import multiprocessing
from settings import pexels_auth_code
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
    for i in json_data["photos"]:
        try:
            image_link = i["src"]["original"]
            image_links.append((image_link, category))
        except Exception as error:
            print(error)
    return image_links


def download_pexel_image(image_link_info):
    output_loc,category,image_link = image_link_info.split("-,&)-")
    # print("output_loc",output_/loc)
    # print("category",category)
    # print("image_link",image_link)
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
    all_image_links = []
    try:
        for category in categories:
            image_links = get_image_links(category, n_images_per_class, auth_code)
            for image_link in image_links:
                all_image_links.append(f"{output_loc}-,&)-{image_link[1]}-,&)-{image_link[0]}")
            # print(category,len(image_links))
        # Use mpire to execute the download_pexel_image function in parallel
        n_jobs= multiprocessing.cpu_count()*2
        print("n_jobs",n_jobs)
        with mpire.WorkerPool(n_jobs=n_jobs) as pool:
            pool.map(download_pexel_image, all_image_links)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    auth_code = pexels_auth_code
    import time
    start  = time.time()
    download_pexel_images(
        auth_code=auth_code,
        output_loc="temp",
        n_images_per_class=100,
        categories=["car", "shoes"],
    )
    print("time taken", time.time()-start)
