import urllib.request
import urllib.error
import re
import socket

import netifaces


def valid_ipv4(ip_string):
    pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    return re.match(pattern, ip_string)


def valid_ip(ip_string):
    return valid_ipv4(ip_string)


def public_ip(url="http://ipinfo.io/ip"):
    try:
        resource = urllib.request.urlopen(url)
    except urllib.error.URLError:
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
        except OSError:  # Most likely, network unreachable
            return None


def local_mac():
    ip = local_ip()
    if not ip:
        return None  # Interface that routes to the public is not found
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET not in addresses:
            continue
        if_ip = addresses[netifaces.AF_INET][0]["addr"]
        if if_ip == ip:
            return addresses[netifaces.AF_LINK][0]["addr"]
