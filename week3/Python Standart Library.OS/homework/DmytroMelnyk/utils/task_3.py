# Task 3
#
# Using requests library, download image from this url https://dummyimage.com/600x400/000/fff
# and save it as a file on your device.

import requests


def dowlnoad_from_url(u: str):
    """
    Using requests library, download image from url and save it as a file on your device.
    :param u: url
    """

    r = requests.get(u)
    with open('img.jpg', 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
        print('Download file complete!')


if __name__ == '__main__':
    url = 'https://dummyimage.com/600x400/000/fff'

    dowlnoad_from_url(url)