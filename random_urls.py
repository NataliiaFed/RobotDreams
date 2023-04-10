import requests
import random

google_url = 'https://www.google.com/'
facebook_url = 'https://www.facebook.com/'
twitter_url = 'https://twitter.com/'
amazon_url = 'https://www.amazon.com/'
apple_url = 'https://www.apple.com/'
urls = [google_url, facebook_url, twitter_url, amazon_url, apple_url]

url = random.choice(urls)

res = requests.get(url)
print(f"Url: {url}\nStatus code: {res.status_code}\nHTML-code length: {len(res.text)}")