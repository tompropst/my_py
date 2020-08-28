import unittest

from my_py import my_ip


class TestMyIP(unittest.TestCase):

    def test_valid_ipv4_good(self):
        self.assertTrue(my_ip.valid_ipv4("127.0.0.1"))
        self.assertTrue(my_ip.valid_ipv4("255.255.255.255"))
        self.assertTrue(my_ip.valid_ipv4("0.0.0.0"))
        self.assertTrue(my_ip.valid_ipv4("1.1.1.1\n"))

    def test_valid_ipv4_bad(self):
        self.assertFalse(my_ip.valid_ipv4("hello"))
        self.assertFalse(my_ip.valid_ipv4("1.1.1.a"))
        self.assertFalse(my_ip.valid_ipv4("2241.4.1.9"))
        self.assertFalse(my_ip.valid_ipv4("224,4.1.9"))

    def test_valid_ip(self):
        self.test_valid_ipv4_good()
        self.test_valid_ipv4_bad()

    def test_public_ip_default_site(self):
        public_ip = my_ip.public_ip()
        self.assertIsNotNone(public_ip)

    def test_public_ip_bad_response(self):
        response = my_ip.public_ip("https://google.com")
        self.assertIsNone(response)

    def test_local_ip_default(self):
        local_ip = my_ip.local_ip()
        self.assertIsNotNone(local_ip)

    def test_local_mac_default(self):
        local_mac = my_ip.local_mac()
        self.assertIsNotNone(local_mac)
