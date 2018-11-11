import requests


def download_im(url: str):
    r = requests.get(url)
    with open('image.png', 'wb') as f:
        f.write(r.content)

    return r.content


url = 'https://dummyimage.com/600x400/000/fff'
