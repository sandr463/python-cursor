import requests


def get_data(url: str):
    with open('img.jpg', 'bw') as file:
        file.write(requests.get(url).content)


if __name__ == '__main__':
    get_data('https://dummyimage.com/600x400/000/fff')
