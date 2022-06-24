from page.NoIP.NoIP import NoIP
from model.NoIP.hostname import Hostname

# New Host Name
host = Hostname('tmt22', '115.78.4.15')

noIp = NoIP()
noIp.login()
# noIp.create_new_hostname(host.hostname, host.ipv4_address)
# noIp.check_exits_host()
