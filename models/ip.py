import requests

class Ip():

  def get_ip_public():
    r = requests.get('https://api.ipify.org?format=json')
    ipv4 = r.json()
    return ipv4['ip']