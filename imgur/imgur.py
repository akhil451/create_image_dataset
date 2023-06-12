import requests
from bs4 import BeautifulSoup

### boilerplate code below

def search_imgur(keyword, n):
    """Searches Imgur for images with the given keyword.

    Args:
        keyword (str): The keyword to search for.
        n (int): The number of images to return.

    Returns:
        list: A list of the first `n` image links found.
    """
    url = 'https://imgur.com/search?q={}'.format(keyword)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print("soup",soup)
    image_links = []
    for image in soup.find_all('div', class_='post-image'):
        print("image",image)
        image_link = image.find('a')['href']
        image_links.append(image_link)
    return image_links[:n]

def main():
    keyword = "cats"
    n = 10
    image_links = search_imgur(keyword, n)
    for image_link in image_links:
        print(image_link)

if __name__ == "__main__":
    main()
