import unittest

import my_ip


class TestMyIP(unittest.TestCase):

    def test_public_ip_default_site(self):
        public_ip = my_ip.public_ip()
        self.assertIsNotNone(public_ip)

    def test_public_ip_bad_response(self):
        response = my_ip.public_ip("https://google.com")
        self.assertIsNone(response)
