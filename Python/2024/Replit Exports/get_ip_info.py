
import ipinfo
import sys 
try:
  ipaddress = sys.argv[1]
except indexError:
  ipaddress = None


accesstoken = '<0ea96832bd8cdd>'
client = ipinfo.getclient(accesstoken)
details = client.getdetails(ipaddress)
for key, values in details.all.items():
  print(key + value)