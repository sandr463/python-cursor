import requests


def download_image(url: str):
    r = requests.get(url)

    file = open('image.png', 'wb')
    file.write(r.content)
    file.close()
