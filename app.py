"""
  This file will define workflow function.
"""
from models.NoIP.NoIP import NoIP
from models.hostname import Hostname
from models.ip import Ip

# Current IPv4
current_ip = Ip.get_ip_public()

# New Host Name
# host = Hostname('svtest', current_ip)

noIp = NoIP()
noIp.login()
# noIp.create_new_hostname('test1', '116.108.47.227')
# noIp.delete_hostname('svtest.ddns.net', noIp.index_hostname('svtest.ddns.net'))
# noIp.refresh_page('https://my.noip.com/dynamic-dns')

# def get_list_host_name():
#   return noIp.list_host_name()

# listhost = get_list_host_name()
# print(listhost)
# noIp.check_exits_host()
# noIp.update_domain_manual('test1', '116.108.47.228')
# noIp.update_domain_auto('test1')
