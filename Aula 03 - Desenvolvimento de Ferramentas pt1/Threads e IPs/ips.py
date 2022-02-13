import ipaddress

ip = "192.168.0.1"
address = ipaddress.ip_address(ip)

print(address + 1000)

network = "192.168.0.0/29"
address = ipaddress.ip_network(network)

for i in address:
  print(i)