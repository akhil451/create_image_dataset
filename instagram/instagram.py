import instaloader

## bloiler plate code below

def search_instagram_images(keywords, n):
    L = instaloader.Instaloader()

    for keyword in keywords:
        print(f"Searching for images with keyword: {keyword}")
        try:
            search_results = L.get_hashtag_posts(L.context).get_profiles_by_username(keyword)
            if search_results:
                profile = search_results[0].profile
                posts = profile.get_posts()

                count = 0
                for post in posts:
                    if post.typename == 'GraphImage':
                        print(f"Downloading image: {post.url}")
                        count += 1
                        if count >= n:
                            break
            else:
                print("No results found for the keyword.")
        except instaloader.exceptions.ConnectionException:
            print("Error: Failed to connect to Instagram. Please check your internet connection.")

        print()

# Example usage
keywords = ["cats", "dogs", "nature"]
num_images_per_keyword = 5

search_instagram_images(keywords, num_images_per_keyword)
