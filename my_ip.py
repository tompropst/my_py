import urllib.request
import urllib.error
import re
import socket


def valid_ipv4(ip_string):
    pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    return re.match(pattern, ip_string)


def valid_ip(ip_string):
    return valid_ipv4(ip_string)


def public_ip(url="http://ipinfo.io/ip"):
    try:
        resource = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        return None
    content = resource.read().decode(resource.headers.get_content_charset())
    ip_string = content.strip()
    return ip_string if valid_ipv4(ip_string) else None


def local_ip(remote_ip="8.8.8.8", remote_port=80):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect((remote_ip, remote_port))
            ip_string = s.getsockname()[0]
            return ip_string if valid_ipv4(ip_string) else None
        except OSError as e:  # Most likely, network unreachable
            return None
