import requests

class Ip():

  def validate_ip(self, ip):
    a = ip.split('.')
    if len(a) != 4:
      return False
    for x in a:
      if not x.isdigit():
        return False
      i = int(x)
      if i < 0 or i > 255:
        return False
    return True

  def get_ip_public():
    r = requests.get('https://api.ipify.org?format=json')
    ipv4 = r.json()
    return ipv4['ip']