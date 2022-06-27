from page.NoIP.NoIP import NoIP
from model.NoIP.hostname import Hostname
from model.ip import Ip

# Current IPv4
current_ip = Ip.get_ip_public()

# New Host Name
host = Hostname('tmt22', current_ip)

print('Watch readme to run')

# noIp = NoIP()
# noIp.login()
# noIp.create_new_hostname(host.hostname, host.ipv4_address)
# noIp.delete_hostname(host.hostname)
# noIp.refresh_page('https://my.noip.com/dynamic-dns')
# noIp.check_exits_host()
# noIp.update_domain('svtest')
