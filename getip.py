import requests

def get_public_ip():
    ip = requests.get('https://ifconfig.co/ip').text.strip()
    return ip

print(get_public_ip())

