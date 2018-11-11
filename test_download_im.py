from unittest import TestCase
from unittest.mock import patch
from Downloading_image import download_im


class TestDownload_im(TestCase):
    def test_download_im(self):
        with patch('requests.get') as mock_request:
            url = 'https://dummyimage.com/600x400/000/fff'
            mock_request.return_value.content = b'picture'
            self.assertEqual(download_im(url), b'picture')
