import urllib.request
import re


def public_ip(url="http://ipinfo.io/ip"):
    resource = urllib.request.urlopen(url)
    content = resource.read().decode(resource.headers.get_content_charset())
    ip_string = content.strip()
    pattern = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")
    return ip_string if re.match(pattern, ip_string) else None
