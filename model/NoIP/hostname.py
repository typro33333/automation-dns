
class Hostname():
  """
    - This class will define hostname on NoIP when we have access.
    - And it often use for:
      1. Define every host name have declare.
      2. Create new host name.
      3. Delete host name.
  """

  hostname = ''
  ipv4_address = ''

  def __init__(self, hostname, ipv4_address):
    self.hostname = str(hostname)
    self.ipv4_address = str(ipv4_address)
